# AWS Toolkit

Automated security and cost optimization tool for Amazon Web Services. This toolkit scans your AWS environment to identify potential vulnerabilities, misconfigurations, and cost-saving opportunities.

## Features

*   **Security Auditing:**
    *   Detect unused IAM access keys.
    *   Identify insecure IAM policies (wildcard actions/principals).
    *   Detect misconfigured IAM roles with overly permissive policies.
    *   Enforce MFA for IAM users.
    *   Scan S3 buckets for potential secrets.
    *   Detect publicly accessible S3 buckets.
    *   Check Lambda function security (VPC placement, sensitive env vars).
*   **Cost Optimization:**
    *   Suggest cost savings (stopped instances, unused volumes, RDS).
    *   Detect old API keys.
*   **Log Analysis:** Analyze CloudTrail logs for suspicious activity (failed logins, unauthorized operations).

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/marcoro11/python-aws-tools.git
    cd aws-toolkit
    ```

2.  Install dependencies:
    ```bash
    pipenv install
    ```

## Usage

Run the tool with desired checks:

```bash
pipenv run python main.py --check-iam
pipenv run python main.py --scan-s3
pipenv run python main.py --detect-public-buckets
pipenv run python main.py --analyze-cloudtrail
pipenv run python main.py --suggest-cost-optimizations
# ...and other checks as needed...
```

## AWS Credentials

This tool uses [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) for AWS authentication. Configure your credentials using one of the following methods:

- **Environment variables**:
  ```bash
  export AWS_ACCESS_KEY_ID=your-access-key-id
  export AWS_SECRET_ACCESS_KEY=your-secret-access-key
  export AWS_DEFAULT_REGION=us-east-1
  ```
- **AWS config/credentials file** (`~/.aws/credentials`)
- **IAM role** (if running on EC2 or similar)

See the [boto3 credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) for more details.