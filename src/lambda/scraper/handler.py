import json
import requests
from bs4 import BeautifulSoup


def lambda_handler(event, context):
    try:
        # Extract the URL from the event data
        url = event.get("url", None)  # Default to None if not provided

        if not url:
            return {
                'statusCode': 400,
                'body': json.dumps("No URL provided")
            }

        response = requests.get(url)

        if response.status_code == 200:
            return {
                'statusCode': 200,
                'body': json.dumps(response.text)
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': json.dumps("Status code is not OK")
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"An error occurred: {str(e)}")
        }
