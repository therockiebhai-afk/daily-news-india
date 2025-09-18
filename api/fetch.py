import os
import requests
import json

def handler(request):
    api_key = os.environ.get("NEWSDATA_API_KEY")
    if not api_key:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "API key not set in Vercel environment"})
        }

    url = f"https://newsdata.io/api/1/news?apikey={api_key}&country=in&language=en&category=top"

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(data)
        }
    except Exception as e:
        return {
            "statusCode": 502,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
