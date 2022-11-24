import os
import pandas as pd
from glob import glob

# Set folder that script is placed in as current directory
abs = os.path.abspath(__file__)
dir = os.path.dirname(abs)
os.chdir(dir)

# Bulk convert all xlsx files to csv while keeping original file names
for excel_file in glob('*.xlsx'):
    print(excel_file)
    df = pd.read_excel(excel_file)
    csv_file = os.path.splitext(excel_file)[0] + '.csv'
    df.to_csv(csv_file, index=None, header=True)
