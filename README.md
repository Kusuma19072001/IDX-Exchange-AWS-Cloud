# AWS Cloud Engineer Journey

This repository documents my 12-week AWS Cloud Engineer internship journey with IDX Exchange.

The program focuses on deploying, securing, scaling, containerizing, automating, monitoring, and operating a cloud application on AWS. The main application used throughout the program is PropertyLite, a Flask-based real estate application.

## Progress

### Week 00 — Environment & PropertyLite Setup
- Set up WSL2 and Ubuntu on Windows.
- Installed and verified AWS CLI.
- Installed Git.
- Configured VS Code with AWS Toolkit and Terraform extension.
- Created the GitHub repository.
- Set up and tested the PropertyLite Flask application locally.
- Verified the application health and property endpoints.

### Week 01 — Cloud Fundamentals & Account Setup
- Enabled MFA on the AWS root account.
- Created a zero-spend AWS budget.
- Created the `kusuma-admin` IAM administrator user.
- Configured AWS CLI access.
- Verified authentication using `aws sts get-caller-identity`.
- Documented the AWS Shared Responsibility Model.
- Committed and pushed the Week 1 work to GitHub.

### Week 02 — IAM & Security Foundations
- Learned IAM users, groups, roles, and policies.
- Applied the principle of least privilege.
- Created the `S3UploaderOnly-kusuma` IAM policy.
- Created a restricted `s3-test-user`.
- Tested `s3:PutObject` and `s3:GetObject`.
- Verified that unauthorized bucket-listing requests returned `AccessDenied`.
- Created and reviewed an IAM Access Analyzer.
- Used IAM Policy Simulator to verify allowed and denied actions.
- Practiced debugging S3 authorization issues.
- Documented the policy in `week-02/policies/`.
- Cleaned up temporary Week 2 AWS resources after completing the lab.

### Week 03 — EC2 & PropertyLite Deployment
- Launched an Amazon Linux 2023 EC2 instance (`t3.micro`) in `us-east-1`.
- Configured the `property-api-sg` security group for SSH and API access.
- Connected to EC2 securely using SSH from Ubuntu (WSL).
- Deployed the PropertyLite Flask API and sample property CSV.
- Tested the `/health`, `/properties`, and property-detail endpoints.
- Verified the API returned the expected responses.
- Created and verified an EBS snapshot.
- Documented the deployment steps and saved screenshot evidence in `week-03/`.

## 12-Week Journey

| Week | Focus |
|------|-------|
| 00 | Environment & PropertyLite Setup |
| 01 | Cloud Fundamentals & Account Setup |
| 02 | IAM & Security Foundations |
| 03 | EC2 & Application Deployment |
| 04 | S3, RDS & DynamoDB |
| 05 | VPC & Networking |
| 06 | Load Balancing & Auto Scaling |
| 07 | Serverless Architecture |
| 08 | Terraform & Infrastructure as Code |
| 09 | Docker, ECR & ECS Fargate |
| 10 | CI/CD with GitHub Actions & OIDC |
| 11 | CloudWatch, Well-Architected & Cost |
| 12 | PropertyLite Capstone |

## Repository Structure

```text
IDX-Exchange-AWS-Cloud/
│
├── README.md
│
├── week-00/
│   └── propertylite/
│
├── week-01/
│   ├── 01-root-mfa.png
│   ├── 02-zero-spend-budget.png
│   └── README.md
│
└── week-02/
    └── policies/
        ├── README.md
        └── S3UploaderOnly-kusuma.json
└── week-03/
    ├── runbook.md
    └── week-03-propertylite-curl.png

## Main Application

### PropertyLite

PropertyLite is the application that will be carried through the internship.

The goal is not to build new business logic every week. Instead, the application is used to practice real cloud engineering tasks:

**Deploy → Secure → Scale → Automate → Monitor → Operate**

## Current Status

**Completed:** Week 0, Week 1, Week 2, Week 3

**Current focus:** Week 3 - EC2 & PropertyLite Deployment completed

**Next:** Week 4 - S3, RDS & DynamoDB

---

This repository will be updated at the end of each week with the work completed, documentation, configuration, and relevant evidence.

