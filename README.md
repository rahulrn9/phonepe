# 📊 PhonePe Data Analysis Project

This project analyzes the transaction trends, insurance growth, and user engagement patterns of PhonePe using data extracted from the [PhonePe Pulse](https://github.com/PhonePe/pulse) repository.

---

## 📁 Project Structure

phonepe/
│
├── data/ # Cleaned CSVs for transactions, insurance, and users
│ ├── transactions_aggregated.csv
│ ├── insurance_aggregated.csv
│ └── users_aggregated.csv
│
├── sql/ # SQL schemas and ETL scripts
│ ├── create_aggregated_transaction.sql
│ ├── create_aggregated_insurance.sql
│ └── etl_load_data.py
│
├── notebooks/ # Jupyter analysis notebook
│ └── phonepe_analysis.ipynb
│
├── streamlit_app/ # Streamlit dashboard app
│ └── app.py
│
├── documentation/ # Final insights report
│ └── PhonePe_Insights_Report.pdf
│
├── presentation/ # Presentation slides
│ └── PhonePe_Analysis_Presentation.pptx

yaml
Copy
Edit

---

## 📌 Key Analyses

- **💰 Transaction Trends**:
  - Peer-to-peer payments are the largest transaction category.
  - Recharge & bill payments show high engagement.

- **🏥 Insurance Growth**:
  - Insurance transaction volume has consistently grown across quarters.
  - Reflects increasing user adoption of embedded financial services.

- **📱 Device Usage Insights**:
  - Xiaomi, Samsung dominate PhonePe user base.
  - Premium brands like Apple and OnePlus show niche user segments.

---

## 🧰 Technologies Used

- Python (Pandas, Seaborn, Matplotlib, Plotly)
- SQL (PostgreSQL Schema)
- Streamlit (for dashboard)
- Jupyter Notebook (for EDA)
- PowerPoint + PDF (for presentation/report)

---

## 🚀 Getting Started

1. Clone the repo:
```bash
git clone https://github.com/rahulrn9/phonepe.git
cd phonepe
Set up PostgreSQL DB and run the schema from sql/ folder.

Load data using:

bash
Copy
Edit
python sql/etl_load_data.py
Explore the notebook:

bash
Copy
Edit
jupyter notebook notebooks/phonepe_analysis.ipynb
Launch the dashboard:

bash
Copy
Edit
cd streamlit_app
streamlit run app.py
