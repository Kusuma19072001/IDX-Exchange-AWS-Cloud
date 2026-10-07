# Week 3 — EC2 & PropertyLite Runbook

## Overview

In Week 3, I deployed the PropertyLite Flask API on an Amazon EC2 instance running Amazon Linux 2023. I configured network access, connected to the instance using SSH, started the application, tested the API, and created an EBS snapshot for backup.

## 1. Launch the EC2 Instance

I launched an EC2 instance using:

- AMI: Amazon Linux 2023
- Instance type: t3.micro
- Region: US East (N. Virginia)
- Root volume: 8 GiB gp3
- Auto-assign public IPv4: Enabled

The instance was named:

`property-api-01`

## 2. Configure the Security Group

I created a security group named:

`property-api-sg`

Inbound rules:

| Protocol | Port | Source | Purpose |
|---|---:|---|---|
| TCP | 22 | My IP | SSH administration |
| TCP | 8080 | 0.0.0.0/0 | PropertyLite API |

SSH was restricted to my current public IP instead of allowing SSH from everyone.

Port 8080 was opened so the PropertyLite API could be accessed from outside the EC2 instance.

## 3. Create and Configure the SSH Key

I created/downloaded the EC2 key pair:

`training-key.pem`

I copied it into my WSL SSH directory and restricted its permissions:

```bash
mkdir -p ~/.ssh
cp /mnt/c/Users/kusum/Downloads/training-key.pem ~/.ssh/
chmod 400 ~/.ssh/training-key.pem
