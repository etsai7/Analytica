import dashboard_secrets as sec
import pandas as pd
import calendar
import logging
import LoggerFormatter
import data_processor as dp


class Dashboard:
    def __init__(self, df, log_enabled):
        self.df = df
        self.log_enabled = log_enabled
        self.categories = []
        self.monthly_spend_df = None
        self.logger = logging.getLogger(__name__)


# Use pandas to open up an Excel sheet for reading
# dataframe = pd.read_excel(f'{sec.expenses_default_dir}{sec.expenses_excel[0]}', sheet_name='Expenses')
# dashboard = Dashboard(dataframe, log_enabled=True)
#
# dashboard.aggregate_monthly_spend()
# dashboard.print_specific_month()

dp.configure_logger()
for report in sec.expenses_excel:
    dataframe = pd.read_excel(f'{sec.expenses_default_dir}{report}', sheet_name='Expenses')
    dataframe_clean = dp.remove_nan_entries(log_enabled=False, df=dataframe, )
    monthly_agg = dp.aggregate_monthly_spend(df=dataframe_clean, year=report)
