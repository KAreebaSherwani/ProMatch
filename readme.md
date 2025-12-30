# 🎯 PRO MATCH

### Enterprise Resume Matching System




## ✨ Features

### 🎯 Intelligent Matching Engine

* **Multi-Factor Scoring Algorithm**
  Analyzes must-have skills (50%), semantic match (25%), nice-to-have skills (15%), and experience (10%)
* **Natural Language Processing (NLP)**
  Contextual understanding of resumes and job descriptions
* **Synonym Recognition**
  Detects skill variations (e.g., JS = JavaScript)
* **OR Logic Support**
  Handles alternative requirements (e.g., Tableau OR Power BI)

---

### ⚡ Rapid Processing

* **Batch Upload** – Process up to 100 resumes simultaneously
* **Real-Time Analysis** – 2–5 seconds per resume
* **Progress Tracking** – Live status updates
* **Multi-Format Support** – PDF, DOCX, and TXT

---

### 📊 Comprehensive Analytics

* **Executive Dashboard** – Key hiring metrics at a glance
* **Visual Charts** – Interactive score distributions and breakdowns
* **Detailed Candidate Profiles** – Skill gap identification
* **Ranking System** – Automatic ranking with medal badges

---

### 🔍 Advanced Extraction

* **Contact Information** – Email, phone, LinkedIn
* **Professional Details** – Total and skill-specific experience
* **Education** – Degree detection (Associate to PhD)
* **Certifications** – Professional certifications and licenses
* **Resume Quality Scoring** – Completeness score (0–100%)

---

### 📥 Export Options

* **CSV Reports** – Structured spreadsheet data
* **JSON Data** – Complete nested analysis
* **Summary Reports** – Professional text reports with recommendations

---

### 🔒 Security and Privacy

* **Local Processing** – Data processed on your infrastructure
* **No External APIs** – Zero third-party data sharing
* **In-Memory Processing** – No permanent data storage
* **Session Isolation** – Independent analysis sessions

---

## 🎬 Demo – Dashboard Overview

### 📊 Executive Summary

* **Total Candidates:** 45
* **Average Score:** 73.2%
* **Qualified Candidates (≥60%):** 32
* **Average Experience:** 5.3 years

---

## 🚀 Installation Guide

### 📌 Prerequisites

* Python 3.8 or higher
* pip (Python package manager)
* Virtual environment (recommended)

---

### 🧩 Step 1: Clone the Repository

```bash
git clone [https://github.com/KAreebaSherwani/promatch-enterprise-ats.git]
cd promatch-enterprise-ats
```

---

### 🛠️ Step 2: Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ✅ Step 4: Verify Installation

```bash
streamlit --version
python --version
```

---

## ⚡ Quick Start

### ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open at:
**[http://localhost:8501](http://localhost:8501)**

---

## 🔄 Basic Workflow

1. Enter the job description in the sidebar
2. Upload resumes (PDF, DOCX, or TXT)
3. Click **Analyze**
4. Review results in the dashboard
5. Export reports as needed

---

## 🏗️ Architecture Overview

### 📂 Project Structure

```text
promatch-enterprise-ats/
├── app.py              # Main Streamlit application
├── matcher.py          # Resume matching logic
├── utils.py            # Utility functions
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
├── LICENSE             # License file
└── config/             # Skills, synonyms, categories
```

---

## 🧠 Technology Stack

* **Frontend:** Streamlit
* **Backend:** Python 3.8+
* **NLP:** Custom algorithms
* **Charts:** Plotly
* **PDF Processing:** PDFMiner
* **DOCX Processing:** python-docx


 
 
 
 
 
 
 
 
 
