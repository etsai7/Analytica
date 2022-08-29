import dashboard_secrets as sec
import pandas as pd

# 1. Use pandas to open up an excel sheet for reading
df = pd.read_excel(f'{sec.expenses_default_dir}{sec.expenses_excel[0]}',sheet_name='Expenses')

print(df.to_markdown())