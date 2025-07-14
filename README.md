# Data Pipeline 🚍

This is a simple project to run query metrics for quick data exploration in a **local environment**.\
It simulates an **OLAP-like analytical environment** using **DuckDB** and executes analytical queries via Python scripts — supporting both **pure DuckDB SQL** and **DuckDB combined with Apache Beam** for batch processing.

✅ **Google Cloud Platform (GCP) Ready**: the project structure makes it easy to migrate to GCP if needed.

---

## 📦 Project Structure

```
.
├── db/              # DuckDB database files
├── files/           # Raw CSV input files
├── storage/         # Output files (queries results)
├── utils/           # Utility scripts (saving outputs, helpers)
├── create_database.py
├── run_query.py
├── run_beam.py
├── main_runner.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 🟣 Full Installation (Docker)

### Requirements:

- Docker and Docker Compose

### How to Run:

```bash
docker-compose build
docker-compose up
```

### If stuck or no output appears 

you can manually run the script inside the container:

```bash
docker-compose build
docker-compose up
```

```bash
docker exec -it rj_smtr_container bash
python main_runner.py
```


This will automatically:

- Create the database if it doesn't exist
- Prompt for query selection via CLI
- Run the selected query and save outputs in `/storage/`

---

## 🟡 Simple Installation (Local Python)

### Requirements:

- Python 3.11+
- Pip

### How to Run:

```bash
pip install -r requirements.txt
python main_runner.py
```



This method runs everything locally without Docker, using your system’s Python environment.

---

## ✅ Summary

- Supports analytical queries via DuckDB and Apache Beam
- Easily adaptable for GCP Dataflow if required
- Outputs query results into `/storage/` for easy export*

*still in development

