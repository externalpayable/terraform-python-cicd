# terrform-python-cicd

This project provides a CI/CD pipeline implementation that automates the deployment of infrastructure changes using Terraform and Python. The pipeline includes stages for Terraform initialization, planning, Python script execution, testing, artifact management, deployment, and more. The pipeline is designed to work with Jenkins as the CI/CD platform.

## Prerequisites

Before setting up the CI/CD pipeline, ensure that you have the following prerequisites:

- Jenkins installed and configured on your build server.
- Python installed on the build server.
- Terraform installed on the build server.
- Git repository to store your codebase and pipeline configurations.

## Setup

Follow these steps to set up and configure the CI/CD pipeline:

1. Clone the repository to your build server:

   ```shell
   git clone https://github.com/kd9s0/terraform-python-cicd.git
