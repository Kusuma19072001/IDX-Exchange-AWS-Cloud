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
| 07 | Serverless Architecture |
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
│   ├── 01-root-mfa.png
│   ├── 02-zero-spend-budget.png
│   └── README.md
├── week-02/
│   └── policies/
│       ├── README.md
│       └── S3UploaderOnly-kusuma.json
├── week-03/
│   ├── runbook.md
│   └── week-03-propertylite-curl.png
├── week-04/
│   ├── decision-guide.md
│   └── runbook.md
└── week-05/
    ├── README.md
    └── vpc-diagram.png
```

*The structure above highlights key deliverables; additional files and screenshots may also be present in each week's folder.*

## Main Application

### PropertyLite

PropertyLite is the application carried through the internship.

The goal is to use the application to practice real cloud engineering tasks rather than build new business logic every week:

**Deploy → Secure → Scale → Automate → Monitor → Operate**

## Current Status

**Completed:** Weeks 00–04 documented lab work.

**Current focus:** Week 05 — VPC & Networking.

**Next:** Week 06 — Load Balancing & Auto Scaling.

## Security & Cost Management

- Never commit credentials, access keys, passwords, private keys, or unredacted property datasets to GitHub.
- Apply least-privilege IAM permissions and restrict inbound network access.
- Remove temporary lab resources when they are no longer needed.
- Verify that EC2 instances, EBS volumes, snapshots, NAT Gateways, Elastic IP addresses, database instances, and other billable resources are in the intended state.
- Review AWS Budgets, credits, and billing estimates regularly.

---

This repository will be updated at the end of each week with completed work, documentation, configuration examples, and relevant evidence.
