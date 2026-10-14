# Week 04 — Storage & Databases
## AWS Cloud Engineer Internship | PropertyLite

> **Objective:** Practice object storage with Amazon S3, relational database connectivity with Amazon RDS, and NoSQL item retrieval with Amazon DynamoDB.  
> **AWS Region:** `us-east-1` (US East — N. Virginia)

---

## 1. Lab Overview

| Lab | Service | What I practiced |
|---|---|---|
| 4.1 | Amazon S3 | Create a bucket, upload an object, configure a lifecycle rule, and clean up |
| 4.2 | Amazon RDS | Connect to managed MySQL from an EC2 client and inspect a database |
| 4.3 | Amazon DynamoDB | Create a table, configure IAM access, and retrieve an item |

## 2. Resources Used

| Resource | Name / Identifier | Purpose |
|---|---|---|
| RDS MySQL | `training-db` | Relational database practice |
| EC2 client | `week4-rds-client` | Run MySQL client and AWS CLI commands |
| DynamoDB table | `Properties` | Store and retrieve a sample property item |
| S3 bucket | `my-training-bucket-kusuma` | Object upload and lifecycle practice |
| IAM role | `week4-dynamodb-ec2-role` | Grant EC2 limited DynamoDB access |

These resources were used during the lab. Cleanup was initiated as recorded in Section 7; verify final deletion status in the AWS console.

---

## 3. Lab 4.1 — Amazon S3

### Goal
Practice bucket creation, object upload, lifecycle configuration, and cleanup.

### Steps completed
1. Created `my-training-bucket-kusuma` in `us-east-1`.
2. Uploaded an object named `runbook.md`.
3. Verified the object with the AWS CLI.
4. Created a lifecycle rule named `archive-after-30-days`.
5. Configured eligible objects to transition to S3 Glacier Flexible Retrieval after 30 days.
6. Deleted the test object and bucket during cleanup.

### Verification command

Run from a terminal configured for the correct AWS account:

```bash
aws s3 ls s3://my-training-bucket-kusuma --region us-east-1
```

**Expected result:** The command lists objects currently in the bucket. After deleting the bucket, the command will no longer succeed because the bucket no longer exists.

### Key takeaway
Amazon S3 is object storage. Lifecycle rules can automate storage-class transitions, but Glacier storage classes have minimum storage-duration and retrieval-cost considerations.

---

## 4. Lab 4.2 — Amazon RDS (MySQL)

### Goal
Connect to a managed MySQL database from an EC2 instance and practice basic SQL.

### Configuration recorded
- **DB identifier:** `training-db`
- **Engine:** MySQL 8.4
- **Database created:** `training_data`
- **Region:** `us-east-1`
- **Client:** `week4-rds-client`

### Network access
The RDS security group was configured to allow TCP port `3306` from the EC2 client's security group.

> **Security reminder:** Keep database access limited to trusted sources. Do not publish passwords, access keys, private connection details, or unnecessary public IP information in a repository.

### Connect to MySQL

Replace the placeholder with the endpoint shown in the RDS console. Enter the password only at the interactive prompt.

```bash
mysql -h YOUR_RDS_ENDPOINT -P 3306 -u YOUR_DB_USER -p
```

After connecting, run:

```sql
CREATE DATABASE IF NOT EXISTS training_data;
USE training_data;
SHOW TABLES;
```

### Import status
The supplied property SQL dump required schema adjustments, and the import did not complete reliably during the recorded lab. **Do not report the full dataset as successfully imported unless you verify the final table count, row count, and sample records.**

The source dump contained sensitive property and personal information. Do not commit the raw dump or unredacted records to GitHub.

### Key takeaway
Amazon RDS manages the database infrastructure. Security groups control network connectivity, while database users and grants control database-level access.

---

## 5. Lab 4.3 — Amazon DynamoDB

### Goal
Create a NoSQL table, grant the EC2 instance limited access, and retrieve an item.

### Configuration
| Setting | Value |
|---|---|
| Table | `Properties` |
| Partition key | `L_ListingID` |
| Key type | String |
| Capacity mode | On-demand |
| Region | `us-east-1` |

### Steps completed
1. Created the `Properties` table.
2. Added a sample item for testing.
3. Attached an IAM role to the EC2 instance with limited DynamoDB permissions.
4. Checked the AWS identity and tested item retrieval.

### Retrieve an item

```bash
aws dynamodb get-item \
  --table-name Properties \
  --key '{"L_ListingID":{"S":"R100001"}}' \
  --region us-east-1
```

**Expected result:** If the table exists and the item is present, the command returns the item attributes as JSON. If the item is missing, the response may contain an empty `Item` result.

### IAM principle
The EC2 role was configured for table-scoped actions such as `GetItem`, `PutItem`, and `DescribeTable`.

### Key takeaway
DynamoDB is a managed NoSQL database. The partition key identifies items, and IAM policies determine which AWS API actions the workload can perform.

---

## 6. Troubleshooting & Lessons Learned

| Issue | Resolution / lesson |
|---|---|
| Network testing utility was unavailable | Not every tool is preinstalled on Amazon Linux; check availability and use an appropriate alternative. |
| DynamoDB access was denied initially | Attach an EC2 IAM role with only the required permissions; avoid storing long-term access keys on the instance. |
| SQL import was interrupted | Verify table names, row counts, and sample records before calling an import successful. |
| S3 cleanup required the correct order | Remove objects and review lifecycle configuration before deleting the bucket. |

---

## 7. Cleanup Checklist

Cleanup actions were reported as performed or initiated. Confirm the final state in the AWS console before considering cleanup complete.

- [x] **S3:** Deleted the test object and bucket; deletion was shown in the console.
- [ ] **DynamoDB:** Confirm `Properties` is fully deleted, not still in `Deleting` state.
- [ ] **RDS:** Confirm `training-db` is fully deleted.
- [ ] **EC2:** Confirm `week4-rds-client` is terminated.
- [ ] **IAM:** Review `week4-dynamodb-ec2-role` and remove it only if no longer needed.
- [ ] **Other charges:** Check for leftover EBS volumes, snapshots, RDS snapshots, Elastic IP addresses, and NAT gateways.

Do **not** delete the default VPC, subnets, or route tables as part of this lab cleanup.

---

## 8. Evidence & Deliverables

### Evidence screenshots
- DynamoDB table creation and sample item
- Successful DynamoDB `get-item` command
- EC2 instance and IAM role configuration
- S3 object upload and lifecycle rule
- S3 bucket deletion
- RDS connection and security-group configuration, if available

Before committing screenshots, confirm that they do not expose passwords, access keys, sensitive records, or unnecessary personal information.

### Deliverables
- `week-04/decision-guide.md`
- `week-04/runbook.md`
- Supporting screenshots, if required by the internship handbook

---

## 9. Summary

Week 4 provided hands-on practice with three AWS services:

- **Amazon S3:** Object storage, lifecycle management, and cleanup
- **Amazon RDS:** Managed MySQL connectivity and database fundamentals
- **Amazon DynamoDB:** NoSQL table creation, IAM permissions, and item retrieval

The main lessons were to use least-privilege permissions, protect sensitive data, verify results rather than assume success, and remove temporary resources to control costs.
