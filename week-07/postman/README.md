# Postman setup

Create a Postman collection named **PropertyLite Serverless API**.

Add these requests:

| Request | Method | URL |
|---|---|---|
| Get Sacramento property | GET | `{{baseUrl}}/properties/R100234` |
| Get Fresno property | GET | `{{baseUrl}}/properties/R100235` |
| Get second Sacramento property | GET | `{{baseUrl}}/properties/R100236` |

Create a collection variable:

- `baseUrl` = `https://wvdvmctrfd.execute-api.us-east-1.amazonaws.com`

For each request, select **Send** and verify that the response status is 200
and the returned `L_ListingID` matches the ID in the request URL.

The equivalent cURL commands are in the parent folder's
[`curl-collection.md`](../curl-collection.md).
