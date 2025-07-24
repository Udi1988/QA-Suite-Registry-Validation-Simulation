# 🐞 Defect Log – QA Suite-Registry

This log captures the defects identified during manual testing of registry data using defined business validation rules.

| Defect ID | Related Test Case | Summary of Issue                             | Severity | Status | Notes                                     |
|-----------|-------------------|----------------------------------------------|----------|--------|-------------------------------------------|
| D-001     | TC-02             | Holder ID uses an invalid prefix             | Major    | Open   | Record #2: Prefix not matching "HLD" rule |
| D-002     | TC-03             | Negative balance encountered                 | Critical | Open   | Record #2: Balance value is below zero    |
| D-003     | TC-05             | Status value "Retired" not in allowed list   | Major    | Open   | Record #2: Value not among valid statuses |
| D-004     | TC-07             | Name field is missing                        | Minor    | Open   | Record #3: Name is empty or null          |

---

### 📌 Notes:
- All defects were discovered during the first round of test execution using the `Sample_Registry_Data.json` file.
- These issues are pending fix before the final test cycle.
- Status will be updated after re-validation is completed.
