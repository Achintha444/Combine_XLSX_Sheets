# Excel Sheet Combination Script

This Python script is designed to combine data from two Excel (XLSX) sheets, giving priority to one sheet while ensuring that rows starting with a '#' character are retained. 
It also removes duplicate rows based on the 'Key' column.

## Purpose

The purpose of this script is to merge data from two XLSX sheets while maintaining the following conditions:

- Priority is given to one sheet (in this case, "English").
- Rows starting with '#' from both sheets are retained.
- Duplicate rows are removed based on the 'Key' column.
- An empty row is added above rows starting with '#' for clarity.

## Prerequisites

Before using this script, ensure that you have the following installed:

- Python (https://www.python.org/)
- pandas library (https://pandas.pydata.org/)
- openpyxl library (https://openpyxl.readthedocs.io/)

You can install the required libraries using pip:

```bash
pip install pandas openpyxl
```
or 

```bash
pip3 install pandas openpyxl
```

## Usage

1. Place your two XLSX sheets in the same directory as this script.
   - The first sheet should contain columns "Key" and "Value" (e.g., "English.xlsx").
   - The second sheet should contain columns "Key" and "Chinese" (e.g., "Chinese.xlsx").

2. Update the file names in the script to match your sheet names:
   ```python
   # Load the first XLSX sheet with columns [Key, Value]
   df1 = pd.read_excel("English.xlsx")

   # Load the second XLSX sheet with columns [Key, Chinese]
   df2 = pd.read_excel("Chinese.xlsx")
   ```

3. Run the script:
   ```bash
   python combine_excel_sheets.py
   ```

4. The script will generate a combined XLSX sheet named "combined_sheet.xlsx" in the same directory, containing the merged data.
