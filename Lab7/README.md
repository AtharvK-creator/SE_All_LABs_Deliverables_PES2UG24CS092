# Lab 7 - Airline Baggage Fees (Fuzz Testing)

## Objective

This lab uses Python and Hypothesis to fuzz-test three airline baggage functions:

- `parse_booking(code)`: reads an airline code, flight number and seat identifier.
- `total_weight(weights_csv)`: calculates the total of comma-separated baggage weights.
- `tag_label(name)`: creates a baggage label from a passenger's first and second name.

The fuzz tests generate arbitrary strings and None values. Invalid inputs are rejected with ValueError; unexpected exceptions cause the tests to fail. Property-based tests also generate valid inputs and check the expected results.

## Files

| File | Description |
|---|---|
| airline_baggage.py | Implementation of the three functions and interactive program |
| test_airline_baggage.py | Hypothesis fuzz tests, valid-input property tests and invalid-input tests |
| README.md | Project description and run instructions |

## Setup

Run these commands from the lab7 folder:

```powershell
python --version
python -m pip install --upgrade pip
python -m pip install pytest hypothesis