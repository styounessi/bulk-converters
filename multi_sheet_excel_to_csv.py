import os
import pandas as pd
from glob import glob

# Set folder that script is placed in as current directory
abs = os.path.abspath(__file__)
dir = os.path.dirname(abs)
os.chdir(dir)

# Bulk convert sheets in all xlsx to csv and use sheet names for new files
for excel_file in glob('*.xlsx'):
    print(excel_file)
    df = pd.read_excel(excel_file, sheet_name=None)
    for key in df.keys():
        df[key].to_csv('%s.csv' %key)