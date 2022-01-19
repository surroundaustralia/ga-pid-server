# GA PID Server
This repository contains the Apache rewrite rules & homepage for a persistent identifier (PID) server for Geoscience Australia.

## GitHub Actions
This repository uses GitHub for CI/CD, which has two events:

1. On pull request to the `main` branch:
    - Run a test Docker image to run `pytest` tests
2. On push to the `main` branch:
    - Build Docker image, push to AWS ECR & deploy to a Kubernetes cluster

