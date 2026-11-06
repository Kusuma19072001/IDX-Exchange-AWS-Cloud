## Lab 7.3 — Debugging API Gateway 500 Internal Server Errors

### Objective

Understand how to diagnose API Gateway HTTP 500 Internal Server Errors by inspecting AWS Lambda execution logs in Amazon CloudWatch.

### Diagnostic procedure

1. Open AWS Lambda and select the `get-property` function.
2. Navigate to Monitor → View CloudWatch logs.
3. Open the latest log stream under `/aws/lambda/get-property`.
4. Inspect the latest invocation for START, END, REPORT, and any ERROR or Traceback entries.
5. Identify the actual exception before making changes to Lambda code, IAM policies, or API Gateway configuration.

### Common failure scenarios

| Exception | Possible root cause | Corrective action |
|---|---|---|
| AccessDeniedException | Lambda execution role has an incorrect DynamoDB table ARN or insufficient permissions | Verify `dynamodb:GetItem` and the exact `Properties` table ARN |
| KeyError | Lambda cannot find the expected path parameter | Verify the route is `GET /properties/{id}` and inspect event parsing |
| ResourceNotFoundException | Incorrect table name or AWS Region | Verify the DynamoDB table and Lambda Region |

### Actual diagnostic findings

The existing Lambda function was inspected through CloudWatch Logs.

- Log group: `/aws/lambda/get-property`
- Lambda function: `get-property`
- Runtime shown in logs: Python 3.14
- Three invocations were observed.
- All three contained corresponding START, END, and REPORT entries.
- No visible AccessDeniedException, KeyError, or ResourceNotFoundException was identified.

### API verification

The deployed API endpoint was tested again:

`GET https://wvdvmctrfd.execute-api.us-east-1.amazonaws.com/properties/R100234`

**Result:** Successful JSON response containing the Sacramento property record.

This confirms that the existing API Gateway → Lambda → DynamoDB read path was functioning during the diagnostic investigation.

### Conclusion

Lab 7.3 demonstrated the CloudWatch-based troubleshooting process for Lambda-backed APIs.

No actual HTTP 500 failure was reproduced during this investigation, so no configuration changes or code fixes were necessary.

An actual failure-and-recovery scenario remains untested.

### Evidence

Screenshots are saved under `screenshots/`:

- `lab-7.3-cloudwatch-logs.png`
- `lab-7.3-api-success.png`