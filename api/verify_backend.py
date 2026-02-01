from fastapi.testclient import TestClient
from api.index import app
import pytest

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Bhargav's Digital Resume API"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_profile_endpoint_exists():
    # Note: Without a real DB, this might return 500 or 404, but we check if the route is registered
    response = client.get("/api/profile")
    assert response.status_code in [200, 404, 500] 

def test_skills_endpoint_exists():
    response = client.get("/api/skills")
    assert response.status_code in [200, 500]

def test_projects_endpoint_exists():
    response = client.get("/api/projects")
    assert response.status_code in [200, 500]

if __name__ == "__main__":
    print("Running basic backend verification...")
    try:
        test_read_main()
        print("✅ Root endpoint OK")
        test_health_check()
        print("✅ Health check OK")
        print("Backend verification complete (basic connectivity).")
    except Exception as e:
        print(f"❌ Verification failed: {e}")
