import os
import pandas as pd
from glob import glob

# Set folder that script is placed in as current directory
abs = os.path.abspath(__file__)
dir = os.path.dirname(abs)
os.chdir(dir)

# Bulk convert all xlsx sheets to csv and use file name + sheet titles as new file names
for excel_file in glob('*.xlsx'):
    print(excel_file)
    df = pd.read_excel(excel_file, sheet_name=None)
    name = os.path.splitext(excel_file)[0]
    for key in df.keys():
        df[key].to_csv('%s_%s.csv' %(name, key), index=None, header=True)
