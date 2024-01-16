# Data Pipeline Project

## Project Overview
Briefly describe the purpose and functionality of your data pipeline project. Include any relevant information about the data sources, processing steps, and expected outcomes.

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

```bash
# Example
python -m pip install -r requirements.txt
Installation
A step-by-step series of examples that tell you how to get a development environment running.

bash
Copy code
# Clone the repository
git clone [repository URL]

# 1- IF using docker
# Navigate to the project directory
cd data_pipeline_project

# Build the Docker image
docker build -t my-data-pipeline .

# Run the Docker container - graph json in the folder /path/on/host via docker run
docker run -v /path/on/host:/path/in/container my-data-pipeline


# 2-  IF using environnement only on local - graph json in the folder output_json/ 
python run src/main.py




