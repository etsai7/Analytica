import logging
import calendar

log = logging.getLogger('log')


def remove_nan_entries(log_enabled=True, df=None):
    df = df[["Date", "Type", "Company", "Net"]]  # Filter for specific columns
    df = df.dropna()  # Remove Nans
    if log_enabled:
        log.info(df.Type.unique())  # Get unique Types
        log.info("\n" + str(df.to_markdown()) + "\n")
    return df


def aggregate_monthly_spend(df=None, year=''):
    # Remove out non-spend items
    filter_out_pay_df = df.apply(lambda row: row[~df['Type'].isin(['Pay', 'Tax'])])

    # Group by Month and aggregate by sum (can use .agg() or .sum() directly). .agg() allows for more functions
    monthly_spend_df = \
        filter_out_pay_df.groupby(filter_out_pay_df.Date.dt.month).sum().reset_index()
    # self.monthly_spend_df = \
    # filter_out_pay_df.groupby(filter_out_pay_df.Date.dt.month).agg(Spend=('Net', 'sum')).astype({'Spend': float}).reset_index()

    # Formatting
    new_headers = {"Date": "Month", "Net": "Net Spent"}
    monthly_spend_df = rename_column_headers(monthly_spend_df, new_headers)
    monthly_spend_df['Net Spent'] = monthly_spend_df['Net Spent'].map('${:,.2f}'.format)
    monthly_spend_df['Month'] = monthly_spend_df['Month'].apply(lambda x: calendar.month_name[x])
    log.info(year)
    log.debug("\n" + str(monthly_spend_df.to_markdown(index=False)) + "\n")
    return monthly_spend_df


def rename_column_headers(df, headers):
    return df.rename(columns=headers)


def print_specific_month(df, month_num):
    monthly_df = df.apply(lambda row: row[df['Date'].dt.month == month_num])
    monthly_df['Net'] = monthly_df['Net'].map('${:,.2f}'.format)
    print(monthly_df.to_markdown())
