# Week 2 — IAM Policy

## S3UploaderOnly-kusuma

This policy follows the principle of least privilege by allowing only the S3 actions required for the lab.

### Allowed Actions

- `s3:PutObject` — allows the user to upload objects.
- `s3:GetObject` — allows the user to read or download objects.

### Resource Scope

The policy is restricted to:

`arn:aws:s3:::my-training-bucket-kusuma/*`

This means the permissions apply only to objects inside the specified training bucket.

### What Is Not Allowed

The policy does not include `s3:ListAllMyBuckets`.

When `aws s3 ls --profile s3test` was tested, AWS returned `AccessDenied`. This confirmed that the restricted user could not list all S3 buckets.

### Least Privilege

The policy grants only the permissions required for the S3 upload and download test instead of giving the user broad S3 or administrator permissions.
