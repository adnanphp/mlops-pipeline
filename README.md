# 🚀 Production MLOps Pipeline

[![CI](https://github.com/adnanphp/mlops-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/adnanphp/mlops-pipeline/actions/workflows/ci.yml)
[![Deploy](https://github.com/adnanphp/mlops-pipeline/actions/workflows/deploy.yml/badge.svg)](https://github.com/adnanphp/mlops-pipeline/actions/workflows/deploy.yml)
[![DVC](https://img.shields.io/badge/DVC-enabled-purple)](https://dvc.org)
[![MLflow](https://img.shields.io/badge/MLflow-enabled-red)](https://mlflow.org)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-testing)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org)
[![Docker](https://img.shields.io/badge/Docker-ready-blue)](https://www.docker.com)
[![License](https://img.shields.io/badge/License-MIT-green)](#-license)

> **An end-to-end MLOps pipeline for reproducible machine learning, experiment tracking, automated testing, CI/CD, deployment, and monitoring.**

---

## 📋 Overview

This project demonstrates how to move a machine learning model beyond a local training script into a **reproducible and automated ML lifecycle**.

The pipeline integrates:

* 🧪 **MLflow** — experiment tracking and model management
* 📦 **DVC** — data and pipeline versioning
* 🐳 **Docker** — reproducible application environments
* ⚙️ **Makefile** — standardized development commands
* 🧪 **Automated testing** — unit/integration tests
* 🔄 **GitHub Actions** — CI/CD automation
* 🚀 **Automated deployment** — deployment workflow
* 📊 **Monitoring workflow** — automated monitoring
* 🐍 **Python** — model training and inference

The goal is to demonstrate the complete workflow from **data and model development to automated deployment and monitoring**.

---

## 🏗️ MLOps Architecture

```text
                         ┌──────────────────┐
                         │   Source Code    │
                         │      Git         │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │       DVC        │
                         │ Data / Pipeline  │
                         │    Versioning    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Model Training │
                         │    src/train.py  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     MLflow       │
                         │ Experiments /    │
                         │ Models / Metrics │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Model Artifact │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   src/predict.py │
                         │    Inference     │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │      Docker      │
                         │   Containerized  │
                         │    Application   │
                         └────────┬─────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │       GitHub Actions      │
                    │                            │
                    │  CI → Test → Build →      │
                    │  Deploy → Monitor         │
                    └────────────────────────────┘
```

---

## 🔄 End-to-End Workflow

```text
        DATA
         │
         ▼
   DVC Versioning
         │
         ▼
   Model Training
         │
         ▼
     MLflow
  Experiment Tracking
         │
         ▼
     Model Artifact
         │
         ▼
      Testing
         │
         ▼
      Docker
         │
         ▼
    CI/CD Pipeline
         │
    ┌────┴─────┐
    ▼          ▼
 Deploy     Monitor
```

---

## 🎯 Key Features

### 🧪 Reproducible Experiments

MLflow is used to track machine learning experiments, including model runs, parameters, metrics, and artifacts.

```text
Training Run
     │
     ├── Parameters
     ├── Metrics
     ├── Model
     └── Artifacts
            │
            ▼
         MLflow
```

---

### 📦 Data & Pipeline Versioning

**DVC (Data Version Control)** is integrated into the project to support reproducible data and ML workflows.

The repository includes:

```text
.dvc/
└── config
```

This separates large data artifacts from Git source-code versioning while allowing experiments and datasets to be tracked systematically.

---

### 🔄 Continuous Integration

GitHub Actions automatically runs the CI workflow.

```text
Git Push
   │
   ▼
GitHub Actions
   │
   ▼
Install Dependencies
   │
   ▼
Run Tests
   │
   ▼
Coverage
   │
   ▼
Build Validation
```

CI workflow:

```text
.github/workflows/ci.yml
```

---

### 🚀 Continuous Deployment

The project includes an automated deployment workflow:

```text
.github/workflows/deploy.yml
```

The deployment pipeline allows changes to move from the repository toward the deployment environment through an automated workflow.

---

### 📊 Automated Monitoring

A dedicated GitHub Actions workflow is included for monitoring:

```text
.github/workflows/monitor.yml
```

This provides a foundation for integrating automated ML monitoring into the deployment lifecycle.

---

## 🧠 Training & Inference

### Model Training

The main training implementation is:

```text
src/train.py
```

Run training through the project tooling:

```bash
make train
```

Or directly:

```bash
python src/train.py
```

---

### Model Prediction

Inference is implemented in:

```text
src/predict.py
```

Run prediction with:

```bash
make predict
```

Or directly:

```bash
python src/predict.py
```

---

## 🧪 Testing

The repository contains a dedicated test suite:

```text
tests/
```

The project currently reports:

**100% test coverage**

Run tests with:

```bash
make test
```

Or:

```bash
pytest
```

Run coverage:

```bash
pytest --cov
```

---

## 🐳 Docker

The project includes a `Dockerfile` for reproducible containerized execution.

Build the image:

```bash
docker build -t mlops-pipeline .
```

Run the container:

```bash
docker run --rm mlops-pipeline
```

Docker Compose is also included:

```bash
docker-compose up -d
```

Stop the services:

```bash
docker-compose down
```

---

## ⚙️ Makefile

Common project operations are centralized through the `Makefile`.

Example workflow:

```bash
make train
make predict
make test
```

This provides a consistent interface for running development and ML pipeline tasks.

---

## 🤖 GitHub Actions

The project contains four automated workflows:

```text
.github/
└── workflows/
    ├── ci.yml
    ├── deploy.yml
    ├── dvc.yml
    └── monitor.yml
```

| Workflow      | Purpose                            |
| ------------- | ---------------------------------- |
| `ci.yml`      | Continuous integration and testing |
| `deploy.yml`  | Automated deployment               |
| `dvc.yml`     | DVC-related pipeline automation    |
| `monitor.yml` | Monitoring workflow                |

---

## 📊 MLflow

MLflow provides experiment tracking and model lifecycle functionality.

The repository contains:

```text
mlflow.db
```

The MLflow workflow can be used to organize:

* Experiment runs
* Parameters
* Metrics
* Model artifacts
* Model versions

Example conceptual workflow:

```text
Experiment
    │
    ├── Run 1
    │    ├── Parameters
    │    ├── Metrics
    │    └── Model
    │
    ├── Run 2
    │    ├── Parameters
    │    ├── Metrics
    │    └── Model
    │
    └── Run N
```

---

## 📁 Project Structure

```text
mlops-pipeline/
│
├── .dvc/
│   └── config
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── deploy.yml
│       ├── dvc.yml
│       └── monitor.yml
│
├── screenshort/
│   └── Screenshot_2026-07-07_16-21-52.png
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── tests/
│   └── # Automated tests
│
├── Dockerfile
├── Makefile
├── docker-compose.yml
├── mlflow.db
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technology Stack

| Technology         | Purpose                                  |
| ------------------ | ---------------------------------------- |
| **Python 3.10**    | ML development                           |
| **MLflow**         | Experiment tracking and model management |
| **DVC**            | Data and pipeline versioning             |
| **Docker**         | Containerization                         |
| **Docker Compose** | Multi-service local environment          |
| **GitHub Actions** | CI/CD automation                         |
| **pytest**         | Automated testing                        |
| **Make**           | Development automation                   |
| **Git/GitHub**     | Source control                           |

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/adnanphp/mlops-pipeline.git
cd mlops-pipeline
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Tests

```bash
pytest
```

### 4. Train the Model

```bash
python src/train.py
```

### 5. Run Prediction

```bash
python src/predict.py
```

### 6. Run with Docker

```bash
docker build -t mlops-pipeline .
docker run --rm mlops-pipeline
```

---

## 🔍 Reproducibility

A central goal of this project is to make ML development more reproducible.

```text
Git
 │
 ├── Source Code
 │
 ▼
DVC
 │
 ├── Data
 └── Pipeline
 │
 ▼
MLflow
 │
 ├── Experiments
 ├── Metrics
 └── Models
 │
 ▼
Docker
 │
 └── Reproducible Environment
 │
 ▼
GitHub Actions
 │
 ├── Test
 ├── Build
 ├── Deploy
 └── Monitor
```

---

## 🎓 What This Project Demonstrates

This project provides hands-on experience with:

* 🧠 Machine learning model development
* 📦 Data version control
* 🧪 Experiment tracking
* 📊 Model lifecycle management
* 🐳 Containerization
* 🔄 Continuous integration
* 🚀 Continuous deployment
* 📈 ML monitoring workflows
* 🧪 Automated testing
* 📏 Test coverage
* ⚙️ Development automation
* 🔁 Reproducible ML pipelines

---

## 💼 Why This Project Matters

A typical ML project often ends after model training.

This project focuses on the **engineering lifecycle around the model**:

```text
Train
  ↓
Track
  ↓
Version
  ↓
Test
  ↓
Package
  ↓
Deploy
  ↓
Monitor
  ↓
Improve
```

This demonstrates how machine learning can be integrated into a repeatable software engineering and deployment workflow.

---

## 🔮 Future Improvements

Potential extensions include:

* [ ] Add model/data drift detection
* [ ] Add Prometheus metrics
* [ ] Add Grafana dashboards
* [ ] Add automated model retraining
* [ ] Add model registry workflow
* [ ] Add API-based model serving
* [ ] Add feature/data validation
* [ ] Add security scanning to CI
* [ ] Add Docker image publishing
* [ ] Add Kubernetes deployment
* [ ] Add automated rollback
* [ ] Add production monitoring alerts

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Adnan**

🔗 GitHub: [github.com/adnanphp](https://github.com/adnanphp)

---

## ⭐ Project Purpose

This project was built to demonstrate a complete **MLOps lifecycle**, from reproducible model development and experiment tracking to automated testing, containerization, deployment, and monitoring.

> **Build reproducibly. Track experiments. Automate deployment. Monitor continuously.**
