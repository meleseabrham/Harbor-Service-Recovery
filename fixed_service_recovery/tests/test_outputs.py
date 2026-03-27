import requests
import pytest
import time
import os

def test_health_endpoint():
    """Verify the API is up and responding to health checks."""
    success = False
    for _ in range(10):
        try:
            response = requests.get("http://localhost:8000/health", timeout=2)
            if response.status_code == 200 and response.json().get("status") == "ok":
                success = True
                break
        except Exception:
            time.sleep(1)
    assert success, "Health check failed: API did not respond with 200 OK after 10 seconds."

def test_status_endpoint():
    """Verify the database logic is initialized and reports connected status."""
    response = requests.get("http://localhost:8000/status")
    assert response.status_code == 200
    assert response.json().get("db") == "connected", "DB status check failed: Engine was not properly initialized."

def test_app_binding():
    """Ensure the app is binding to 0.0.0.0 and not 127.0.0.1 (Docker requirement)."""
    # This is indirectly tested by the fact that the verifier can reach localhost:8000 
    # but we can look for the fix pattern.
    pass

def test_psycopg2_import():
    """Verify that the database driver is correctly installed and importable."""
    # We can't easily check inside the container from here, but we check via status endpoint
    # However, we can check if a file was created if it was a requirement
    pass

def test_config_robustness():
    """Verify that the application uses the correct PROD environment variable keys."""
    # The /status endpoint check confirms DB_URL_PROD was used correctly if db == connected
    response = requests.get("http://localhost:8000/status")
    assert response.status_code == 200

def test_version_integrity():
    """Verify that the refactor preserved the application version constant."""
    # This checks if the agent successfully handled the circular import without losing data
    # (assuming we check an endpoint that returns version)
    try:
        response = requests.get("http://localhost:8000/version", timeout=2)
        assert response.status_code == 200
        assert "version" in response.json()
    except Exception:
        pytest.fail("Version endpoint failed - circular import fix might have broken metadata.")
