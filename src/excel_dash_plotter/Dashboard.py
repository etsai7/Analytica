import dashboard_secrets as sec
import pandas as pd


class Dashboard:
    def __init__(self, df):
        self.df = df
        self.clean_data()

    def clean_data(self):
        self.df = self.df[["Date", "Type", "Company", "Net"]]  # Filter for specific columns
        self.df = self.df.dropna()  # Remove Nans
        print(self.df.Type.unique())  # Get unique Types
        print(self.df.to_markdown())


# Use pandas to open up an Excel sheet for reading
dataframe = pd.read_excel(f'{sec.expenses_default_dir}{sec.expenses_excel[0]}', sheet_name='Expenses')
dashboard = Dashboard(dataframe)
