# 📋 RML QA Suite – Test Plan

## 1. Project Overview
This project simulates a registry record validation system using manual QA processes. The goal is to test sample registry data for accuracy and compliance with defined business rules.

## 2. Scope
Testing will focus on:
- Holder ID validation
- Name field presence
- Balance checks
- Status value compliance

## 3. Objectives
- Validate that registry records meet required format and business logic
- Identify invalid records
- Document defects clearly
- Demonstrate manual test design and execution

## 4. Test Types
- Functional Testing
- Negative Testing
- Boundary Testing
- Data Validation Testing

## 5. Test Environment
- OS: Ubuntu 24.04 LTS
- Tools: Python 3.10, LibreOffice Calc
- Data: Sample JSON input file

## 6. Deliverables
- Test Plan
- Manual Test Cases (Excel)
- Defect Log (Excel)
- Test Execution Report
- Optional Python validator script

## 7. Risks
- False negatives if business logic is misunderstood
- Small data set might not represent all edge cases

## 8. Entry & Exit Criteria

**Entry Criteria:**
- Sample registry data is available
- Test cases reviewed and approved

**Exit Criteria:**
- All planned tests executed
- All defects logged and analyzed

## 9. Roles & Responsibilities
- QA Analyst: Test planning, case design, defect logging, reporting

## 10. Tools
- Ubuntu Terminal
- Python 3 for optional validation
- LibreOffice for test case and defect management
