# 🧪 ETL Tutorial: Extract, Transform, Load

This tutorial explains how to perform an ETL (Extract, Transform, Load) process using Python, Scrapy, Pandas, and SQLite, based on the notebook market research project on Mercado Livre.

---

## 📥 1. Extract (Data Extraction with Scrapy)

The extraction is performed using a Scrapy Spider that accesses Mercado Livre pages and collects notebook data.

### Steps:

1. Navigate to the project directory and activate your virtual environment (if needed).
2. Run the Spider using:

```bash
scrapy crawl notebook -o data/data.jsonl
```

This command creates a file named `data.jsonl` containing raw data in JSON Lines format.

---

## 🧼 2. Transform (Cleaning and Processing with Pandas)

After extraction, the data is cleaned and processed using Pandas.

### What happens:

- Null values are replaced with default values.
- Price values are converted from strings to floats.
- Ratings and review counts are converted to floats/integers.
- Rows with prices outside the R$1000–R$10000 range are filtered out.
- Metadata columns `_source` and `_datetime` are added.

### Command:

```bash
python main.py
```

This script reads `data.jsonl`, applies all transformations, and saves the cleaned data to the `mercadolivre.db` SQLite database.

---

## 💾 3. Load (Storing the Data in SQLite)

In the final step, the cleaned DataFrame is loaded into an SQLite table called `notebook`.

### What happens:

- The `mercadolivre.db` database is created (if it doesn't already exist).
- Data is inserted into the `notebook` table.
- The SQLite connection is closed at the end.

---

## ✅ Final Result

You will get:

- A `data.jsonl` file with raw data.
- A `mercadolivre.db` database with a `notebook` table.
- A ready-to-use base for dashboards or further analysis.

---

## 💡 Tip

After finishing the ETL process, run the dashboard interface with:

```bash
streamlit run app.py
```

This will allow you to visualize KPIs and extracted insights!

---