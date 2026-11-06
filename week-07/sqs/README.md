# Lab 7.2 — Amazon SQS and Dead-Letter Queue (DLQ)

## Objective

Implement an asynchronous message-processing workflow using Amazon Simple Queue Service (SQS) and a Dead-Letter Queue (DLQ).

The objective is to understand how SQS stores messages, handles repeated message deliveries, and moves messages that exceed the configured receive threshold into a separate queue for investigation.

## Architecture

```text
                Message Producer
                       |
                       v
              Amazon SQS
              property-queue
                       |
                 Message received
                       |
              Repeated receives
                       |
             Receive threshold reached
                       |
                       v
              Amazon SQS DLQ
               property-dlq
                       |
                       v
             Inspect failed messages
```

## AWS Configuration

| Component | Configuration |
|---|---|
| AWS Region | us-east-1 |
| Main queue | property-queue |
| Dead-letter queue | property-dlq |
| Queue type | Standard |
| Encryption | Amazon SQS key (SSE-SQS) |
| AWS Account ID | 211391213806 |

## Implementation Steps

### 1. Create the Dead-Letter Queue

Created a Standard SQS queue named `property-dlq`.

This queue serves as the destination for messages that exceed the permitted receive threshold in the main queue.

### 2. Create the Main Queue

Created another Standard SQS queue named `property-queue`.

Configured its redrive policy to use `property-dlq` as its Dead-Letter Queue.

### 3. Send a Sample Property Message

Sent a sample JSON message to the main queue:

```json
{
  "listing_id": "R100234",
  "city": "Sacramento",
  "status": "Active",
  "price": 450000
}
```

### 4. Test Message Reception

Used the SQS Send and receive messages console to retrieve the message multiple times.

Observed the receive count increasing during repeated polling.

### 5. Verify Dead-Letter Queue Behavior

After the configured receive threshold was exceeded, the message was moved from `property-queue` to `property-dlq`.

The main queue showed zero available messages, while the DLQ contained one message.

### 6. Inspect the DLQ Message

Verified the message body and metadata in the Dead-Letter Queue.

Observed results:

| Field | Result |
|---|---|
| Message ID | 399c4f2d-1be8-4550-8bc8-a26e32dfce56 |
| Listing ID | R100234 |
| City | Sacramento |
| Status | Active |
| Price | 450000 |
| Message size | 94 bytes |
| Receive count | 4 |

## Test Results

| Validation | Result |
|---|---|
| Main SQS queue created | Successful |
| DLQ created | Successful |
| Redrive configuration | Verified |
| Sample message sent | Successful |
| Repeated message reception | Observed |
| Message transferred to DLQ | Verified |
| Original message body inspected | Successful |
| Message metadata inspected | Successful |

## Key Learnings

- Amazon SQS provides reliable message queuing for decoupled application components.
- A Dead-Letter Queue isolates messages that cannot be successfully processed within the configured receive threshold.
- The redrive policy connects a source queue to its DLQ.
- The `ApproximateReceiveCount` attribute helps identify repeated message deliveries.
- DLQs help developers investigate problematic messages without losing them from the messaging workflow.
- Standard queues provide at-least-once message delivery, so consumers should be designed to handle duplicate messages.

## Deliverables

```text
week-07/
├── lambda/
├── postman/
├── screenshots/
│   ├── Queue creation evidence
│   ├── DLQ creation evidence
│   ├── Message delivery evidence
│   └── DLQ verification evidence
├── sqs/
│   └── README.md
├── README.md
└── curl-collection.md
```

## Lab Status

Lab 7.2 — Amazon SQS and Dead-Letter Queue implementation completed and verified through the AWS Management Console.

**Note:** This lab demonstrates DLQ behavior through controlled manual message-reception testing. It does not yet implement an application consumer or an automated message-processing failure workflow.