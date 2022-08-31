import dashboard_secrets as sec
import pandas as pd
import calendar
import logging
import LoggerFormatter


class Dashboard:
    def __init__(self, df, log_enabled):
        self.df = df
        self.log_enabled = log_enabled
        self.categories = []
        self.monthly_spend_df = None
        self.logger = logging.getLogger(__name__)

        self.configure_logger()
        self.clean_data()

    def configure_logger(self):
        self.logger.setLevel(logging.DEBUG)
        format = '%(asctime)s | %(levelname)8s | %(message)s'
        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(LoggerFormatter.LoggerFormatter(format))
        if self.log_enabled:
            self.logger.addHandler(stdout_handler)

    def clean_data(self):
        self.df = self.df[["Date", "Type", "Company", "Net"]]  # Filter for specific columns
        self.df = self.df.dropna()  # Remove Nans
        if self.log_enabled:
            self.logger.info(self.df.Type.unique())  # Get unique Types
            self.logger.info("\n"+str(self.df.to_markdown()) + "\n")

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
        self.logger.info("\n" + str(self.monthly_spend_df.to_markdown(index=True)) + "\n")

    def rename_column_headers(self, df, headers):
        return df.rename(columns=headers)
    def print_specific_month(self):
        monthly_df = self.df.apply(lambda row: row[self.df['Date'].dt.month == 4])
        monthly_df['Net'] = monthly_df['Net'].map('${:,.2f}'.format)
        # print(monthly_df.to_markdown())


# Use pandas to open up an Excel sheet for reading
dataframe = pd.read_excel(f'{sec.expenses_default_dir}{sec.expenses_excel[0]}', sheet_name='Expenses')
dashboard = Dashboard(dataframe, log_enabled=False)

dashboard.aggregate_monthly_spend()
dashboard.print_specific_month()
