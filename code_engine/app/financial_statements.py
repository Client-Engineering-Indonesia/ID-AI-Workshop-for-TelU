import yfinance as yf

def get_financial_statements(ticker: str, statement_type: str = "income", annual: bool = True):
    """
    Get quarterly or annual financial statements.
    statement_type: "income", "balance", "cashflow"
    annual: True = annual, False = quarterly
    """
    stock = yf.Ticker(ticker)
    
    if statement_type == "income":
        data = stock.financials if annual else stock.quarterly_financials
    elif statement_type == "balance":
        data = stock.balance_sheet if annual else stock.quarterly_balance_sheet
    elif statement_type == "cashflow":
        data = stock.cashflow if annual else stock.quarterly_cashflow
    else:
        raise ValueError("Invalid statement_type. Choose income, balance, or cashflow.")
    
    return data.to_dict()
