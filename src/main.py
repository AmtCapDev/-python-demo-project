import yfinance as yf

# Portfolio tickers
tickers = [
    "ADSK",
    "AEHR",
    "AGYS",
    "ALGM",
    "ALGN",
    "AMT",
    "ARES",
    "AXON",
    "BMI",
    "BURL",
    "CDNS",
    "CMG",
    "CVLT",
    "CWST",
    "DT",
    "DXCM",
    "EL",
    "ELF",
    "ENPH",
    "EXPI",
    "EXPO",
    "GSHD",
    "HEI",
    "IDXX",
    "INTU",
    "ISRG",
    "JYNT",
    "LNTH",
    "LSCC",
    "MANH",
    "MKTX",
    "MPWR",
    "NOVT",
    "NOW",
    "NSSC",
    "NVDA",
    "PANW",
    "PAYC",
    "PCTY",
    "PGNY",
    "SNPS",
    "SPSC",
    "SSTI",
    "STAA",
    "TSLA",
    "TTD",
    "VEEV",
]

# Get EOD adjusted close prices
prices = yf.download(
    tickers,
    start="2023-03-21",
    end=None,  # None = up to today
    interval="1d",  # Daily (EOD)
    group_by="ticker",  # Keeps data organized by ticker
    auto_adjust=True,  # Adjusts for splits & dividends
    progress=False,
)

adj_close = prices.xs("Close", level=1, axis=1)
print(adj_close.head())
