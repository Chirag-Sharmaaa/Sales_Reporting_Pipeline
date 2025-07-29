# Sales Reporting Pipeline 🚀

> 📊 A complete automated sales reporting solution using PostgreSQL, DBT, Power BI, and Apache Airflow.

![Dashboard Screenshot](https://your-screenshot-url-here) <!-- Replace with actual link -->

---

## 🎯 Why This Project Matters

In fast-moving retail or e-commerce environments, teams often rely on **automated, daily reporting systems** to stay on top of:

- 📈 **Sales trends**
- 🚚 **Regional performance**
- 💰 **Profitability insights**
- 📦 **Product-level contributions**

This project simulates that very pipeline, giving you:

- ✅ **Automated data ingestion** from daily CSVs
- ✅ **Transformations using DBT** for maintainable modeling
- ✅ **Interactive dashboards** for business users
- ✅ **Airflow-based orchestration**, just like in real-world data teams

It's not just a demo — it's a **production-grade analytics pipeline** simplified for learning and showcasing!

---

## 🧾 Tech Stack & Workflow

1. **Ingest** fresh CSV data using Python + SQLAlchemy → PostgreSQL  
2. **Transform** data with DBT (models: `orders_summary`, `top_products`, `regional_sales`)  
3. **Visualize** with Power BI dashboard (`Sales_Overview.pbix`)  
4. **Automate** daily ingestion & DBT run using Airflow DAG (`sales_reporting_pipeline`)

---

## 📂 Project Structure  
| Folder / File Path                         | Description                                      |
|-------------------------------------------|--------------------------------------------------|
| `superstore_sales_data.csv`               | Raw sales data used for ingestion               |
| `sales_overview_dashboard/Sales_Overview.pbix` | Final Power BI dashboard                       |
| `CSV_Ingestion/ingestion_code.ipynb`      | CSV to PostgreSQL ingestion using pandas & SQLAlchemy |
| `sales_reporting_dbt/dbt_project.yml`     | DBT project configuration file                  |
| `sales_reporting_dbt/models/top_products.sql` | DBT model: Top selling products               |
| `sales_reporting_dbt/models/regional_sales.sql` | DBT model: Regional monthly sales           |
| `sales_reporting_dbt/models/orders_summary.sql` | DBT model: Order-level summary             |
| `airflow_dags/dags/sales_reporting_dag.py` | Airflow DAG automating ingestion & DBT refresh |
| `airflow_dags/scripts/ingest_csv.py`      | Python script for daily CSV ingestion          |
| `airflow_dags/scripts/run_dbt.bat`        | Batch file to run DBT models automatically     |
| `requirements.txt`                        | Python dependencies (optional)                 |


---

## 📊 Power BI Dashboard Highlights

- KPI Cards: **Total Sales, Total Profit, Total Orders, Avg Order Value**
- **Top Products by Sale** (Clustered Bar Chart)
- **Sales Distribution by Category** (Donut Chart)
- **Monthly Sales vs Orders** (Bar + Line Chart)
- **Regional Profit per Order** (Bar Chart)
- **Regional Monthly Sales** (Line Chart)
- **Dynamic slicers** for *Product Category*, *Sub‑Category*, and *Region*

---

## 🕓 Airflow Automation (via Docker)

- **DAG Name**: `sales_reporting_pipeline`
- Triggers 2 daily tasks:
  1. CSV ingestion to PostgreSQL (`ingest_csv.py`)
  2. DBT model refresh (`run_dbt.bat`)
- Built inside Dockerized Apache Airflow environment
- Scheduled to run at 12:00 AM IST daily
- Validated in the Airflow UI

---

## ⚙️ How to Run Locally

1. Ensure Docker Desktop is running
2. Mount this repo's folders into your Airflow Docker environment:
   - `dags/ → airflow_dags/dags`
   - `scripts/ → airflow_dags/scripts`
3. Trigger the DAG from Airflow UI (`localhost:8080`)
4. Power BI dashboard connects to `Sales_Reporting` PostgreSQL DB for live visuals

---
