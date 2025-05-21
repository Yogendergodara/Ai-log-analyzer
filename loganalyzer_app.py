import streamlit as st
import google.generativeai as genai
import os
import re
import json
import datetime

# ---------------------------- CONFIG ----------------------------
API_KEY = "AIzaSyCds1rxRCLW15nPst_jB4VAc5KsGTG-2VM"  # Replace with your actual Gemini API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")
HISTORY_FILE = "history/analysis_log.json"
os.makedirs("history", exist_ok=True)


# ---------------------------- FUNCTIONS ----------------------------

def parse_log_content(log_content):
    """Extract structured entries using regex from raw logs."""
    log_lines = log_content.strip().splitlines()
    extracted_logs = []

    # Common regex for Apache/Nginx-style access logs
    pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - .*? \[(?P<time>[^\]]+)\] "(?P<method>[A-Z]+) (?P<url>[^ ]+) HTTP/.*" (?P<status>\d+)')

    for line in log_lines:
        match = pattern.search(line)
        if match:
            info = match.groupdict()
            extracted_logs.append(
                f"[{info['time']}] IP: {info['ip']} — Method: {info['method']} — URL: {info['url']} — Status: {info['status']}"
            )
        else:
            # Include unmatched lines as is (e.g., kernel logs)
            extracted_logs.append(line)

    return "\n".join(extracted_logs)


def analyze_with_gemini(clean_log_text):
    prompt = (
        "Analyze the following server logs. For each entry, determine whether it's normal or an attack. "
        "If it's an attack, classify it using the MITRE ATT&CK framework, explain the technique and impact, "
        "highlight IoCs, privilege escalations, persistence, and post-exploitation. Add mitigation steps and CVEs.\n\n"
        f"Log Data:\n{clean_log_text}"
    )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ AI Analysis Error: {str(e)}"


def save_analysis(filename, result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = {"filename": filename, "timestamp": timestamp, "result": result}

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(new_entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


# ---------------------------- UI ----------------------------

st.set_page_config("AI Log Analyzer", layout="wide")
st.title("🛡️ AI Log Analyzer")
st.markdown("Upload log files, parse them using regex, and analyze them using **Gemini AI** with MITRE ATT&CK integration.")

tab1, tab2 = st.tabs(["📂 Upload & Analyze", "🕘 Analysis History"])

# Tab 1: Analyze
with tab1:
    file = st.file_uploader("Upload a `.log` or `.txt` file", type=["log", "txt"])
    if file:
        raw_logs = file.read().decode("utf-8")
        st.subheader("📜 Raw Logs")
        st.text_area("Preview", raw_logs, height=200)

        parsed_logs = parse_log_content(raw_logs)
        st.subheader("🧾 Parsed Log Summary")
        st.text_area("Formatted for AI", parsed_logs, height=200)

        if st.button("🔍 Analyze with Gemini"):
            with st.spinner("Running AI forensic analysis..."):
                ai_result = analyze_with_gemini(parsed_logs)

            st.success("✅ Analysis Complete")
            st.subheader("🧠 Gemini AI Analysis")
            st.text_area("Result", ai_result, height=400)
            save_analysis(file.name, ai_result)
    else:
        st.info("Upload a file to begin analysis.")

# Tab 2: History
with tab2:
    st.subheader("📂 Recent Analyses")
    history = load_history()
    if history:
        for entry in reversed(history[-10:]):
            with st.expander(f"{entry['filename']} — {entry['timestamp']}"):
                st.text_area("AI Result", entry['result'], height=250)
    else:
        st.info("No saved analysis history found.")