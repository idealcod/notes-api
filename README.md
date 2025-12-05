# Notes API – DevOps Project

## 1. Project Overview
Notes API is a small educational DevOps project demonstrating full development and deployment lifecycle using:
- Git & GitHub
- GitHub Actions CI
- Docker & Docker Compose
- Kubernetes (Minikube)
- Automated tests
- PostgreSQL database

The application is a simple notes service with CRUD operations.

---

## 2. Architecture
The project contains two main services:

### **Backend**
- FastAPI application  
- Provides CRUD API for notes  
- Includes unit tests  
- Uses environment variables  
- Includes `/health` endpoint  

### **Database**
- PostgreSQL 14  
- Runs inside Docker and Kubernetes  
- Persistent storage (volume / PVC)

Optional Kubernetes resources:
- Deployment (2 replicas)
- Service (NodePort)
- Secret for DB credentials
- ConfigMap for environment variables (optional)

---

## 3. How to Run with Docker Compose

### 🚀 Start the entire stack:
```bash
docker-compose up --build



Backend will be available at:

http://localhost:8000/docs


Database volume is created automatically.












4. Kubernetes Deployment
Apply manifests:
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/postgres.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Port-forward to access API:
kubectl port-forward service/notes-api-service 8000:8000


API now available at:

http://localhost:8000





5. API Endpoints
Method	Endpoint	Description
POST	/notes	Create a new note
GET	/notes	List all notes
GET	/notes/{id}	Retrieve a note
PUT	/notes/{id}	Update a note
DELETE	/notes/{id}	Delete a note
GET	/health	Healthcheck endpoint



6. Running Tests
pytest


CI pipeline in GitHub Actions also runs tests automatically.
