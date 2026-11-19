# SE Lab 6 — Code and Branch Coverage Analysis

**Scenario:** Airline Baggage Fees  
**Course activity:** Software Engineering Lab 6  
**Objective:** Measure and improve code (statement) coverage and branch coverage using Python, pytest, and coverage.py.

## Overview

This repository contains the assigned airline baggage application and two separate test suites:

- The code coverage suite exercises the application's statements and functions.
- The branch coverage suite exercises alternative decision outcomes, including validation, membership, route, carry-on, and check-in decisions.

The original application is kept unchanged. Additional tests are stored in separate files so that the two coverage activities can be run and reviewed independently.

## Repository structure

```text
.
├── README.md
├── SE_Lab6_Coverage_Screenshots.pdf
└── lab6/
    ├── airline_baggage.py
    ├── test_airline_baggage.py
    ├── CodeCoverageTest_28_airline_baggage.py
    ├── BranchCoverageTest_28_airline_baggage.py
    ├── code_coverage.png
    ├── branch_coverage.png
    └── README.md
```

## Requirements

- Python 3.x
- pytest
- coverage.py

Install the test dependencies:

```bash
python -m pip install pytest coverage
```

## Run code coverage

Open a terminal in the repository root and enter the `lab6` directory:

```bash
cd lab6
python -m coverage erase
python -m coverage run --source=airline_baggage -m pytest -q CodeCoverageTest_28_airline_baggage.py
python -m coverage report -m
```

The submitted terminal evidence shows **24 tests passed** and **100% statement coverage** for `airline_baggage.py` (37 statements, 0 missed).

Evidence: [Code coverage terminal screenshot](lab6/code_coverage.png)

## Run branch coverage

From the repository root, enter `lab6` (skip the `cd lab6` command if you are already in that directory):

```bash
cd lab6
python -m coverage erase
python -m coverage run --branch --source=airline_baggage -m pytest -q BranchCoverageTest_28_airline_baggage.py
python -m coverage report -m
```

The submitted terminal evidence shows **25 tests passed** and **100% branch coverage** for `airline_baggage.py` (37 statements, 26 branches, 0 partial branches).

Evidence: [Branch coverage terminal screenshot](lab6/branch_coverage.png)

## Test coverage scope

The tests cover the application's three public functions:

- `baggage_fee()`: unknown cabin, negative weight, free allowance, membership allowance, business-cabin membership behavior, domestic/international route rates, large excess baggage, and the international surcharge.
- `carry_on_ok()`: infant item limit, non-infant weight limit, and non-infant item limit.
- `check_in_status()`: baggage-dependent and international cutoffs, and the `open`, `late`, and `closed` outcomes.

## Submission evidence

The two terminal screenshots are combined into a two-page PDF:

[SE Lab 6 coverage screenshots PDF](SE_Lab6_Coverage_Screenshots.pdf)

The repository also contains separate commits for the code coverage test/evidence and the branch coverage test/evidence, as requested by the Lab 6 handout.

## Note

Coverage indicates which statements and decision branches were executed by the tests; it does not by itself prove that the application is free of defects. The percentages stated above are the results shown in the submitted terminal evidence.
