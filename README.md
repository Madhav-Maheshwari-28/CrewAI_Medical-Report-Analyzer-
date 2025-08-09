# Medical Report Analyzer

**AI-powered tool to extract, interpret, and summarize medical PDF reports**

> Convert complex medical PDFs into clear, actionable health insights in seconds.

---

## 🔎 Project Overview

Medical Report Analyzer is an AI-driven pipeline that reads medical PDF reports (scanned or digital), extracts lab values, compares them with reference ranges, and generates a concise, patient-friendly summary. The system is built using multiple cooperating agents orchestrated by CrewAI.

This project was developed during the **IIT Jammu Summer Internship** under the mentorship of **Premveer Sir**.

---

## 🚀 Key Features

* 📄 **OCR extraction** from scanned or digital PDFs (using PyMuPDF)
* 📊 **Parameter interpretation** with comparison to medical reference ranges
* 🗣 **Natural-language summary** explaining flagged results (Low / Normal / High)
* 🤝 **Agent-based pipeline** (OCR Parser, Health Data Interpreter, Summary Generator)

---

## 🛠 Tech Stack

* Python 3.8+
* CrewAI (agent orchestration)
* PyMuPDF (fitz) for PDF text extraction
* OpenAI (GPT-5) for natural-language summarization

---

## 📁 Repository Structure

```
├── crew.py            # Main pipeline that defines agents, tasks and runs the Crew
├── tools.py           # Tool functions: PDFTableExtractor and get_normal_range
├── samples/           # Sample PDF reports
│   └── sample_blood_report.pdf
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

---

## ⚙️ Quick Start

1. Clone the repository:

```bash
git clone <repo-url>
cd medical-report-analyzer
```

2. Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set environment variables (example using a `.env` file):

```
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL_NAME=gpt-5
```

4. Run the analyzer on a sample file:

```bash
python crew.py
# or
python crew.py samples/sample_blood_report.pdf
```

> The main function in `crew.py` runs `analyze_report(path)` and prints the structured result and summary.

---

## 🧩 How it works (brief)

1. **OCR Parser Agent** (uses `PDFTableExtractor`) — extracts raw text from the PDF.
2. **Health Data Interpreter Agent** (uses `get_normal_range`) — parses known lab parameters, compares to reference ranges, and assigns statuses (Low / Normal / High).
3. **Summary Generator Agent** — turns the interpreted results into an easy-to-understand summary for the user.

CrewAI coordinates these agents and passes outputs between them.

---

## ✍️ Customization

* Update `REFERENCE_RANGES` in `tools.py` to change or extend parameter ranges.
* Add more parsing rules or regex patterns in `get_normal_range` to support additional report formats.
* Tweak the agents' backstories/goals in `crew.py` to refine behavior.

---

## ✅ Contribution & Credits

* Developed by **Madhav Maheshwari** during the **IIT Jammu Summer Internship**.
* Special thanks to **Premveer Sir** for mentorship and guidance.

Contributions and improvements are welcome — feel free to open issues or pull requests.

---

## 📄 License

This project is provided under the MIT License — see `LICENSE` for details.

---

## 📬 Contact

For questions or feedback, reach out on GitHub or email: `madhav@example.com` (replace with your contact).
