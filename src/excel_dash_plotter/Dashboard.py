import dashboard_secrets as sec
import pandas as pd
import calendar


class Dashboard:
    def __init__(self, df):
        self.df = df
        self.clean_data()
        self.categories = []
        self.monthly_spend_df = None

    def clean_data(self):
        self.df = self.df[["Date", "Type", "Company", "Net"]]  # Filter for specific columns
        self.df = self.df.dropna()  # Remove Nans
        print(self.df.Type.unique())  # Get unique Types
        print(self.df.to_markdown())

    def aggregate_monthly_spend(self):
        # Remove out non-spend items
        filter_out_pay_df = self.df.apply(lambda row: row[~self.df['Type'].isin(['Pay', 'Tax'])])

        # Group by Month and aggregate by sum (can use .agg() or .sum() directly). .agg() allows for more functions
        self.monthly_spend_df = \
            filter_out_pay_df.groupby(filter_out_pay_df.Date.dt.month).sum().reset_index()
        # self.monthly_spend_df = \
        # filter_out_pay_df.groupby(filter_out_pay_df.Date.dt.month).agg(Spend=('Net', 'sum')).astype({'Spend': float}).reset_index()

        # Formatting
        new_headers = {"Date": "Month", "Net": "Net Spent"}
        self.monthly_spend_df = self.rename_column_headers(self.monthly_spend_df, new_headers)
        self.monthly_spend_df['Net Spent'] = self.monthly_spend_df['Net Spent'].map('${:,.2f}'.format)
        self.monthly_spend_df['Month'] = self.monthly_spend_df['Month'].apply(lambda x: calendar.month_name[x])
        print(self.monthly_spend_df.to_markdown(index=True))

    def rename_column_headers(self, df, headers):
        return df.rename(columns=headers)
    def print_specific_month(self):
        monthly_df = self.df.apply(lambda row: row[self.df['Date'].dt.month == 3])
        monthly_df['Net'] = monthly_df['Net'].map('${:,.2f}'.format)
        # print(monthly_df.to_markdown())


# Use pandas to open up an Excel sheet for reading
dataframe = pd.read_excel(f'{sec.expenses_default_dir}{sec.expenses_excel[0]}', sheet_name='Expenses')
dashboard = Dashboard(dataframe)

dashboard.aggregate_monthly_spend()
dashboard.print_specific_month()
