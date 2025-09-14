from fastapi import FastAPI, Query
from app.stock_info import get_stock_information
from app.stock_price import get_stock_price_data
from app.financial_statements import get_financial_statements
from app.wikipedia_search import search_wikipedia
from app.web_search import search_web

app = FastAPI(
    title="Financial Analyst Agent API",
    description="Agentic AI tools for financial research & analysis",
    version="1.0.0"
)

# --- STOCK INFO ---
@app.get("/stock/info")
def stock_info(ticker: str = Query(..., description="Stock ticker symbol, e.g., AAPL")):
    return get_stock_information(ticker)

# --- STOCK PRICE ---
@app.get("/stock/price")
def stock_price(
    ticker: str = Query(..., description="Stock ticker symbol, e.g., AAPL"),
    period: str = Query("6mo", description="Data period: 1d,5d,1mo,6mo,1y,5y,10y,max"),
    interval: str = Query("1d", description="Data interval: 1m,5m,1h,1d,1wk,1mo")
):
    return get_stock_price_data(ticker, period, interval)

#--- FINANCIAL STATEMENTS ---
@app.get("/stock/financials")
def financial_statements(
    ticker: str = Query(..., description="Stock ticker symbol, e.g., AAPL"),
    statement_type: str = Query("income", description="income, balance, cashflow"),
    annual: bool = Query(True, description="True=Annual, False=Quarterly")
):
    return get_financial_statements(ticker, statement_type, annual)

#--- WIKIPEDIA ---
@app.get("/wiki/search")
def wiki_search(query: str, sentences: int = 3):
    return search_wikipedia(query, sentences)

# --- WEB SEARCH ---
@app.get("/web/search")
def web_search(query: str, max_results: int = 5):
    return search_web(query, max_results)
