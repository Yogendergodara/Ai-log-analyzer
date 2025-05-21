# Ai-log-analyzer



# 🛡️ AI Log Analyzer (Gemini AI + Streamlit)

This project helps developers, analysts, and security teams quickly understand log data and detect suspicious patterns using AI. It features regex-based log parsing and forensic analysis powered by **Gemini AI** and MITRE ATT&CK.

---

## 🧠 Overview

**AI Log Analyzer** is a powerful AI-driven tool designed for **developers**, **network analysts**, and **cybersecurity teams** to quickly interpret log files and identify suspicious activities using **Google Gemini AI**.

It supports intelligent log parsing with **regex**, smart structuring of data, and forensic-grade analysis by referencing the **MITRE ATT&CK framework**. This tool bridges raw logs with meaningful security insights — all through a clean, web-based interface.

---

## 🔥 Features

- ✅ **AI-Driven Analysis**: Uses **Gemini AI** to classify logs as normal or attack-related
- ✅ **Regex-Based Parsing**: Extracts IPs, timestamps, methods, URLs, and status codes
- ✅ **MITRE ATT&CK Integration**: Classifies attacks with known TTPs
- ✅ **IoC Detection**: Highlights indicators of compromise and anomalies
- ✅ **Mitigation Strategies**: Includes CVEs and remediation advice
- ✅ **Local History Saving**: Stores all analysis results
- ✅ **Streamlit Interface**: Clean, interactive, and responsive

---

## ⚙️ Technologies Used

- **Python** – Core programming language
- **Streamlit** – Modern web UI
- **Regex (`re`)** – For structured log parsing
- **Google Generative AI** – Gemini 1.5 Pro model
- **JSON** – History persistence

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/ai-log-analyzer.git
cd ai-log-analyzer


2. Install Requirements

pip install -r requirements.txt
3. Add Your Gemini API Key
Open loganalyzer_app.py and replace:

API_KEY = "YOUR_GEMINI_API_KEY"
4. Run the App

streamlit run loganalyzer_app.py

📁 Folder Structure

ai-log-analyzer/
├── loganalyzer_app.py        # Main Streamlit app
├── requirements.txt          # Python dependencies
├── README.md                 # Project guide
└── history/
    └── analysis_log.json     # Auto-saved past results
👀 Sample Output
When you upload a .log file, you'll see:

Parsed logs in structured format

Gemini AI output with attack classification and MITRE mapping

Past analysis saved and viewable in History tab

💬 License
Open-source project. Use for learning, research, or internal audits.

