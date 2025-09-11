import yfinance as yf

def get_stock_information(ticker: str) -> dict:
    """
    Retrieve company fundamentals, valuation metrics, and current price.
    """
    stock = yf.Ticker(ticker)
    info = stock.info  # metadata from Yahoo
    
    return {
        "company": info.get("longName"),
        "ticker": ticker,
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "profit_margin": info.get("profitMargins"),
        "beta": info.get("beta"),
        "currency": info.get("currency"),
        "current_price": info.get("currentPrice"),
        "description": info.get("longBusinessSummary")
    }
