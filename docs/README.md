
```markdown
# Serverless Web Scraper with AWS

## Project Overview
"Serverless Web Scraper with AWS" is a serverless application built on Amazon Web Services (AWS). It uses AWS Lambda to scrape data from specified websites and stores the results in Amazon DynamoDB. The project is designed to be flexible, scalable, and easy to maintain, leveraging serverless architecture for lower operational overhead.

## Key Features
- **Serverless Design**: Utilizes AWS Lambda for code execution and Amazon DynamoDB for data storage.
- **Web Scraping**: Extracts data from specified websites using Python-based scraping logic.
- **Scheduled and On-Demand Execution**: CloudWatch Events schedule periodic scraping, while AWS API Gateway provides an HTTP endpoint for manual triggers.
- **Logging and Monitoring**: AWS CloudWatch is used for monitoring Lambda execution and storing logs.

## Project Structure
The project is organized into the following key directories:
- **`src/`**: Contains the source code, including the Lambda function, data handling, and utilities.
- **`tests/`**: Includes unit and integration tests to ensure code quality.
- **`deployment/`**: Holds deployment-related files, such as CloudFormation templates and deployment scripts.
- **`config/`**: Contains configuration files, such as AWS credentials and settings.
- **`docs/`**: Includes documentation related to the project.

## Requirements
To run this project, you need the following:
- AWS account with permissions to create and manage Lambda, DynamoDB, S3, CloudWatch, and API Gateway resources.
- Python 3.7 or later.
- Python packages specified in `requirements.txt`.
- A development environment for AWS, such as AWS CLI and AWS SAM (Serverless Application Model).

## Setup Instructions
Follow these steps to set up the project:

1. **Clone the Repository**
   Clone the repository to your local environment:
   ```bash
   git clone https://github.com/naoralkobi/serverless_web_scraper_aws.git
   ```

2. **Install Dependencies**
   Navigate to the project directory and install Python dependencies:
   ```bash
   cd serverless_web_scraper_aws/src/lambda/scraper
   pip install -r requirements.txt
   ```

3. **Configure AWS**
   Set up your AWS credentials and configuration:
   ```bash
   aws configure
   ```

4. **Deploy the Project**
   Use deployment scripts or AWS CloudFormation to deploy the Lambda function and related resources:
   ```bash
   bash deployment/scripts/deploy.sh
   ```

## Usage Instructions
- To trigger a scheduled scrape, wait for the next scheduled event, or manually trigger using CloudWatch.
- To manually trigger via HTTP, send a request to the API Gateway endpoint (configured during deployment).
- Check CloudWatch logs for monitoring and debugging information.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit and push your changes.
4. Open a pull request with a description of your changes.

## Contact
For questions or support, contact naor9985@gmail.com or open an issue on GitHub.



how to run:

1. ``` aws lambda invoke --function-name "RequestsLambda" --payload '{"url": "https://edition.cnn.com/interactive/2024/04/world/human-elephant-conflict-sri-lanka-cnnphotos/"}' output.json```
2. ```sam local invoke "RequestsLambda" --event test_event.json```
