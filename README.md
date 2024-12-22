# ZOOCAMP_Mike_regration


## Objective

The goal of this project is to apply everything we have learned in this course to build an end-to-end machine learning project.

## Problem Statement

For the project, we will build an end-to-end ML project. This includes:

1. Selecting a dataset of interest. 
2. Training a model on that dataset while tracking experiments.
3. Creating a model training pipeline.
4. Deploying the model in batch, as a web service, or in streaming mode.
5. Monitoring the performance of the model.
6. Following the best practices for ML project development.

## Technologies

- **Cloud**: AWS localstack
- **Experiment tracking tools**: MLFlow
- **Workflow orchestration**: Mage
- **Monitoring**: Evidently
- **CI/CD**: GitHub Actions
- **Infrastructure as Code (IaC)**: Terraform?


## Evaluation Criteria

### Problem Description
- **0 points**: The problem is not described.
- **1 point**: The problem is described briefly or unclearly.
- **2 points**: The problem is well described and clearly identifies what the project solves.

### Cloud Usage
- **0 points**: Cloud is not used, and everything runs locally.
- **2 points**: The project is developed on the cloud, uses Localstack (or similar), or is deployed on Kubernetes or similar platforms.
- **4 points**: The project is developed on the cloud, and IaC tools are used to provision the infrastructure.

### Experiment Tracking and Model Registry
- **0 points**: No experiment tracking or model registry.
- **2 points**: Experiments are tracked, or models are registered in a registry.
- **4 points**: Both experiment tracking and model registry are used.

### Workflow Orchestration
- **0 points**: No workflow orchestration.
- **2 points**: Basic workflow orchestration is implemented.
- **4 points**: Fully deployed workflow orchestration.

### Model Deployment
- **0 points**: Model is not deployed.
- **2 points**: Model is deployed but only locally.
- **4 points**: Model deployment is containerized and deployable to the cloud, or advanced tools are used.

### Model Monitoring
- **0 points**: No model monitoring.
- **2 points**: Basic model monitoring calculates and reports metrics.
- **4 points**: Comprehensive monitoring includes alerts or conditional workflows (e.g., retraining, generating debugging dashboards, switching to different models).

### Reproducibility
- **0 points**: No instructions or missing data.
- **2 points**: Instructions are present but incomplete, or data is missing.
- **4 points**: Clear instructions, easy-to-run code, and dependencies are specified.

### Best Practices
- Unit tests: **1 point**
- Integration tests: **1 point**
- Linter/Formatter: **1 point**
- Makefile: **1 point**
- Pre-commit hooks: **1 point**
- CI/CD pipeline: **2 points**

## Resources

### Datasets

You can explore and select datasets from:
- [Kaggle](https://www.kaggle.com/)
- [AWS Datasets](https://registry.opendata.aws/)
- [UK Government Open Data](https://data.gov.uk/)
- [GitHub Archive](https://www.githubarchive.org/)
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
- [Million Songs Dataset](http://millionsongdataset.com/)
- [COVID-19 Datasets](https://github.com/CSSEGISandData/COVID-19)
- [Azure Datasets](https://azure.microsoft.com/en-us/services/open-datasets/)
- [Google's Dataset Search Engine](https://datasetsearch.research.google.com/)
- [European Statistics Datasets](https://ec.europa.eu/eurostat/data/database)

Feel free to explore other datasets from the course-provided resources or contribute additional suggestions.


## Getting Started

1. Clone this repository.
2. Follow the setup instructions in `README.md`.
3. Start with the provided directory structure.

## Directory Structure

```
project-name/
├── data/                   # Directory for raw and processed data
│   ├── raw/
│   ├── processed/
├── notebooks/              # Jupyter notebooks for EDA and experiments
├── src/                    # Source code for the pipeline
│   ├── __init__.py
│   ├── data_processing.py  # Data cleaning and preprocessing functions
│   ├── model_training.py   # Code for model training
│   ├── batch_prediction.py # Batch prediction pipeline
├── tests/                  # Tests for code
│   ├── unit/
│   ├── integration/
├── models/                 # Saved models
├── monitoring/             # Scripts for monitoring
├── docker/                 # Docker-related files
│   ├── Dockerfile
│   ├── docker-compose.yaml
├── scripts/                # Shell scripts
│   ├── run_project.sh      # Script for running the pipeline
├── Makefile                # Automation tasks
├── requirements.txt        # Python dependencies
├── README.md               # Project description and instructions
├── .gitignore              # Ignored files
└── config.yaml             # Configuration file for pipeline parameters
```

