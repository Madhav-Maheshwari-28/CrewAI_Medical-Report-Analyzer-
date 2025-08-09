from crewai import Agent, Task, Crew, Process
from tools import PDFTableExtractor
from tools import get_normal_range

from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-5"

# Define Tools
file_reader = PDFTableExtractor

# Agent 1: OCR Parser
ocr_agent = Agent(
    role="OCR Parser",
    goal="Extract text from a PDF blood report file",
    backstory="Expert at reading and extracting information from scanned or digital medical documents.",
    tools=[file_reader],
    verbose=True,
    allow_delegation=True
)

# Agent 2: Health Data Interpreter
interpreter_agent = Agent(
    role="Health Data Interpreter",
    goal="Extract structured medical parameters and flag abnormalities",
    backstory="A medical assistant skilled at identifying values and comparing them to standard ranges.",
    tools=[get_normal_range],
    verbose=True,
    allow_delegation=True 
)


# Agent 3: Summary Generator
summary_agent = Agent(
    role="Summary Generator",
    goal="Generate a user-friendly explanation of medical results",
    backstory="An AI that explains complex medical information in simple, caring language.",
    verbose=True,
    allow_delegation=True
)

# Define Tasks
ocr_task = Task(
    description="Extract text from the PDF file: '{{pdf_path}}'",
    agent=ocr_agent,
    expected_output="Raw text content from the blood report.",
    output_file="ocr_output.txt"
)

interpreter_task = Task(
    description="Analyze this raw text and extract structured medical parameters with normal ranges and status.",
    agent=interpreter_agent,
    context=[ocr_task],
    expected_output="Dictionary of values like {'Hemoglobin': {'value': 11.2, 'status': 'Low'}}"
)

summary_task = Task(
    description="Create a simple explanation from the interpreted values.",
    agent=summary_agent,
    context=[interpreter_task],
    expected_output="A short readable summary for the user."
)

# Define Crew
crew = Crew(
    agents=[ocr_agent, interpreter_agent, summary_agent],
    tasks=[ocr_task, interpreter_task, summary_task],
    process=Process.sequential,
    verbose=True
)

# Run Crew
def analyze_report(pdf_path):
    result = crew.kickoff(inputs={"pdf_path": pdf_path})
    return result

if __name__ == "__main__":
    path = "samples/sample_blood_report.pdf"
    output = analyze_report(path)
    print(output)

