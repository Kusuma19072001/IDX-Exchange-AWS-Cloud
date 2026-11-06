# PropertyLite Serverless API — cURL Collection

Base URL:
```bash
export API_BASE="https://wvdvmctrfd.execute-api.us-east-1.amazonaws.com"
```

## 1. Retrieve R100234 (Sacramento, $450,000)

```bash
curl -i "$API_BASE/properties/R100234"
```

## 2. Retrieve R100235 (Fresno, $395,000)

```bash
curl -i "$API_BASE/properties/R100235"
```

## 3. Retrieve R100236 (Sacramento, $299,000)

```bash
curl -i "$API_BASE/properties/R100236"
```

Each request uses HTTP GET and should return a JSON property record with HTTP
status 200. These expected values are based on the three sample records loaded
into the Properties table during this lab.

## 4. Test a missing listing ID

```bash
curl -i "$API_BASE/properties/DOES-NOT-EXIST"
```

The Lambda implementation in this folder returns HTTP 404 with a JSON message
when the item is not found. If your deployed Lambda still uses the original
handbook code without the 404 handling, DynamoDB's empty item will instead be
returned with HTTP 200.
