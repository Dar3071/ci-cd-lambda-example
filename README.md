# ci-cd-lambda-example
# updated
Random Quote Fetcher - AWS Lambda Function

# Overview

This AWS Lambda function fetches a random quote from the "Quotable" API and logs it to the console. It is designed as a simple example of integrating external APIs with AWS Lambda.

# Features

Fetches a random quote using the "Quotable" API.

Logs the quote along with its author to the console.

Includes basic error handling for HTTP request failures.

# Requirements

Python 3.x

AWS Lambda

IAM role with necessary permissions for API access.

# Setup Instructions

Create an AWS Lambda function in your AWS Management Console.

Upload this code as a Python script.

Configure the runtime to Python 3.x.

Attach a role with permissions to execute the function.

# CI/CD Integration

This project includes a buildspec.yml file for automating builds and deployments using AWS CodeBuild. It:

Installs dependencies listed in requirements.txt.

Packages the function code and dependencies into a ZIP file.

Deploys the updated package to AWS Lambda using the AWS CLI.
This ensures continuous delivery and seamless updates without manual intervention.

# Usage

This function can be triggered by any supported AWS Lambda event. It logs the retrieved quote in the Lambda execution logs.

# Version

v1.1 - Current version logs API response status and outputs a version label.

# Dependencies

requests (must be included in a deployment package or installed in the Lambda environment).

# Example Output

Random Quote: 'Success is not final, failure is not fatal: It is the courage to continue that counts.' - Winston Churchill
v1.1

# Notes

Ensure the "requests" module is included in the Lambda deployment package, as it is not built-in.

