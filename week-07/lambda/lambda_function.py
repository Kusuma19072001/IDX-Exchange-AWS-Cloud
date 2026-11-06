import json
import boto3
from decimal import Decimal

# DynamoDB client resource and Properties table
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Properties")


def decimal_converter(obj):
    """Convert DynamoDB Decimal values into JSON-compatible numbers."""
    if isinstance(obj, Decimal):
        # Preserve whole numbers as integers and fractional values as floats.
        if obj % 1 == 0:
            return int(obj)
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")


def lambda_handler(event, context):
    """Return one PropertyLite record identified by the URL path parameter."""
    try:
        path_parameters = event.get("pathParameters") or {}
        listing_id = path_parameters.get("id")

        if not listing_id:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"message": "Missing listing ID in path"})
            }

        response = table.get_item(
            Key={"L_ListingID": listing_id}
        )

        item = response.get("Item")
        if item is None:
            return {
                "statusCode": 404,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"message": "Property not found"})
            }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(item, default=decimal_converter)
        }

    except Exception:
        # The full exception is available in the Lambda/CloudWatch execution logs.
        print("Error while retrieving property")
        raise
