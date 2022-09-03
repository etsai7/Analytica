import logging

log = logging.getLogger('log')
class Dashboard:
    def __init__(self, df, log_enabled):
        self.df = df
        self.log_enabled = log_enabled
        self.categories = []
        self.monthly_spend_df = None
        self.logger = logging.getLogger(__name__)

    def graph_monthly_aggs(self, monthly_aggs):
        pass



