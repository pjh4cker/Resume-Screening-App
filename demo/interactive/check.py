import os

OUT_PATH = "C:/Users/jaypr/Desktop/Resume Screening App/Resume-Screening-RAG-Pipeline-main/data/supplementary-data/pdf-resumes.csv"
# Check if the file path exists
if os.path.exists(OUT_PATH):
    print("✅ The path is valid.")
else:
    print("❌ The path does NOT exist.")