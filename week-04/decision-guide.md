# Week 4 — AWS Storage and Database Decision Guide

| AWS Service | When to Use It |
|---|---|
| Amazon S3 | Use for scalable object storage, backups, logs, images, and files. |
| Amazon EBS | Use for persistent block storage attached to EC2 instances, such as boot volumes and database disks. |
| Amazon EFS | Use when multiple instances need shared, elastic file storage. |
| Amazon RDS | Use for managed relational databases that support SQL and structured tables. |
| Amazon DynamoDB | Use for managed NoSQL key-value and document databases that need fast access by key. |

## Key Takeaway

Choose the service based on the data model, access pattern, sharing requirements, and operational responsibilities. S3 stores objects, EBS provides block storage, EFS provides shared file storage, RDS manages relational databases, and DynamoDB manages NoSQL data.

