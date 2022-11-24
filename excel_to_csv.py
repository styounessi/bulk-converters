import pandas as pd
import os
from glob import glob

abs = os.path.abspath(__file__)
dir = os.path.dirname(abs)
os.chdir(dir)

for excel_file in glob('*.xlsx'):
    print(excel_file)
    df = pd.read_excel(excel_file)
    csv_file = os.path.splitext(excel_file)[0] + '.csv'
    df.to_csv(csv_file, index=None, header=True)