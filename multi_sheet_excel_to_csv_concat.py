import os
import pandas as pd
from glob import glob

# Set folder that script is placed in as current directory
abs = os.path.abspath(__file__)
dir = os.path.dirname(abs)
os.chdir(dir)

# Bulk convert all sheets in xlsx files into one concatenated csv
for excel_file in glob('*.xlsx'):
    print(excel_file)
    df = pd.concat(pd.read_excel(excel_file, sheet_name=None))
    csv_file = os.path.splitext(excel_file)[0]
    df.to_csv(f'{csv_file}_combined.csv', index=None, header=True)
