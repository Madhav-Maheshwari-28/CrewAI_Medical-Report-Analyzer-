from crew import analyze_report

if __name__ == "__main__":
    # Path to a local PDF file (put a sample in the `samples/` folder)
    pdf_path = "samples/sample_blood_report.pdf"

    print(f"Running Medical Report Analyzer on: {pdf_path}")
    result = analyze_report(pdf_path)

    print("\n🧾 Final Output:")
    print(result)
