# 🧪 RML QA Suite – Registry Validation Simulation

> A manual QA simulation project that replicates a registry validation process inspired by RML systems used in the financial sector.

---

## 🧾 Project Scope

This project simulates quality assurance validation of mock registry data based on simple business rules:

- `holder_id` must start with `"HLD"`
- `balance` must not be negative
- `status` must be one of: `"Active"`, `"Inactive"`, `"Deceased"`
- `name` field must not be empty

---

RML-QA-Suite/
├── Sample_Registry_Data.json            # Mock RML input data
├── simulate_rml_input.py                # Python validation script
├── TestPlan_RML_QA_Suite.md             # Test plan with scope, approach, criteria
├── TestCases_RML_QA_Suite.md            # Manual test cases (positive/negative/boundary)
├── DefectLog_RML_QA_Suite.md            # Logged defects with severity and status
├── TestExecutionReport_RML_QA_Suite.md  # Summary of test results and defect coverage
└── README.md

---

📂 **Quick Start Guide**

**TestPlan:** Defines objectives, scope, strategy, entry/exit criteria
**TestCases:** Lists detailed manual test scenarios
**Sample_Registry_Data:** Provides input data for validation
**simulate_rml_input.py:** Enforces rules on input data
**DefectLog:** Records issues found during testing
**TestExecutionReport:** Summarizes results and mapping to defects

---

## ⚙️ Technologies Used

- Ubuntu 24.04 LTS
- Python 3.10+
- VS Code / Nano / LibreOffice 
- Markdown for documentation

---

## 🎯 Objective

**To Demonstrate QA skills using:**
- Manual test planning
- Test case design
- Defect logging
- Test execution reporting
- Optional automation support via Python

---

💻 Script Execution Output
Running simulate_rml_input.py validates registry records and outputs:

**✅ Example Output**

RML Registry Record Validation - QA Simulation Started

[Record 1 - Holder ID: HLD001] ✅ VALID  
[Record 2 - Holder ID: HLD002] ❌ INVALID  
 - Balance is negative  
 - Deceased requires zero balance  
[Record 3 - Holder ID: 001XYZ] ❌ INVALID  
 - ID format + Invalid status  
[Record 4 - Holder ID: HLD004] ❌ INVALID  
 - Empty name + Negative balance  
[Record 5 - Holder ID: HLD005] ✅ VALID  

Total Evaluated: 5  
Valid: 2  
Invalid: 3  

RML Registry Record Validation - QA Simulation Completed

---

**📌 Interpretation**
Each record is validated line-by-line
Failures are clearly explained
Matches are traceable to test cases and defect log

---

## ✅ Key Skills Demonstrated

- Test Plan creation with scope, strategy, and entry/exit criteria
- Functional and boundary test case design (positive and negative scenarios)
- Manual execution and result tracking
- Severity-based defect logging and status updates

---

## 📌 Note

This is a **fictional simulation project** for demonstration purposes and does **not reference or replicate any proprietary company systems**.

---

## 👤 About Me

I'm **Udeshan Moodley**, a QA Analyst with 2+ years of experience, ISTQB certified, and certified in Python-based automation.

📧 Email: udeshan68@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/udeshan-moodley/)  
📂 Other project: [Log Parser in Python](https://github.com/Udi1988/log-parser-project)

