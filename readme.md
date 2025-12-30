🎯 PRO MATCH
Enterprise Resume Matching System



✨ FEATURES

🎯 Intelligent Matching Engine

• Multi-Factor Scoring Algorithm
Analyzes must-have skills (50%), semantic match (25%), nice-to-have skills (15%), and experience (10%)

• Natural Language Processing
Advanced NLP for contextual understanding of resumes and job descriptions

• Synonym Recognition
Automatically detects skill variations (e.g., JS = JavaScript)

• OR Logic Support
Handles alternative requirements such as Tableau OR Power BI




⚡ Rapid Processing

• Batch Upload
Process up to 100 resumes simultaneously

• Real-Time Analysis
2–5 seconds processing time per resume

• Progress Tracking
Live progress indicators with detailed status updates

• Multi-Format Support
Supports PDF, DOCX, and TXT files




📊 Comprehensive Analytics

• Executive Dashboard
Key hiring metrics at a glance

• Visual Charts
Interactive score distributions and category breakdowns

• Detailed Candidate Profiles
Complete analysis with skill gap identification

• Ranking System
Automatic candidate ranking with medal badges for top performers




🔍 Advanced Extraction

• Contact Information
Email addresses, phone numbers, and LinkedIn profiles

• Professional Details
Total experience, skill-specific experience, and job titles

• Education
Automatic degree detection from Associate to PhD

• Certifications
Professional certifications and licenses

• Resume Quality Scoring
Completeness score from 0 to 100 percent




📥 Export Options

• CSV Reports
Structured data for spreadsheet analysis

• JSON Data
Complete nested analysis output

• Summary Reports
Professionally formatted text reports with recommendations




🔒 Security and Privacy

• Local Processing
All data processed on local infrastructure

• No External APIs
Zero data transmission to third parties

• In-Memory Processing
No permanent storage of sensitive information

• Session Isolation
Each analysis runs independently



🎬 Demo – Dashboard Overview

📊 Executive Summary

Total Candidates: 45
Average Score: 73.2%
Qualified Candidates (≥60%): 32
Average Experience: 5.3 years



🚀 Installation Guide

📌 Prerequisites

• Python 3.8 or higher
• pip (Python package manager)
• Virtual environment (recommended)



🧩 Step 1: Clone the Repository

git clone [https://github.com/KAreebaSherwani/promatch-enterprise-ats.git]
cd promatch-enterprise-ats



🛠️ Step 2: Create a Virtual Environment

Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate



📦 Step 3: Install Dependencies

pip install -r requirements.txt



✅ Step 4: Verify Installation

streamlit --version
python --version



⚡ Quick Start

▶️ Run the Application

streamlit run app.py

The application will open in your browser at:
[http://localhost:8501](http://localhost:8501)




🔄 Basic Workflow

1. Enter the job description in the sidebar
2. Upload resumes in PDF, DOCX, or TXT format
3. Click Analyze to process candidates
4. Review results in the dashboard
5. Export reports in the desired format




🏗️ Architecture Overview

📂 Project Structure

promatch-enterprise-ats/
│
├── app.py                Main Streamlit application
├── matcher.py            Resume matching logic
├── utils.py              Utility functions
├── requirements.txt      Python dependencies
├── README.md             Documentation
├── LICENSE               License file
└── config                Skills, synonyms, and categories




🧠 Technology Stack

Frontend: Streamlit
Backend: Python 3.8+
NLP: Custom algorithms
Charts: Plotly
PDF Processing: PDFMiner
DOCX Processing: python-docx



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
