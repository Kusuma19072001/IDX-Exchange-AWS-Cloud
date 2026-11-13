
# Week 8 — Infrastructure as Code (Terraform)

## Overview

During Week 8 of the IDX Exchange AWS Cloud Engineer Internship, I used Terraform to provision and manage AWS networking infrastructure through Infrastructure as Code (IaC).

The objective was to reproduce the Week 5 VPC architecture using Terraform instead of manually creating resources in the AWS Management Console.

## Concepts Learned

### Infrastructure as Code (IaC)

Infrastructure as Code allows cloud resources to be defined and managed using configuration files rather than manual console operations.

### Declarative vs. Imperative Provisioning

- Declarative: Define the desired infrastructure state, and Terraform determines the required actions.
- Imperative: Specify the individual commands or steps needed to create infrastructure.

Terraform follows a declarative approach.

### Terraform State

Terraform maintains a state file (`terraform.tfstate`) to track the infrastructure resources it manages.

State helps Terraform:
- Associate configuration resources with actual AWS resources.
- Identify infrastructure changes.
- Determine which resources need to be created, updated, or destroyed.
- Manage dependencies during infrastructure operations.

State files may contain sensitive information and must not be committed to GitHub.

### Terraform Drift

Infrastructure drift occurs when actual cloud resources differ from the expected or recorded infrastructure state.

Drift can occur when resources are modified or deleted outside Terraform, such as through the AWS Console.

## Lab 8.1 — Reproduce the VPC Using Terraform

### Environment

- Cloud Provider: AWS
- Region: us-east-1
- Operating System: Ubuntu (WSL2)
- Terraform Version: 1.16.3
- AWS Provider: HashiCorp AWS
- VPC Module: terraform-aws-modules/vpc/aws v5.8.1

### VPC Configuration

| Component | Configuration |
|---|---|
| VPC Name | training-vpc-tf |
| VPC CIDR | 10.1.0.0/16 |
| Availability Zones | us-east-1a, us-east-1b |
| Public Subnet 1 | 10.1.1.0/24 |
| Public Subnet 2 | 10.1.2.0/24 |
| Private Subnet 1 | 10.1.101.0/24 |
| Private Subnet 2 | 10.1.102.0/24 |
| NAT Gateway | Enabled |
| NAT Gateway Count | 1 |

The Terraform configuration is defined in `main.tf`.

### Terraform Commands

#### terraform init

Initializes the Terraform working directory, downloads required providers and modules, and prepares the backend.

#### terraform validate

Checks whether the Terraform configuration is syntactically and internally valid.

Result:

`Success! The configuration is valid.`

#### terraform plan

Previews the infrastructure changes Terraform intends to make without applying them.

Initial result:

`Plan: 19 to add, 0 to change, 0 to destroy.`

#### terraform apply

Creates or updates AWS infrastructure according to the Terraform configuration.

Result:

`Apply complete! Resources: 19 added, 0 changed, 0 destroyed.`

### AWS Verification

Verified the newly created VPC through the AWS Management Console.

- VPC Name: training-vpc-tf
- VPC ID: vpc-04c4e428ff015ed33
- Status: Available

Terraform successfully provisioned the VPC, public and private subnets, Internet Gateway, NAT Gateway, Elastic IP, route tables, associations, and default networking resources.

## Debug Lab 8.2 — Terraform State Drift

### Objective

Understand how Terraform tracks infrastructure and detects differences between recorded state and actual AWS resources.

### Step 1 — Inspect Terraform State

Command:

`terraform state list`

Result:

Terraform listed all 19 managed resource addresses.

### Step 2 — Check for Drift

Command:

`terraform plan -refresh-only`

Result:

Terraform detected changes in recorded route-table attributes.

The refreshed information included:
- Public route table: default route to the Internet Gateway.
- Private route table: default route to the NAT Gateway.

These differences may reflect AWS-populated route information after resource creation.

No manual modification or deletion was performed to simulate drift.

The refresh-only plan inspected differences without modifying AWS infrastructure.

### Lessons Learned

- Terraform state maps configuration resources to real AWS infrastructure.
- Manual infrastructure changes can introduce drift.
- `terraform state list` displays managed resources.
- `terraform plan -refresh-only` detects differences between recorded state and actual infrastructure.
- Terraform state should be protected from unauthorized access.
- State operations such as import or state removal must be performed carefully.

## Cleanup — terraform destroy

The command `terraform destroy` removes infrastructure managed by the current Terraform configuration and state.

Command:

`terraform destroy`

Result:

`Destroy complete! Resources: 19 destroyed.`

The Week 8 Terraform-managed VPC and associated resources were successfully destroyed.

This cleanup was important because NAT Gateways and public IPv4 addresses can incur AWS charges.

The existing Week 5 VPC was not included in the Week 8 Terraform destroy operation.

## Security and Best Practices

- Review Terraform plans before applying changes.
- Never commit Terraform state files to GitHub.
- Use `.gitignore` to exclude `.terraform/` and state files.
- Commit `.terraform.lock.hcl` for reproducible provider selection.
- Avoid modifying Terraform-managed infrastructure manually.
- Use least-privilege AWS permissions.
- Destroy temporary lab resources after testing.
- For team environments, consider a secure remote state backend with appropriate access controls and locking.

## Deliverables

- `main.tf` — Terraform VPC configuration.
- `.gitignore` — Excludes Terraform state and local working files.
- `.terraform.lock.hcl` — Records provider dependency selections.
- `README.md` — Documents provisioning, state management, drift investigation, and cleanup.

## Outcome

Successfully provisioned 19 AWS networking resources using Terraform, inspected Terraform state and refreshed infrastructure information, and destroyed all 19 Terraform-managed resources.

This lab demonstrated the benefits of Infrastructure as Code for repeatable provisioning, infrastructure visibility, change management, and controlled cleanup.
