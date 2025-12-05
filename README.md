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
