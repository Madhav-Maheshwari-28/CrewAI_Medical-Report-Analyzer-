# tools.py
from crewai.tools import tool
import fitz  # PyMuPDF
import re

# Reference ranges for common blood test parameters
REFERENCE_RANGES = {
    "Hemoglobin": (13.8, 17.2),
    "RBC Count": (4.7, 6.1),
    "WBC Count": (4500, 11000),
    "Platelet Count": (150000, 450000),
    "Fasting Glucose": (70, 99),
    "Total Cholesterol": (0, 200),
    "HDL Cholesterol": (40, float('inf')),
    "LDL Cholesterol": (0, 130),
    "ALT (SGPT)": (7, 56),
    "AST (SGOT)": (10, 40),
    "Total Bilirubin": (0.1, 1.2),
    "Creatinine": (0.7, 1.3),
    "Urea": (15, 40),
}

@tool("Extract tables and text from PDF report")
def PDFTableExtractor(pdf_path: str) -> str:
    """Extracts raw text content from a medical PDF using PyMuPDF."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text")
    return text

@tool("Parse lab values and compare with normal ranges")
def get_normal_range(text: str) -> dict:
    """Parses lab test values from text and flags them as Low, Normal, or High."""
    results = {}
    for param, (low, high) in REFERENCE_RANGES.items():
        # Create regex to extract the value for each parameter
        pattern = rf"{re.escape(param)}\s*[:\-]?\s*([\d\.]+)"
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = float(match.group(1))
            if value < low:
                status = "Low"
            elif value > high:
                status = "High"
            else:
                status = "Normal"
            results[param] = {"value": value, "status": status}
    return results
