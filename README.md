# 🏛️ Harbor Service Recovery: DevOps & Backend Challenge

[![Harbor Framework](https://img.shields.io/badge/Framework-Harbor%202.0-blue)](https://harborframework.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.12](https://img.shields.io/badge/Python-3.12-green)](https://www.python.org/downloads/release/python-3120/)

A sophisticated **Hard** task designed for the [Terminal Bench 2.0](https://harborframework.com/) framework. This project evaluates an AI agent's ability to diagnose and repair complex architectural flaws in a modern FastAPI microservice architecture.

---

## 🎯 Task Objective
**The Rescue Mission**: A mission-critical microservice is failing to deploy due to a cascading "circular dependency" failure and missing runtime environment context. The agent must:
1.  **Refactor** code to break a **4-way recursive import chain**.
2.  **Discover** hidden environment requirements for the production tier.
3.  **Harden** the infrastructure to allow functional health checks and status reporting.

---

## 🏗️ Technical Architecture & "Hard" Challenge logic
This task is engineered to challenge high-LLM agents (e.g., *Terminus-2*, *Kimi K2*).

### Cascading Circular Dependency (The Core Bug)
The service initializes a recursive crash through the following modules:
1.  `app.main` (App Config) ➔ Imports `app.routes`
2.  `app.routes` (API Handlers) ➔ Imports `app.database`
3.  `app.database` (DB Logic) ➔ Imports `app.main` (Metadata)

### Environment Hardening
The test suite requires `/status` to return `connected`.
*   **The Trap**: The service defaults to `inactive` unless `APP_ENV=production` is present.
*   **Environment variable**: Requirement of `DB_URL_PROD`.

---

### 🧪 Automated Tests
Execute the comprehensive test suite to ensure architectural integrity:

```bash
pytest tests/test_outputs.py
```

---

### 🛠️ 2. Environment Setup
Create a virtual environment and install the verified dependency stack:

```bash
cd fixed_service_recovery
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

pip install -r environment/app/requirements.txt
```

### 🚀 3. Running the Service
The service requires the `DB_URL_PROD` environment variable to reflect its connection status.

```bash
# Set environment variable
export DB_URL_PROD="postgresql://user:pass@localhost:5432/task_db"
export APP_ENV="production"

# Start the application
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 🐳 4. Rebuild and run Docker
From the project root:

```bash
docker build -t fixed_service_recovery -f fixed_service_recovery/environment/Dockerfile fixed_service_recovery/environment/
```

Then run the container:

```bash
docker run -it fixed_service_recovery bash
```

Inside the container:

```bash
bash solution/solve.sh
```

---

## 📊 Performance Benchmarks
| Agent | Model | Success Rate (Mean) |
| :--- | :--- | :--- |
| **Oracle** | Bash (Golden Solution) | ✅ **1.000** |
| **Terminus-2** | Kimi-K2-Instruct-0905 | 🛠️ **0.2** (First Trial) |

---

### **Harbor CLI Benchmarking**
```bash
$env:GROQ_API_KEY = "[GROQ_API_KEY]"; 
harbor run -p "./fixed_service_recovery" -a terminus-2 --model groq/moonshotai/kimi-k2-instruct-0905 -k 5 -n 1
```

---

**Developer**: Antigravity (Powered by Advanced Agentic Coding)