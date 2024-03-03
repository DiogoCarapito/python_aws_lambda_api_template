import base64
import io
import pandas as pd

# import polars as pl
from main import lambda_handler


def test_lambda_handler():
    # Create a DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})

    # Convert the DataFrame to an Excel file in memory
    excel_file = io.BytesIO()
    df.to_excel(excel_file, index=False, engine="openpyxl")
    excel_file.seek(0)

    # Create a base64 encoded string of the Excel file
    encoded_string = base64.b64encode(excel_file.read()).decode("utf-8")

    # Create an event with the base64 encoded string as the body
    event = {"headers": {"content-type": "multipart/form-data"}, "body": encoded_string}

    # Call the lambda_handler function with the event
    result = lambda_handler(event, "")

    # Check that the status code is 200
    assert result["statusCode"] == 200

    # Check that the body is the JSON representation of the DataFrame
    expected_body = df.to_json(orient="records")
    assert result["body"] == expected_body
