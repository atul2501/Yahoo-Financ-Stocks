```markdown
# 📈 Yahoo Finance US Stocks Scraper

This Python project automatically scrapes the **"Most Active" US stocks** from [Yahoo Finance](https://finance.yahoo.com/), processes the data, and saves it in a clean CSV format for analysis.

> ⚡ Built using `Selenium`, `Pandas`, and `NumPy`.  
> 📊 Ideal for traders, data analysts, and anyone interested in US stock market activity.

---

## 🚀 Features

- ✅ **Headless web automation** using Selenium
- ✅ Extracts: Symbol, Name, Price, Volume, Market Cap, PE Ratio, and more
- ✅ Supports **multi-page scraping**
- ✅ **Data cleaning & transformation** (volume, market cap, %, etc.)
- ✅ Final export to **CSV** for downstream use (dashboards, analysis, ML)

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/yahoo-stock-scraper.git
cd yahoo-stock-scraper
```

### 2. Install dependencies

> Make sure you have Python 3.8+ and Chrome installed.

```bash
pip install selenium pandas numpy
```

> You may optionally use `undetected-chromedriver` if Yahoo blocks normal scraping.

---

## 💡 How It Works

### 1. Launches Chrome browser
Uses Selenium WebDriver to open and maximize the Chrome browser window.

### 2. Navigates to Yahoo Finance
Accesses the homepage and clicks on:
- "Markets" ➝ "Trending Tickers"
- Then selects the **"Most Active"** tab

### 3. Extracts table data
Iterates through all pages and scrapes:
- 📌 **Stock Symbol**
- 💼 **Company Name**
- 💲 **Price**
- 📈 **Change / % Change**
- 🔄 **Volume & Avg Volume**
- 💰 **Market Cap**
- 🔍 **P/E Ratio**
- 📆 **52-Week Change %**

### 4. Cleans data with Pandas
- Removes symbols (`$`, `%`, `M`, `B`, etc.)
- Converts values into numeric format
- Handles missing or unknown data (`NaN`)

### 5. Exports to CSV
Final output is saved as `yahoo_finance_stocks.csv`.

---

## 📂 Output Sample

| Symbol | Name          | Price(USD) | Volume_M | Market_Cap_B | PE_Ratio | 52_WK_Change % |
|--------|---------------|------------|----------|---------------|----------|----------------|
| AAPL   | Apple Inc.    | 174.57     | 45.2     | 2891.5        | 30.4     | 15.6           |
| TSLA   | Tesla, Inc.   | 245.12     | 60.1     | 915.3         | 75.2     | -12.4          |

---

## 📎 File Structure

```text
📁 yahoo-stock-scraper/
├── stocks_scraper.py     # Main scraping + data cleaning script
├── requirements.txt      # Optional: dependencies list
└── yahoo_finance_stocks.csv  # Output file (after run)
```

---

## 👨‍💻 Author

Developed by **@yourusername**  
Follow me on [Twitter](https://x.com/0xDavid_xyz) or [LinkedIn](https://www.linkedin.com/in/atul-yadav-112063294/)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
```

---

Let me know if you want to:
- Include screenshots of the output
- Turn this into a Python package
- Or automate this to run daily/weekly

I can help polish those too.
