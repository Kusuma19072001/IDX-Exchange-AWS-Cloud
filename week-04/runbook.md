\# Week 4 — Storage and Databases Runbook



\## 1. Overview



\*\*Objective:\*\* Learn how to store files in Amazon S3, work with relational databases using Amazon RDS, and retrieve individual records using Amazon DynamoDB.



\*\*AWS Region:\*\* `us-east-1` (US East — N. Virginia)



\*\*Project:\*\* PropertyLite



\## 2. AWS Resources Used



| Resource | Name | Purpose |

|---|---|---|

| Amazon RDS | `training-db` | Practice relational database connectivity |

| Amazon EC2 | `week4-rds-client` | Connect to RDS and run AWS CLI commands |

| Amazon DynamoDB | `Properties` | Store and retrieve property records |

| Amazon S3 | `my-training-bucket-kusuma` | Upload and manage objects |

| IAM Role | `week4-dynamodb-ec2-role` | Allow the EC2 instance to access DynamoDB |



These resources were used during the lab. They were subsequently scheduled for deletion or cleaned up as described below.



\## 3. Lab 4.1 — Amazon S3



\### Objective

Create an S3 bucket, upload an object, and configure a lifecycle rule.



\### Steps performed

1\. Created the S3 bucket `my-training-bucket-kusuma` in `us-east-1`.

2\. Uploaded a `runbook.md` object.

3\. Verified the bucket and object using the AWS CLI.

4\. Created a lifecycle rule named `archive-after-30-days`.

5\. Configured the rule to transition eligible objects to S3 Glacier Flexible Retrieval after 30 days.



\### Verification



```powershell

aws s3 ls s3://my-training-bucket-kusuma --region us-east-1

```



The object listing confirmed that the uploaded object was present.



\### Cleanup

Deleted the object and then deleted the bucket. The S3 console showed that the bucket had been deleted.



\*\*Learning:\*\* S3 stores objects in buckets. Lifecycle rules automate transitions between storage classes and can help manage storage costs. Glacier Flexible Retrieval has minimum storage-duration considerations, so lifecycle rules should be planned carefully.



\## 4. Lab 4.2 — Amazon RDS



\### Objective

Practice connecting to a managed relational database from an EC2 instance.



\### Configuration

\- DB instance identifier: `training-db`

\- Engine: MySQL 8.4

\- Database: `training\_data`

\- Region: `us-east-1`

\- Client instance: `week4-rds-client`



\### Network access

The RDS security group was configured to allow MySQL traffic on TCP port `3306` from the EC2 client's security group.



\*\*Security note:\*\* Database access should be restricted to trusted sources. Avoid opening port 3306 to the entire internet or including public IP addresses, passwords, or database credentials in GitHub documentation.



\### Steps performed

1\. Created the RDS MySQL instance.

2\. Connected from the EC2 instance using a MySQL client.

3\. Created the `training\_data` database.

4\. Inspected database tables and SQL schema.

5\. Attempted to work with the supplied property SQL dump.



\### Example connection command



Use your actual endpoint and credentials in the terminal. Never put a password in a GitHub runbook.



```bash

mysql -h YOUR\_RDS\_ENDPOINT -P 3306 -u YOUR\_DB\_USER -p

```



After connecting, the following SQL commands can be used:



```sql

CREATE DATABASE IF NOT EXISTS training\_data;

USE training\_data;

SHOW TABLES;

```



\### Import status and data handling

The SQL dump required schema adjustments, and the import did not complete reliably during the recorded lab work. Do not describe the full dataset as successfully imported unless you independently verify the final row count and table contents.



The source property dump contained sensitive personal and property-related information. Raw dumps, personal information, credentials, and unredacted datasets must not be committed to GitHub.



\*\*Learning:\*\* Amazon RDS manages the database infrastructure, while security groups control network access to the database.



\## 5. Lab 4.3 — Amazon DynamoDB



\### Objective

Create a NoSQL table and retrieve a record using the AWS CLI.



\### Configuration

\- Table: `Properties`

\- Partition key: `L\_ListingID`

\- Key type: String

\- Capacity mode: On-demand

\- Region: `us-east-1`



\### Steps performed

1\. Created the `Properties` table.

2\. Added a sample property item for testing.

3\. Attached an IAM role to the EC2 instance with limited DynamoDB permissions.

4\. Verified the AWS identity using STS.

5\. Retrieved the sample item using the AWS CLI.



\### Example retrieval command



```bash

aws dynamodb get-item \\

&#x20; --table-name Properties \\

&#x20; --key '{"L\_ListingID":{"S":"R100001"}}' \\

&#x20; --region us-east-1

```



The command returned the sample item when it was available in the table.



\### IAM permissions

The EC2 role was configured for limited access to the `Properties` table, including actions such as `GetItem`, `PutItem`, and `DescribeTable`.



\*\*Learning:\*\* DynamoDB is a managed NoSQL database. Its partition key identifies records, and IAM policies control which actions an identity can perform.



\## 6. Issues Encountered and Lessons Learned



\### Issue 1 — Network utility unavailable

A network testing command was not available on the EC2 instance.



\*\*Lesson:\*\* Not every utility is preinstalled on Amazon Linux. Check available tools and use an appropriate alternative.



\### Issue 2 — DynamoDB access denied

The EC2 instance initially lacked the required permissions.



\*\*Resolution:\*\* Attached an IAM role with the necessary DynamoDB permissions and tested the AWS identity.



\*\*Lesson:\*\* Prefer IAM roles for AWS workloads instead of storing long-term access keys on an instance.



\### Issue 3 — SQL import did not complete reliably

The database connection was interrupted during the import attempt.



\*\*Lesson:\*\* Verify database imports with table listings, row counts, and sample queries. Do not assume an import succeeded simply because a table exists.



\### Issue 4 — S3 cleanup

The object and bucket needed to be removed in the correct order.



\*\*Lesson:\*\* Clean up objects and lifecycle configurations before deleting buckets, and account for storage-class minimum-duration charges.



\## 7. Cleanup



The following cleanup actions were performed or initiated during the lab:



\- \*\*S3:\*\* Deleted the test object and bucket; the console showed successful deletion.

\- \*\*DynamoDB:\*\* Submitted deletion of the `Properties` table; verify that it reached the deleted state.

\- \*\*RDS:\*\* Initiated deletion of `training-db`; verify that the instance is fully deleted.

\- \*\*EC2:\*\* The temporary `week4-rds-client` instance was reported terminated; verify its final state.

\- \*\*IAM:\*\* Review the temporary `week4-dynamodb-ec2-role` and its policies. Remove them only if they are no longer needed.

\- \*\*Other billable resources:\*\* Check for retained EBS volumes, snapshots, RDS snapshots, Elastic IP addresses, and NAT gateways.



Do not delete the default VPC, subnets, or route tables as part of this cleanup.



\## 8. Evidence and Deliverables



Evidence collected during the lab included screenshots of:



\- DynamoDB table creation and the sample item

\- Successful DynamoDB `get-item` command

\- EC2 instance and IAM role configuration

\- S3 object upload and lifecycle rule

\- S3 bucket deletion



Include RDS connection and security-group screenshots if available. Screenshots should not expose passwords, access keys, sensitive records, or unnecessary personal information.



\### Deliverables

\- `week-04/decision-guide.md`

\- `week-04/runbook.md`

\- Supporting screenshots, if required by the internship handbook



\## 9. Summary



Week 4 provided hands-on practice with three AWS storage and database services:



\- \*\*Amazon S3:\*\* Object storage, lifecycle management, and cleanup

\- \*\*Amazon RDS:\*\* Managed MySQL connectivity and database fundamentals

\- \*\*Amazon DynamoDB:\*\* NoSQL table creation, IAM access, and item retrieval



The lab reinforced the importance of least-privilege access, data protection, verification, and cost-aware resource cleanup.



