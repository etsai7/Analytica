import data_processor as dp
import dashboard_secrets as sec
import pandas as pd
from src.excel_dash_plotter.tools import logger
from dash import Dash, html, dcc
import plotly.express as px

logger.create_logger()
monthly_aggs = {}
for report in sec.expenses_excel:
    dataframe = pd.read_excel(f'{sec.expenses_default_dir}{report}', sheet_name='Expenses')
    dataframe_clean = dp.remove_nan_entries(log_enabled=False, df=dataframe, )
    monthly_aggs[report] = dp.aggregate_monthly_spend(df=dataframe_clean, year=report)

print(monthly_aggs)

# app = Dash(__name__)
#
# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
#
# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),
#
#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),
#
#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)