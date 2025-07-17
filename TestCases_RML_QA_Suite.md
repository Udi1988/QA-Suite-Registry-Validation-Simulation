# ✅ Test Cases – RML QA Suite

| TC_ID | Test Scenario                          | Input Example         | Expected Result                          | Test Type   |
|-------|----------------------------------------|------------------------|-------------------------------------------|-------------|
| TC01  | Validate holder ID starts with "HLD"   | "HLD123456"           | Record accepted                           | Functional  |
| TC02  | Invalid holder ID format               | "XYZ987654"           | Error: Invalid holder ID prefix           | Negative    |
| TC03  | Balance must not be negative           | -250.00               | Error: Negative balance not allowed       | Boundary    |
| TC04  | Valid balance                          | 1500.00               | Record accepted                           | Functional  |
| TC05  | Status must be in allowed list         | "Retired"             | Error: Invalid status                     | Negative    |
| TC06  | Status = "Deceased"                    | "Deceased"            | Record accepted                           | Functional  |
| TC07  | Name must not be empty                 | ""                    | Error: Name field is empty                | Negative    |
| TC08  | All fields valid                       | Valid record          | Record accepted                           | Functional  |
| TC09  | Edge case: balance = 0.00              | 0.00                  | Record accepted                           | Boundary    |
| TC10  | Valid record with decimal balance      | 300.75                | Record accepted                           | Functional  |
