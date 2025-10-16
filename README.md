# 🌤 Weather Data ELT Pipeline with Airflow, dbt, Postgres & Superset

This project demonstrates a near real-time **ELT data pipeline** that ingests live weather data from an API, loads it into a data warehouse, transforms it with dbt, and visualizes insights in a dashboard.  
It's designed to showcase **modern data engineering skills**: ingestion, transformation, orchestration, and visualization — fully containerized using Docker.

---

## 🧰 Tech Stack

- 🐳 Docker & WSL2  
- 🐘 PostgreSQL (Data Warehouse)  
- 🌬 Apache Airflow (Orchestration)  
- 🪄 dbt (Transformation)  
- 📊 Apache Superset (Visualization)  
- 🐍 Python (API ingestion: `requests`, `psycopg2`)

---

## 🚀 Features

- Pull live weather data from [Weatherstack API](https://weatherstack.com/)
- Store raw data in Postgres
- Transform data with dbt models
- Orchestrate the ELT pipeline with Airflow
- Build a near real-time dashboard with Superset
- Fully containerized with Docker Compose

---

## 🛠 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Tanh36054/weather-data-project.git
cd weather-data-project

### 2. Start services with Docker Compose
docker-compose up -d

### 3. Set up the virtual environment
python3 -m venv .venv
source .venv/bin/activate

### 4. Configure environment variables
Tạo file .env trong thư mục docker/:
WEATHERSTACK_API_KEY=your_api_key_here
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=weather

### 5. Access services
Airflow: http://localhost:8000
Superset: http://localhost:8088
Postgres: localhost:5432 (hoặc port bạn config)

## 🧠 What I Learned
How to build an end-to-end ELT pipeline
How to orchestrate workflows with Airflow
How to containerize modern data stack with Docker
How to write dbt models for transformations
How to visualize data with Superset
How tools communicate together in a real-world data project

## 📌 Future Improvements
Add data quality checks (e.g., with Great Expectations)
Add streaming ingestion or CDC
Deploy pipeline to cloud
CI/CD for dbt models


