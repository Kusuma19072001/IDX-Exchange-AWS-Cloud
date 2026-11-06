# Week 7 — Serverless & Event-Driven Architecture

## Lab 7.1 — PropertyLite serverless read path

### Objective

Re-host the existing PropertyLite property-read operation using API Gateway,
AWS Lambda, and DynamoDB. The lab reuses the existing `Properties` table and
the cleaned sample records; it does not load data from the raw SQL export.

### Architecture

```mermaid
flowchart TD
    A[Client: Browser / Postman / cURL] -->|GET /properties/{id}| B[Amazon API Gateway]
    B -->|Invokes function with pathParameters.id| C[AWS Lambda: get-property]
    C -->|dynamodb:GetItem| D[(Amazon DynamoDB: Properties)]
    D -->|Property item| C
    C -->|HTTP 200 + JSON body| B
    B -->|JSON response| A
    C -.->|Execution logs| E[Amazon CloudWatch Logs]
    C -->|Assumes execution role| F[IAM role: get-property]
    F -->|GetItem on Properties table only| D
```

### AWS configuration

| Component | Configuration |
|---|---|
| Region | `us-east-1` |
| DynamoDB table | `Properties` |
| Partition key | `L_ListingID` (String) |
| Lambda function | `get-property` |
| Runtime | Python 3.12 |
| API | `propertylite-serverless-api` |
| API ID | `wvdvmctrfd` |
| Stage | `$default` |
| Route | `GET /properties/{id}` |
| Integration | Lambda `get-property` |
| Invoke URL | `https://wvdvmctrfd.execute-api.us-east-1.amazonaws.com` |

### Request example

```http
GET https://wvdvmctrfd.execute-api.us-east-1.amazonaws.com/properties/R100234
```

The Lambda function reads the `id` path parameter, calls DynamoDB `GetItem`
using `L_ListingID`, and serializes the returned item as JSON.

### Sample data used for validation

| Listing ID | City | Status | System price |
|---|---|---|---:|
| `R100234` | Sacramento | Active | 450000 |
| `R100235` | Fresno | Active | 395000 |
| `R100236` | Sacramento | Pending | 299000 |

### IAM least-privilege design

The Lambda execution role needs CloudWatch Logs permissions and only the
DynamoDB read action required by this function. The custom policy should allow
`dynamodb:GetItem` on the exact table ARN:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["dynamodb:GetItem"],
      "Resource": "arn:aws:dynamodb:us-east-1:211391213806:table/Properties"
    }
  ]
}
```

The account ID above is the one shown in the lab's Lambda error/role context.
Verify the ARN in your own AWS account before reusing this policy elsewhere.
Do not attach broad DynamoDB permissions when a table-scoped permission is
sufficient.

### Test results

The Lambda console test succeeded for `R100234` with status code `200`.
The browser request to the deployed API also returned the Sacramento record
with listing ID `R100234`, status `Active`, and system price `450000`.

Run the commands in [`curl-collection.md`](curl-collection.md) to validate the
other two records. Save your own screenshots in the `screenshots/` folder.

### Troubleshooting

If API Gateway returns `{"message":"Internal Server Error"}`:

1. Open Lambda → `get-property` → Monitor → View CloudWatch logs.
2. Inspect the newest invocation's stack trace.
3. For `AccessDeniedException`, verify the execution role policy action and
   exact `Properties` table ARN.
4. For `KeyError` or a missing path parameter, verify the API route is exactly
   `GET /properties/{id}` and that the code reads `pathParameters.id`.
5. For `ResourceNotFoundException`, verify the table name and AWS Region.

The API response alone does not provide the full Lambda stack trace; CloudWatch
Logs is the first diagnostic step.

### Deliverable structure

```text
week-07/
├── README.md
├── curl-collection.md
├── lambda/
│   └── lambda_function.py
├── postman/
│   └── README.md
└── screenshots/
    └── (add AWS console and successful API test screenshots)
```

### Important

This folder documents Lab 7.1. Lab 7.2 (SQS with a dead-letter queue) should
be documented separately after completing and validating that exercise.
