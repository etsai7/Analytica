# Dashboard
This project uses the `dash` [library](https://plotly.com/dash/) which is built on top of `plotly`. 
This script will retrieve data from an excel sheet to plot on an interactive dashboard built with dash.

## Resources
- [Dash Guide](https://dash.plotly.com/installation) - setup and tutorials
- [Read Excel with Python Pandas](https://pythonbasics.org/read-excel/)

## Packages
- [`dash`](https://plotly.com/dash/) - for interactive graphs
- [`pandas`](https://pandas.pydata.org/) - for data processing
- [`openpyxl`](https://openpyxl.readthedocs.io/en/stable/) - needed for reading excel sheets
- [`tabuleate`](https://github.com/astanin/python-tabulate) - needed for printing the data frame with markdown

## Setup
1. Install the above packages with either `pip install <package>` or in PyCharm select `Files -> Settings -> Project -> Python Interpreter` to add the packages
   2. Create a `dashboard_secrets.py` file in the same folder as `Dashboard.py` and create the following values
      ```python
      expenses_default_dir = 'C:/Users/<directory>'
      expenses_excel = ['2022 Expenses.xlsx', '<excel file name>']
      ```
      

## Learning Resources
- Using `.agg()` [Stack Overflow](https://stackoverflow.com/questions/51849186/when-using-pandas-groupby-why-use-agg-versus-directly-using-the-function-eg)
