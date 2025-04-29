# Nexford-Assignments 
# Highridge Construction Company Payment Slips

## Overview
This project automates the generation of weekly payment slips for Highridge Construction Company workers. The program is implemented in both Python and R.

## Features
- Dynamically creates a list of 400 workers with random salaries.
- Assigns random genders to workers.
- Categorizes workers into employee levels based on salary and gender.
- Implements exception handling (Python version).
- Saves payment slips as a CSV file.

## Requirements
### Python
- Python 3.x
- Required Libraries: `random`, `csv`

### R
- R 4.x+
- Required Library: `dplyr`

## How to Run
### Python
1. Install Python (if not installed).
2. Run the script `highridge_payment.py`:
   ```bash
   python highridge_payment.py
   ```
3. The output will be saved as `payment_slips.csv`.

### R
1. Install R and RStudio (if not installed).
2. Install the `dplyr` package (if not installed):
   ```r
   install.packages("dplyr")
   ```
3. Run the script `highridge_payment.R` in RStudio or from the command line.
4. The output will be saved as `payment_slips.csv`.

## Output
- The generated `payment_slips.csv` file contains:
  - Worker ID
  - Name
  - Gender
  - Salary
  - Employee Level

## Error Handling
- The Python script includes `try-except` blocks to catch potential errors.
- The R script uses `dplyr` for efficient data handling.

## Author
Nnamani Favour
