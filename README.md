# 🧪 RML-QA-Suite – Registry Validation Simulation

A manual QA project to validate registry records using defined business rules and simulate basic QA activities including test design, execution, and defect tracking.

---

## 🧾 Project Scope

This project simulates quality assurance validation of mock registry data based on simple business rules:

- `holder_id` must start with `"HLD"`
- `balance` must not be negative
- `status` must be one of: `"Active"`, `"Inactive"`, `"Deceased"`
- `name` field must not be empty

---

## 📁 Project Structure

RML-QA-Suite/
├── Sample_Registry_Data.json
├── simulate_rml_input.py
├── TestPlan_RML_QA_Suite.md
├── TestCases_RML_QA_Suite.md
├── DefectLog_RML_QA_Suite.md
├── TestExecutionReport_RML_QA_Suite.md
└── README.md

---

## ⚙️ Technologies Used

- Ubuntu 24.04 LTS
- Python 3.10+
- VS Code / Nano / LibreOffice
- Markdown for documentation

---

## 🎯 Objective

To simulate QA skills using:
- Manual test planning
- Test case design
- Defect logging
- Test execution reporting
- Optional automation support via Python

---

## 📌 Note

This is a **fictional simulation project** for demonstration purposes and does **not reference or replicate any proprietary company systems**.

---

💻 Script Execution Output

When you run the Python script `simulate_rml_input.py`, it reads the `Sample_Registry_Data.json` file and evaluates each registry entry against the defined business rules.

### 🔍 Sample Command

```bash
python3 simulate_rml_input.py

RML Registry Record Validation - QA Simulation Started

[Record 1 - Holder ID: HLD001] ✅ VALID

[Record 2 - Holder ID: HLD002] ❌ INVALID
 - Balance is negative: -150.0
 - Status 'Deceased' requires balance to be 0

[Record 3 - Holder ID: 001XYZ] ❌ INVALID
 - holder_id does not start with 'HLD'
 - Status 'Closed' is not a valid status

[Record 4 - Holder ID: HLD004] ❌ INVALID
 - Name is empty
 - Balance is negative: -20.0

[Record 5 - Holder ID: HLD005] ✅ VALID

-----------------------------------
Total Records Evaluated: 5
Valid Records: 2
Invalid Records: 3

RML Registry Record Validation - QA Simulation Completed

📌 Interpretation:

Each record is validated line-by-line.

Errors are printed clearly to help QA testers understand what failed.

You can match the results above with the test case IDs and defects documented in the suite.

📂 Related Files:

Sample_Registry_Data.json: Source data used for validation

simulate_rml_input.py: The script performing validations

DefectLog_RML_QA_Suite.md: Tracks known issues found from these outputs

<img width="466" height="413" alt="image" src="https://github.com/user-attachments/assets/15eb2144-5f93-412f-aa2e-8fef6e01661c" />



---

👤 Author
Udeshan Moodley
QA Analyst | Manual & Automation | GitHub Portfolio Project
📧 udeshan68@gmail.com
