import os
import pandas as pd
from config import VARS_TO_CHANGE
from openpyxl import load_workbook


class Excel_Name:

    def __init__(self, files_dir=""):
        self.files_dir = files_dir
        self.excel_files = os.listdir(self.files_dir)

    def change_name(self, file):
        file_path = os.path.join(self.files_dir, file)
        wb = load_workbook(file_path)

        for sheet in wb.sheetnames:
            ws = wb[sheet]
            df = pd.DataFrame(ws.values)

            for var in VARS_TO_CHANGE:
                print(f"Changing '{var}' to '{VARS_TO_CHANGE[var]}'")
                df.replace(var, VARS_TO_CHANGE[var], inplace=True, regex=True)

            # Write the modified DataFrame back to the sheet
            for row_index, row in enumerate(df.values, start=1):
                for col_index, value in enumerate(row, start=1):
                    ws.cell(row=row_index, column=col_index, value=value)

        output_path = f"excel_name_change/output/{file}"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save workbook with original formatting
        wb.save(output_path)
        print(f"Updated file saved at: {output_path}")

    def change_on_all(self):
        for file in self.excel_files:
            print(f"Processing file: {file}")
            self.change_name(file)


Excel_Name(files_dir="excel_name_change/excel_files/").change_on_all()
