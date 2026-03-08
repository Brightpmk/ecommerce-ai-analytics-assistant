
# AI Analytics Assistant for E-commerce

AI-powered analytics assistant that converts natural language business questions into **safe SQL queries**, executes them on a **PostgreSQL analytics database**, and returns **tables, charts, and concise business insights**.

This project demonstrates how Large Language Models (LLMs) can be integrated into **real analytics workflows** while maintaining **SQL safety guardrails**, **structured data pipelines**, and **clean application architecture**.

---

## Overview

Modern business users often need answers from data but lack SQL expertise.  
This project demonstrates a practical approach to building an **AI-assisted analytics interface** where users can ask business questions in natural language.

The system:

1. Converts natural language questions into SQL using an LLM  
2. Validates SQL queries to prevent destructive operations  
3. Executes queries safely on a PostgreSQL analytics database  
4. Returns results as tables, visualizations, and concise insights

Rather than acting as a simple chatbot, the system behaves like a **mini Business Intelligence application**.

---

## Key Features

### Natural Language Analytics

Users can ask business questions such as:

- What is the monthly revenue trend?
- Which product categories generate the highest revenue?
- What are the most common payment types?
- Which states have the most customers?
- What is the average freight cost per order by month?

The application automatically translates these questions into SQL.

---

### SQL Safety Guardrails

Generated queries are validated before execution to prevent destructive database operations.

Blocked SQL operations include:

- DELETE
- DROP
- UPDATE
- ALTER
- TRUNCATE
- Multiple SQL statements

Only **SELECT queries** are allowed.

Example:

User request:

Write SQL that deletes all rows from orders

Generated safe response:

SELECT 'This operation is not allowed as per the guidelines.' AS message;

This ensures that analytics queries cannot modify or damage the database.

---

### Automatic Data Visualization

The application automatically generates charts when query results match common analytics patterns.

| Pattern | Visualization |
|------|------|
| Time series | Line chart |
| Category + metric | Bar chart |

This allows users to interpret trends immediately without manually building visualizations.

---

### Business Insight Generation

After retrieving query results, the system generates a concise **business insight summary**.

Example insight:

"The monthly revenue trend shows a steady increase through early 2017, followed by strong growth later in the year. This suggests increasing customer demand and potentially successful sales campaigns."

---

## Architecture

![Architecture](docs/architecture_diagram.png)

### System Workflow

1. User asks a question in the Streamlit UI  
2. Prompt Builder constructs a context-aware SQL prompt  
3. LLM generates SQL query  
4. SQL Validator checks query safety  
5. Safe queries execute on PostgreSQL  
6. Query results load into a pandas DataFrame  
7. Chart Builder attempts visualization  
8. Insight Generator summarizes results  
9. Streamlit displays results, charts, and insights

---

## Screenshots

### Application Interface

![Home](docs/screenshots/home.jpg)

### SQL Generation and Query Results

![SQL Results](docs/screenshots/sql_and_results.jpg)

### Revenue Trend Visualization

![Revenue Chart](docs/screenshots/revenue_chart.jpg)

### Business Insight Generation

![Insight](docs/screenshots/business_insight.jpg)

### SQL Safety Guardrails

![SQL Safety](docs/screenshots/sql_safety_guardrails.jpg)

---

## Tech Stack

| Layer | Technology |
|------|-----------|
| Frontend | Streamlit |
| Programming Language | Python |
| Database | PostgreSQL |
| Data Processing | pandas |
| SQL Access | SQLAlchemy |
| Visualization | Plotly |
| LLM Integration | OpenAI API |
| Environment Management | python-dotenv |
| Testing | pytest |

---

## Project Structure

```
ecommerce-ai-analytics-assistant
│
├── app
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── llm.py
│   ├── prompt_builder.py
│   ├── validator.py
│   ├── analytics.py
│   ├── charts.py
│   ├── insights.py
│   └── utils.py
│
├── scripts
│   ├── load_csvs.py
│   ├── inspect_data.py
│   └── check_*.py
│
├── sql
│   ├── create_tables.sql
│   └── sample_queries.sql
│
├── tests
│   └── test_validator.py
│
├── docs
│   ├── architecture_diagram.png
│   └── screenshots
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Dataset

This project uses the **Olist Brazilian E-commerce dataset**, which contains real-world e-commerce transaction data including:

- customers
- orders
- products
- order items
- payments

The dataset enables realistic business analysis scenarios such as revenue trends, customer segmentation, and category performance.

---

## Installation

### Clone the repository

git clone https://github.com/YOUR_USERNAME/ecommerce-ai-analytics-assistant.git  
cd ecommerce-ai-analytics-assistant

### Create virtual environment

python -m venv venv

Activate environment:

Mac/Linux

source venv/bin/activate

Windows

venv\Scripts\activate

### Install dependencies

pip install -r requirements.txt

---

## Configure Environment Variables

Create a `.env` file:

OPENAI_API_KEY=your_api_key  
DB_HOST=localhost  
DB_PORT=5432  
DB_NAME=ai_analytics_ecommerce  
DB_USER=postgres  
DB_PASSWORD=your_password  

---

## Create Database Schema

psql -U postgres -d ai_analytics_ecommerce -f sql/create_tables.sql

---

## Load Dataset

Place dataset CSV files inside:

data/raw/

Then run:

python scripts/load_csvs.py

---

## Run the Application

streamlit run app/main.py

The application will launch in your browser.

---

## Testing

Run automated tests:

pytest

Expected output:

6 passed

Tests currently validate SQL safety rules to ensure destructive queries are blocked.

---

## Example Questions

What is the monthly revenue trend?  
Which product categories generate the highest revenue?  
Which states have the most customers?  
What are the most common payment types?  
What is the average freight cost per order by month?

---

## Future Improvements

Potential future enhancements:

- query caching
- SQL explanation for generated queries
- richer visualization types
- persistent query history
- semantic schema descriptions
- role-based query permissions

---

## Learning Goals

This project demonstrates practical skills in:

- analytics system design
- relational database modeling
- SQL safety validation
- LLM integration in data workflows
- interactive analytics applications

---

## License

MIT License
