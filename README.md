http://13.60.76.70:30007/

🚨 Incident Management System (DevOps Project)

A production-style DevOps project that deploys a Flask-based Incident Management application using modern DevOps tools and cloud infrastructure.

This project demonstrates a complete CI/CD pipeline, containerization, Kubernetes orchestration, and integration with a managed cloud database.

---

📌 Project Overview

The Incident Management System allows teams to create, track, and manage incidents.
The application is containerized using Docker and deployed to a Kubernetes cluster running on an AWS EC2 instance.
All incident data is stored in AWS RDS MySQL, ensuring persistence outside the containers.

---

🏗 Project Architecture

flowchart LR

A[User Browser] --> B[EC2 NodePort Service]
B --> C[Kubernetes Service]
C --> D[Flask Application Pods]

D --> E[AWS RDS MySQL Database]

subgraph AWS EC2 Instance
C
D
end

subgraph AWS RDS
E
end

---

⚙️ CI/CD Pipeline Workflow

flowchart LR

A[Developer Push Code] --> B[GitHub Repository]

B --> C[Jenkins Pipeline]

C --> D[Build Docker Image]

D --> E[Push Image to DockerHub]

E --> F[EC2 Kubernetes Cluster]

F --> G[Pull Latest Image]

G --> H[Deploy to Kubernetes]

H --> I[Flask Application Pods]

I --> J[AWS RDS Database]

---

🧰 Technology Stack

Layer| Technology
Backend| Flask (Python)
Web Server| Gunicorn
Containerization| Docker
CI/CD| Jenkins
Container Registry| DockerHub
Orchestration| Kubernetes (K3s)
Cloud Platform| AWS EC2
Database| AWS RDS MySQL
Reverse Proxy| Nginx

---

📂 Project Structure

incidentmanagement/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── db-init
│   └── init.sql
│
├── k8s
│   ├── deployment.yaml
│   └── service.yaml
│
├── nginx
│   └── default.conf
│
└── Jenkinsfile

---

🐳 Docker Workflow

flowchart TD

A[Source Code] --> B[Docker Build]
B --> C[Docker Image]
C --> D[Push to DockerHub]
D --> E[Kubernetes Pull Image]
E --> F[Run Container Pods]

---

☸ Kubernetes Deployment

The application is deployed using Kubernetes Deployment and Service resources.

Deployment

File:

k8s/deployment.yaml

Creates:

2 Flask application pods

Each pod runs the Docker image from DockerHub.

---

Service

File:

k8s/service.yaml

Service type:

NodePort

Port configuration:

App Port: 8000
NodePort: 30007

Access the application:

http://EC2_PUBLIC_IP:30007

---

🗄 Database Architecture

The application connects to AWS RDS MySQL instead of a local database.

flowchart LR

A[Flask App Pods] --> B[AWS RDS Endpoint]
B --> C[MySQL Database]
C --> D[incidents_p Table]

Database initialization is handled using an SQL script.

Example schema:

CREATE DATABASE IF NOT EXISTS pypro;

USE pypro;

CREATE TABLE IF NOT EXISTS incidents_p (
    id INT AUTO_INCREMENT PRIMARY KEY,
    incident_code VARCHAR(50),
    service VARCHAR(100),
    severity VARCHAR(50),
    description TEXT,
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

---

🚀 Jenkins CI/CD Pipeline

The Jenkins pipeline automates the entire build and deployment process.

Pipeline Stages

flowchart LR

A[Checkout Code] --> B[Build Docker Image]
B --> C[Login to DockerHub]
C --> D[Push Image]
D --> E[SSH to EC2]
E --> F[Deploy to Kubernetes]

Steps

1. Checkout code from GitHub
2. Build Docker image
3. Login to DockerHub
4. Push image to DockerHub
5. SSH into EC2 instance
6. Deploy latest image to Kubernetes

---

📊 Kubernetes Commands

Check running pods:

kubectl get pods

Check services:

kubectl get svc

Restart deployment:

kubectl rollout restart deployment incident-app

View application logs:

kubectl logs deployment/incident-app

---

🌐 Application Access

Once deployed, access the application in the browser:

http://EC2_PUBLIC_IP:30007

---

🔐 Production Improvements

For production-ready infrastructure, the following improvements can be implemented:

- Kubernetes Secrets for database credentials
- Ingress Controller instead of NodePort
- Horizontal Pod Autoscaler
- Monitoring with Prometheus and Grafana
- Logging with ELK Stack

---

🎯 DevOps Skills Demonstrated

This project demonstrates the following DevOps practices:

- Containerization using Docker
- Continuous Integration and Continuous Deployment (CI/CD)
- Kubernetes container orchestration
- Cloud infrastructure deployment
- Database integration with AWS RDS
- Automated application deployment

---

