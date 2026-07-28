# Data Quality Summary – Day 1

## Project
Mutual Fund Analytics – Bluestock Fintech Internship

## Dataset Overview
- Total datasets loaded: 10
- All datasets were loaded successfully using Pandas.
- Dataset structure (shape, data types, and sample records) was verified.

## Data Quality Checks
- No duplicate rows were found across the datasets.
- No missing values were detected in the datasets.
- Date columns are currently stored as `object` datatype and will be converted to `datetime` during preprocessing.

## Fund Master Exploration
- Total Fund Houses: 10
- Categories: Equity, Debt
- Multiple sub-categories identified, including Large Cap, Mid Cap, Small Cap, ELSS, Index, Liquid, and Gilt.
- Risk categories identified: Low, Moderate, Moderately High, High, and Very High.

## AMFI Code Validation
- Successfully validated that all AMFI codes in `fund_master` exist in `nav_history`.

## API Integration
- Successfully fetched live NAV data from the MFAPI service.
- Live NAV data was saved as CSV files for the required scheme codes.

## Observation
The AMFI scheme codes provided in the assignment returned different scheme names from the current MFAPI responses, indicating that the API mapping has changed since the assignment was prepared.

## Conclusion
Day 1 project setup, data ingestion, validation, and API integration were completed successfully. The datasets are ready for further preprocessing and analysis.