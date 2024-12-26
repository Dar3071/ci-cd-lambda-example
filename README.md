# ci-cd-lambda-example

Random Quote AWS Lambda Application

# Overview

This project demonstrates my ability to build and deploy serverless applications using AWS Lambda. It features a Python-based function that fetches random quotes from the ZenQuotes API and includes a CI/CD pipeline for automated deployment.

# Key Features

Serverless Architecture - Uses AWS Lambda for scalable and event-driven execution.

API Integration - Fetches data from the ZenQuotes API.

CI/CD Pipeline - Automates packaging and deployment with AWS CodeBuild.

# Skills Demonstrated

Python programming

AWS Lambda and serverless development

REST API integration

CI/CD pipelines and DevOps practices

# Setup Instructions

Clone the Repository:

git clone <repository-url>
cd <repository-folder>

Install Dependencies:Ensure Python 3.12 is installed. Create a requirements.txt file and include any dependencies.

pip install -r requirements.txt -t lib

Build and Package:Use the provided buildspec.yml file to create a deployment package.

zip -r9 deployment_package.zip .

Deploy the Lambda Function:Replace python-application with your Lambda function name.

aws lambda update-function-code --function-name python-application --zip-file fileb://deployment_package.zip

# Usage

The Lambda function fetches a random quote from the ZenQuotes API when triggered and logs the result in CloudWatch.

# Example Output

Random Quote: 'Be yourself; everyone else is already taken.' - Oscar Wilde

