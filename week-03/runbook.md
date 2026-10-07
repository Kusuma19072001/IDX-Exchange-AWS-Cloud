# Week 3 — EC2 & PropertyLite Runbook

## Overview

In Week 3, I deployed the PropertyLite Flask API on an Amazon EC2 instance running Amazon Linux 2023. I configured network access, connected to the instance using SSH, tested the API endpoints, created an EBS snapshot, and documented SSH troubleshooting and cleanup procedures.

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
4. Connect to the EC2 Instance

I connected to the instance using SSH:

ssh -i ~/.ssh/training-key.pem ec2-user@<EC2-PUBLIC-IP>

The SSH connection was successful and opened an Amazon Linux shell.

5. Deploy PropertyLite

The PropertyLite application was deployed under:

/opt/property-api

The application included:

app.py
rets_property_sample.csv

The Flask application listens on port 8080.

6. Start the PropertyLite API

The EC2 user-data bootstrap script installed Flask and started the PropertyLite API.

The application was started with:

cd /opt/property-api
nohup python3 app.py > /var/log/property-api.log 2>&1 &

I verified that the Flask process was running.

7. Test the Health Endpoint

From my local WSL terminal, I tested:

curl http://<EC2-PUBLIC-IP>:8080/health

Expected response:

{"status":"ok"}

The health endpoint returned successfully.

8. Test the Property Endpoint

I tested a specific property:

curl http://<EC2-PUBLIC-IP>:8080/properties/R100234

The API returned the property information successfully.

A screenshot showing both successful curl responses was saved as:

week-03-propertylite-curl.png

and uploaded to the week-03/ directory in the GitHub repository.

9. Create an EBS Snapshot

The EC2 instance used an 8 GiB gp3 root EBS volume.

I created an EBS snapshot of the volume.

Snapshot ID:

snap-0faba8386562ee71f

The snapshot was created successfully.

10. Verify EC2 Status Checks

I verified that the EC2 instance passed:

System status check
Instance status check
EBS status check

All checks passed successfully.

Debug Lab 3.3 — SSH Timeout Troubleshooting
11. Symptom

An SSH connection can time out if the security group's SSH rule allows access only from an old public IP address.

12. Diagnose

Check the following in order:

Confirm the EC2 instance is running.
Confirm the instance has the correct public IPv4 address.
Check the security group's inbound SSH rule.
Confirm the SSH source is the user's current public IP.
Check the VPC route and network ACLs if necessary.
13. Root Cause

The security group used a My IP SSH rule.

This creates a /32 rule for the public IP address that was detected when the rule was created.

If the user's public IP changes, SSH can time out because the new IP is no longer allowed.

14. Fix

Update the security group's SSH inbound rule to the user's current public IP using the My IP option.

SSH should remain restricted to the user's IP rather than opening port 22 to everyone.

Cleanup
15. Terminate the EC2 Instance

After completing the lab, the EC2 instance should be terminated to avoid unnecessary AWS charges.

Instance:

property-api-01

16. Verify the EBS Volume

After the instance is terminated, verify that the root EBS volume is also deleted because it was configured with Delete on Termination.

The EBS snapshot should not be deleted because it is part of the Week 3 lab deliverable.

Week 3 Deliverables
week-03/runbook.md
week-03/week-03-propertylite-curl.png
EBS snapshot successfully created
EC2 and EBS status checks verified
Cleanup completed: EC2 instance terminated and EBS volume verified as deleted
Week 3 Summary
Deployed a Flask-based PropertyLite API on Amazon EC2.
Configured a security group for SSH and application access.
Connected to EC2 using an SSH key from WSL.
Tested the API using curl.
Created an EBS snapshot.
Practiced diagnosing SSH timeout issues.
Completed EC2 cleanup and verified that the EBS volume was deleted while the snapshot was retained.
