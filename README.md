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
- Documented the deployment steps in `week-03/runbook.md`.
- Saved relevant screenshot evidence in `week-03/`.

### Week 04 — Storage & Databases

- Practiced Amazon S3 bucket creation, object upload, and lifecycle configuration.
- Configured a lifecycle rule to transition eligible objects to S3 Glacier Flexible Retrieval.
- Connected to an Amazon RDS MySQL database from an EC2 client.
- Created the `training_data` database and practiced SQL commands.
- Explored SQL dump preparation and database import troubleshooting.
- Created a DynamoDB table named `Properties` with `L_ListingID` as the partition key.
- Configured EC2 IAM role permissions for DynamoDB access.
- Tested retrieving a DynamoDB item using the AWS CLI.
- Practiced cleaning up temporary AWS resources to help control costs.
- Documented the labs in `week-04/runbook.md` and `week-04/decision-guide.md`.
- Performed additional cleanup checks for temporary AWS resources.

### Week 05 — VPC & Networking

- Explored VPCs, public and private subnets, route tables, and Internet Gateways.
- Reviewed the network layout for the training environment.
- Practiced understanding the traffic path from a laptop through a bastion host to a private EC2 instance.
- Documented SSH access flow and the role of security groups.
- Created a VPC traffic-path diagram in `week-05/vpc-diagram.png`.
- Explained the architecture and traffic path in `week-05/README.md`.
- Reviewed AWS resource cleanup and cost considerations, including NAT Gateway and VPC endpoint removal.

**Architecture note:** The Week 5 diagram represents the intended bastion-to-private-instance SSH access pattern. Verify subnet associations, route tables, instance addresses, and security group rules in the AWS console before treating the diagram as a verified production architecture.

### Week 06 — Load Balancing & Auto Scaling

- Learned Application Load Balancer (ALB) concepts, listeners, target groups, and health checks.
- Explored EC2 Launch Templates and Auto Scaling Groups (ASG).
- Configured an Auto Scaling Group behind an Application Load Balancer.
- Worked with EC2 user-data scripts to automate application deployment.
- Configured health checks to monitor application instance availability.
- Practiced troubleshooting unhealthy targets and EC2 instance initialization.
- Investigated networking dependencies affecting instance deployment, including NAT Gateway requirements.
- Performed load testing against the PropertyLite application.
- Reviewed scaling behavior and load test results.
- Prepared a Week 6 load test report documenting the ASG and ALB architecture, observations, and results.

### Week 07 — Serverless & Event-Driven Architecture

**Lab 7.1 — PropertyLite Serverless Read Path**

- Re-hosted the PropertyLite property-read operation using API Gateway, AWS Lambda, and DynamoDB.
- Reused the existing `Properties` DynamoDB table with `L_ListingID` as its partition key.
- Created the `get-property` Lambda function using Python 3.12.
- Implemented DynamoDB `GetItem` to retrieve property records.
- Configured a custom least-privilege IAM policy scoped to the `Properties` table.
- Created an API Gateway HTTP API named `propertylite-serverless-api`.
- Configured the `GET /properties/{id}` route and connected it to Lambda.
- Deployed the API using the `$default` stage with automatic deployment.
- Tested the endpoint using a browser and verified successful JSON responses.

**Lab 7.2 — Amazon SQS & Dead-Letter Queue**

- Created a Standard SQS queue named `property-queue`.
- Created a separate Dead-Letter Queue named `property-dlq`.
- Configured the main queue's redrive policy with a maximum receive count of 3.
- Sent a sample property message through the main queue.
- Practiced repeated message reception and observed receive-count behavior.
- Verified that the message was transferred to the Dead-Letter Queue.
- Inspected the original message payload and metadata.
- Documented the queue configuration and DLQ verification results.

**Lab 7.3 — Debugging API Gateway 500 Errors**

- Inspected Lambda execution logs through Amazon CloudWatch Logs.
- Reviewed invocation START, END, and REPORT entries.
- Studied common Lambda failure scenarios, including `AccessDeniedException`, `KeyError`, and `ResourceNotFoundException`.
- Reviewed the relationship between IAM permissions, API Gateway route configuration, and Lambda event parsing.
- Retested the deployed PropertyLite API and confirmed successful JSON responses.
- Documented the diagnostic investigation and findings.

**Lab 7.3 note:** No actual HTTP 500 failure was reproduced during the investigation. The existing serverless read path was functioning successfully, so no code or configuration fixes were necessary.


### Week 08 — Infrastructure as Code (Terraform)

- Recreated the Week 5 VPC architecture using Terraform and the AWS VPC module.
- Provisioned a VPC with two public subnets, two private subnets, an Internet Gateway, and a NAT Gateway.
- Used `terraform init`, `validate`, `plan`, and `apply` to initialize, validate, review, and deploy infrastructure.
- Successfully provisioned 19 AWS resources in `us-east-1`.
- Verified the deployed VPC through the AWS Management Console.
- Inspected Terraform state using `terraform state list`.
- Investigated state differences using `terraform plan -refresh-only`.
- Successfully destroyed all 19 Terraform-managed resources using `terraform destroy`.
- Documented Terraform state management, drift detection, cleanup, and security best practices.

**Deliverables:** [week-08/](week-08/)

## 12-Week Journey

| Week | Focus |
|---|---|
| 00 | Environment & PropertyLite Setup |
| 01 | Cloud Fundamentals & Account Setup |
| 02 | IAM & Security Foundations |
| 03 | EC2 & Application Deployment |
| 04 | S3, RDS & DynamoDB |
| 05 | VPC & Networking |
| 06 | Load Balancing & Auto Scaling |
| 07 | Serverless & Event-Driven Architecture |
| 08 | Terraform & Infrastructure as Code |
| 09 | Docker, ECR & ECS Fargate |
| 10 | CI/CD with GitHub Actions & OIDC |
| 11 | CloudWatch, Well-Architected & Cost |
| 12 | PropertyLite Capstone |

## Repository Structure

```text
IDX-Exchange-AWS-Cloud/
├── README.md
├── week-00/
│   └── PropertyLite/
├── week-01/
│   ├── README.md
│   └── screenshots/
├── week-02/
│   └── policies/
│       ├── README.md
│       └── S3UploaderOnly-kusuma.json
├── week-03/
│   └── runbook.md
├── week-04/
│   ├── decision-guide.md
│   └── runbook.md
├── week-05/
│   ├── README.md
│   └── vpc-diagram.png
├── week-06/
│   └── load-test-report.md
└── week-07/
    ├── README.md
    ├── curl-collection.md
    ├── lambda/
    │   └── lambda_function.py
    ├── postman/
    │   └── README.md
    ├── screenshots/
    ├── sqs/
    │   └── README.md
    └── debugging/
        └── README.md
└── week-08/
    ├── main.tf
    ├── .gitignore
    ├── .terraform.lock.hcl
    └── README.md
```

*The repository structure highlights key deliverables. Additional scripts, screenshots, configuration files, and supporting documentation may also be present in individual weekly folders.*

## Main Application

### PropertyLite

PropertyLite is the application carried throughout the internship.

The objective is to apply cloud engineering concepts to a consistent application rather than develop new business logic every week.

**Deploy → Secure → Scale → Automate → Monitor → Operate**

The application has been used to explore traditional EC2 deployment, load balancing, Auto Scaling, serverless APIs, DynamoDB integration, and event-driven messaging.

## Current Status


**Completed:** Weeks 00–08 documented lab work.

**Current focus:** Week 08 completed — Terraform & Infrastructure as Code. Successfully provisioned, validated, inspected, and destroyed AWS networking infrastructure using Terraform.

**Upcoming:** Docker, ECS Fargate, CI/CD automation, monitoring, cost optimization, and the PropertyLite capstone.

## Security & Cost Management


- Never commit credentials, access keys, passwords, private keys, or unredacted property datasets to GitHub.
- Apply least-privilege IAM permissions and restrict inbound network access.
- Remove temporary lab resources when they are no longer needed.
- Verify that EC2 instances, EBS volumes, snapshots, NAT Gateways, Elastic IP addresses, database instances, and other billable resources are in the intended state.
- Review AWS Budgets, credits, and billing estimates regularly.
- Review SQS queue retention and message contents before deleting or purging queues.

---

This repository will be updated at the end of each week with completed work, documentation, configuration examples, and relevant evidence.
