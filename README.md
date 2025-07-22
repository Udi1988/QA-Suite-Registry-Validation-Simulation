# 🧪 RML QA Suite – Registry Validation Simulation

> A manual QA simulation project that replicates a registry validation process inspired by RML systems used in the financial sector.  
> Designed to demonstrate core skills in test planning, case design, defect tracking, and execution reporting.

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

---

## ✅ Key Skills Demonstrated

- Test Plan creation with scope, strategy, and entry/exit criteria
- Functional and boundary test case design (positive and negative scenarios)
- Manual execution and result tracking
- Severity-based defect logging and status updates
- Optional Python script to simulate technical interaction with input data

---

## 📁 Project Highlights

| Component        | Description |
|------------------|-------------|
| Test Plan        | Strategic document defining QA approach |
| Test Cases       | Excel-based validation steps with expected results |
| Defect Log       | Categorized bugs with severity and test traceability |
| Execution Report | Real-time execution summary for decision-making |
| rml_sample.json  | Simulated input data for RML registry fields |
| Python Script    | JSON viewer for optional technical showcase |

---

## 📌 Note

This is a **fictional simulation project** for demonstration purposes and does **not reference or replicate any proprietary company systems**.

---

## 👤 About Me

I'm **Udeshan Moodley**, a QA Analyst with 2+ years of experience, ISTQB certified, and certified in Python-based automation.

📧 Email: udeshan68@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/udeshan-moodley/)  
📂 Other project: [Log Parser in Python](https://github.com/Udi1988/log-parser-project)

