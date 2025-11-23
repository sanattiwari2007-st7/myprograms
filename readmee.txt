Cleaned Average Temperature Calculator
A robust Python utility designed to process raw temperature data. It filters out unrealistic outlier values (sensor errors) and calculates the average of the remaining valid readings.

📝 Overview
In data science and IoT (Internet of Things) applications, sensors often produce "noise" or erroneous readings. This script acts as a data cleaning layer that ensures averages are calculated based only on physically probable data, specifically within a defined range of -50°C to 50°C.

✨ Features
Data Validation: Automatically discards values lower than -50 or higher than 50.

Precision: Calculates the average rounded to 2 decimal places.

Error Handling: Safely handles scenarios where all data is invalid or the input list is empty, preventing "Division by Zero" errors.

Zero Dependencies: Written in pure Python; no external libraries (like NumPy or Pandas) are required.

🚀 Getting Started
Prerequisites
Python 3.x installed on your machine.

Usage
Copy the function calculate_cleaned_average into your Python project.

Pass a list of integers or floats to the function.


Technical Logic
The function operates in two distinct steps:
Filtering Phase: It iterates through the input list and applies the following logic:Valid: $-50 \leq x \leq 50$Invalid: $x < -50$ or $x > 50$

Calculation Phase: If valid readings exist: $\text{Average} = \frac{\sum(\text{Valid Temps})}{\text{Count}(\text{Valid Temps})}$If no valid readings exist: Returns a descriptive error message string.




