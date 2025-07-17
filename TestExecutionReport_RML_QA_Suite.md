# 📊 Test Execution Report – RML QA Suite

## Execution Summary
- Total Test Cases: 10
- Test Cases Passed: 6
- Test Cases Failed: 4
- Defects Raised: 4

## Execution Environment
- OS: Ubuntu 24.04 LTS
- Validator: Python 3.10 script (simulate_rml_input.py)
- Manual Review: Based on markdown test cases

## Test Results Summary

| Test Case | Result | Comments                              |
|-----------|--------|---------------------------------------|
| TC01      | ✅ Pass  | Valid holder ID                      |
| TC02      | ❌ Fail  | Invalid holder ID detected           |
| TC03      | ❌ Fail  | Negative balance flagged             |
| TC04      | ✅ Pass  | Valid balance                        |
| TC05      | ❌ Fail  | Invalid status "Retired"             |
| TC06      | ✅ Pass  | Valid status: "Deceased"             |
| TC07      | ❌ Fail  | Name field is empty                  |
| TC08      | ✅ Pass  | Valid full record (Emma Brown)       |
| TC09      | ✅ Pass  | Valid edge case: balance = 0.00      |
| TC10      | ✅ Pass  | Valid decimal balance: 300.75        |

## Notes
Manual testing supported by validation script. All business rules verified. No defects in new records (#4 and #5).
