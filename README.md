# Resume-Parser-POC

A Proof of Concept (POC) project for parsing resumes and converting extracted information into JSON and CSV formats.

---

## 📌 Project Structure
│── OUTPUTconversion.py # Script to convert JSON output to CSV
│── main_with_json.py # Main parser script (produces JSON output)
│── output.csv # Sample parsed CSV output
│── output.json # Sample parsed JSON output
│── requirements.txt # Python dependencies
│── README.md # Project documentation

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/UtkarshTrivedi2934/Resume-Parser-POC.git
   cd Resume-Parser-POC

   pip install -r requirements.txt

   os.mkdir('Manual-parsing')
   os.mkdir('Auto-parsing')

## Usage
   ```bash
   streamlit run OUTPUTconversion.py
   ```
## Outputs
output.json → Parsed resume data in JSON format.
output.csv → Parsed resume data in CSV format.

## Notes
- Place all resumes in the input folder(Resumes) as required by the script before running.
- Make sure to install all dependencies from requirements.txt.
- Modify paths inside the scripts if needed to point to your local directories.
