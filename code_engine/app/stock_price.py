import yfinance as yf

def get_stock_price_data(ticker: str, period: str = "6mo", interval: str = "1d"):
    """
    Retrieve historical stock prices for time-series analysis.
    period: "1d", "5d", "1mo", "6mo", "1y", "5y", "10y", "max"
    interval: "1m", "5m", "1d", "1wk", "1mo"
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    
    return hist.reset_index().to_dict(orient="records")
