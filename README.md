# Sales Reporting Pipeline 🚀

> 📊 A complete automated sales reporting solution using PostgreSQL, DBT, Power BI, and Apache Airflow.

![Dashboard Screenshot](https://your-screenshot-url-here) <!-- Replace with actual link -->

---

## 🧾 Tech Stack & Workflow

1. **Ingest** fresh CSV data using Python + SQLAlchemy → PostgreSQL  
2. **Transform** data with DBT (models: `orders_summary`, `top_products`, `regional_sales`)  
3. **Visualize** with Power BI dashboard (`Sales_Overview.pbix`)  
4. **Automate** daily ingestion & DBT run using Airflow DAG (`sales_reporting_pipeline`)

---

## 📂 Project Structure  
Sales_Reporting_Pipeline/
├── superstore_sales_data.csv
├── sales_overview_dashboard/
│ └── Sales_Overview.pbix
├── CSV_Ingestion/
│ └── ingestion_code.ipynb
├── sales_reporting_dbt/
│ ├── dbt_project.yml
│ └── models/
│ ├── top_products.sql
│ ├── regional_sales.sql
│ └── orders_summary.sql
├── airflow_dags/
│ ├── dags/
│ │ └── sales_reporting_dag.py
│ └── scripts/
│ ├── ingest_csv.py
│ └── run_dbt.bat
├── requirements.txt
└── README.md  


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

## ✍️ Author

**Chirag Sharma**  
_Data Engineering Intern • SQL • Python • DBT • Airflow • Power BI_  
🔗 [GitHub Profile](https://github.com/Chirag-Sharmaaa)

---

## 📎 Notes

- `logs/` and `.ipynb_checkpoints/` folders were excluded to keep the repo clean.
- Use `requirements.txt` to set up any missing Python dependencies locally.

---

