# Week 5 — VPC Diagram and Traffic Path

## Purpose

This diagram explains how an administrator connects from a laptop to an EC2 instance that has no public IPv4 address, using a public bastion host as the SSH jump point.

## Traffic path

1. **Laptop → public bastion:** Start an SSH connection to `training-bastion` using its public IPv4 address (`184.195.186.185`) and the appropriate private key.
2. **Internet Gateway:** The public subnet's route table has a default route (`0.0.0.0/0`) to the Internet Gateway, allowing internet traffic to reach the public bastion when its security group permits it.
3. **Bastion → private EC2:** After logging in to the bastion, open a second SSH connection to the private instance's private IP, `10.0.11.252`, on TCP port 22.
4. **Security groups:** The bastion security group should permit SSH only from the administrator's approved source IP. The private instance's security group should permit SSH from the bastion security group, rather than from the public internet.
5. **Private instance:** The `training-private` instance has no public IPv4 address, so it is not directly addressable from the public internet.

## Important security notes

- Do not open SSH (TCP 22) to `0.0.0.0/0`.
- Keep the private instance without a public IPv4 address.
- Use a bastion/jump host only when needed; AWS Systems Manager Session Manager is another option when configured with the required IAM permissions, agent, and network connectivity.
- Never commit `training-key.pem`, credentials, passwords, or real property data to GitHub.

## Current cleanup state

The NAT Gateway and the S3 VPC endpoint were deleted during the Week 4 cost cleanup. The diagram focuses on the SSH access path used in the lab. **Private-subnet internet egress through a NAT Gateway is currently unavailable** unless a NAT Gateway is recreated and the private route table is updated.

## Verification note

The screenshots showed `training-bastion` with public IPv4 `184.195.186.185`, and `training-private` with private IP `10.0.11.252` and no public IPv4 address. The private instance's subnet was displayed as `training-subnet-public1-us-east-1a` in the console, despite the instance being treated as the private target in this lab. Verify the subnet association and security group rules in the final environment before presenting this as a production architecture.

## Deliverables

- `vpc-diagram.png` — diagram of the SSH traffic path.
- `README.md` — explanation of the traffic path and security controls.
