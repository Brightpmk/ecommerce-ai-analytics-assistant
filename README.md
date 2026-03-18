# AI Analytics Assistant for E-commerce

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-purple)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange)
![License](https://img.shields.io/badge/License-MIT-green)

AI-powered analytics assistant that converts **natural language business questions into SQL queries**, validates them for safety at the application layer, executes them on a **PostgreSQL analytics database**, and returns **tables, charts, and concise business insights**.

The project demonstrates how **Large Language Models (LLMs)** can be integrated into real **data analytics workflows** while maintaining **SQL safety guardrails** and a **clean modular application architecture**.

---

# Project Overview

Modern business teams often need answers from data but **lack SQL expertise**.

This project demonstrates how an **AI analytics interface** can allow users to explore business data using **natural language queries**.

Instead of writing SQL manually, users can ask questions such as:

- What is the monthly revenue trend?
- Which product categories generate the most revenue?
- Which states have the most customers?
- What are the most common payment types?

The system automatically converts these questions into SQL, validates them, executes them, and returns insights.

This project functions as a **mini AI-powered Business Intelligence system**.

---

# Key Features

## Natural Language to SQL

Users can interact with the analytics database using natural language.

Example question:

```
What is the monthly revenue trend?
```

The system automatically generates a valid SQL query to answer the question.

---

## SQL Safety Guardrails

All generated SQL queries pass through a **validation layer** before execution.

Blocked SQL operations include:

- DELETE
- DROP
- UPDATE
- ALTER
- TRUNCATE
- Multiple SQL statements

Only **SELECT-style analytical queries** are allowed.

Unsafe questions are blocked before SQL generation, and unsafe generated SQL is rejected before execution.

This enforces **read-only analytics behavior at the application layer**.

---

## Automatic Data Visualization

The system automatically generates charts when query results match common analytics patterns.

| Query Pattern | Chart Type |
|---------------|-----------|
| Time series | Line chart |
| Category + metric | Bar chart |

---

## Business Insight Generation

After executing a query, the system generates **short natural-language summaries** describing the results.

- Uses LLM when API key is available  
- Falls back to simple rule-based summaries if not  

---

# System Architecture

![Architecture](docs/architecture_diagram.png)

## Workflow

1. User submits a question in the Streamlit interface  
2. Prompt Builder constructs a context-aware SQL prompt  
3. LLM generates a candidate SQL query  
4. SQL Validator checks for safety violations  
5. Safe queries execute on the PostgreSQL database  
6. Results load into a pandas DataFrame  
7. Chart Builder attempts automatic visualization  
8. Insight Generator summarizes the results  
9. Streamlit renders tables, charts, and insights  

---

# Screenshots

## Application Interface

![Home](docs/screenshots/home.png)

---

## SQL Generation and Query Results

![SQL Results](docs/screenshots/sql_and_results.png)

---

## Revenue Trend Visualization

![Revenue Chart](docs/screenshots/revenue_chart.png)

---

## Business Insight Generation

![Insight](docs/screenshots/business_insight.png)

---

## SQL Safety Guardrails

![SQL Safety](docs/screenshots/sql_safety_guardrails.png)

---

# Tech Stack

| Layer | Technology |
|------|-----------|
| Frontend | Streamlit |
| Language | Python |
| Database | PostgreSQL |
| Data Processing | pandas |
| SQL Access | SQLAlchemy + pandas |
| Visualization | Plotly |
| LLM Integration | OpenAI API |
| Environment | python-dotenv |
| Testing | pytest |

---

# Project Structure

```
ecommerce-ai-analytics-assistant
│
├── app
├── scripts
├── sql
├── tests
├── docs
├── data
│   └── raw
│       └── *.csv
├── requirements.txt
└── README.md
```

---

# Dataset

The current implementation uses a **subset of the Olist Brazilian E-commerce dataset**, including:

- customers  
- orders  
- order items  
- order payments  
- products  
- product category translation  

This supports analytics such as:

- revenue trends  
- category performance  
- customer distribution  
- payment behavior  

---

# Installation

```
git clone https://github.com/YOUR_USERNAME/ecommerce-ai-analytics-assistant.git
cd ecommerce-ai-analytics-assistant
```

```
python -m venv venv
```

Mac/Linux
```
source venv/bin/activate
```

Windows
```
venv\Scripts\activate
```

```
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create `.env`

```
OPENAI_API_KEY=your_api_key
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_analytics_ecommerce
DB_USER=postgres
DB_PASSWORD=your_password
```

---

# Create Database Schema

```
psql -U postgres -d ai_analytics_ecommerce -f sql/create_tables.sql
```

---

# Load Dataset

Place CSV files inside:

```
data/raw/
```

Then run:

```
python scripts/load_csvs.py
```

---

# Run the Application

```
python -m streamlit run app/main.py
```

---

# Testing

```
pytest
```

Tests currently focus on SQL validation logic.

---

# Example Questions

- What is the monthly revenue trend?
- Which product categories generate the highest revenue?
- Which states have the most customers?
- What are the most common payment types?
- What is the average freight cost per order by month?

---

# Current Limitations

- Only a subset of the Olist dataset is used  
- SQL safety is enforced at the application layer (not DB-level permissions)  
- CSV loader appends data (may duplicate if rerun without clearing tables)  
- Test coverage is limited to validator logic  
- Chart selection is heuristic-based  

---

# Learning Goals

- LLM + SQL integration  
- Natural language analytics systems  
- SQL validation design  
- Data app architecture  
- Interactive BI-style interfaces  

---

# License

MIT License
