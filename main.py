# import json
import polars as pl
import base64
import io


def lambda_handler(event, context):
    # Parse the 'multipart/form-data' request and extract the file
    content_type = event["headers"]["content-type"]

    # Check if the content type is 'multipart/form-data'
    # If not, return a 400 Bad Request
    if content_type != "multipart/form-data":
        return {"statusCode": 400, "body": "Invalid Content-Type"}

    # Decode the base64 encoded file
    body_decoded = base64.b64decode(event["body"])
    body_as_file = io.BytesIO(body_decoded)

    # Read the Excel file into a DataFrame
    df = pl.read_excel(body_as_file)

    # Convert the DataFrame to JSON
    json_data = df.to_pandas().to_json(orient="records")

    return {"statusCode": 200, "body": json_data}
