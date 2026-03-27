# Service Recovery Challenge (Hardened)

A FastAPI microservice is failing to initialize correctly due to architectural flaws and missing runtime context. Your goal is to rescue the service.

## Critical Issues:
- **Architecture**: Persistent circular dependency chains in the core modules.
- **Environment**: Missing or incorrect environment variables for the production tier.
- **Infrastructure**: Incorrect internal module resolution.

## Objective:
Restore the service so all functional tests pass. 
- `/health` must return `200 OK`.
- `/status` must report `connected`.
- `/version` must return `2.0.0`.

The service must run on `0.0.0.0:8000`.
You are NOT permitted to modify the test suite. Fix the application code and deployment script instead.
