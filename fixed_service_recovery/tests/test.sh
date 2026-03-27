#!/bin/bash

python3 -m venv /tmp/venv
source /tmp/venv/bin/activate

pip install --upgrade pip
pip install fastapi==0.100.0 uvicorn==0.23.0 pydantic==2.1.0 requests pytest psycopg2-binary

export DB_URL_PROD="postgresql://user:pass@localhost:5432/task_db"

cd /app

nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > log.txt 2>&1 &

for i in {1..20}; do
  if curl -s http://localhost:8000/health | grep "ok"; then
    break
  fi
  sleep 1
done

mkdir -p /logs/verifier

pytest -v /tests/test_outputs.py
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
