#!/bin/bash
# 1. SETUP ENVIRONMENT
python3 -m venv /tmp/venv
source /tmp/venv/bin/activate
pip install fastapi==0.100.0 uvicorn==0.23.0 requests pytest pydantic==2.1.0

cd /app

# 2. FIX ARCHITECTURE: Solve Triple Circular Dependency
# Create a centralized metadata file to break main -> routes -> database -> main
echo 'APP_VERSION = "2.0.0"' > app/constants.py

# Replace the circular import in database.py
sed -i 's/from app.main import APP_VERSION/from app.constants import APP_VERSION/' app/database.py

# 3. SET RUNTIME CONTEXT
# Hidden requirement: APP_ENV=production
export DB_URL_PROD="postgresql://user:pass@localhost:5432/task_db"
export APP_ENV="production"
export PYTHONPATH=$PYTHONPATH:.

# 4. INITIALIZE SERVICE
# Bind to 0.0.0.0 to allow traffic
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > log.txt 2>&1 &

# 5. HEALTH CHECK
for i in {1..20}; do
  if curl -s http://localhost:8000/health | grep "ok"; then
    echo "Service is UP"
    break
  fi
  sleep 1
done

# 6. VERIFICATION (Mock tests)
pytest /tests/test_outputs.py