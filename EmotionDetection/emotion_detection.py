import requests

def emotion_detector(text_to_analyze):

    # URL and headers for the API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # Input JSON
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()  # Raise an error for HTTP status codes 4xx/5xx

        # Parse and return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle exceptions such as connection errors or timeouts
        return {"error": str(e)}
        
    formatted_result = json.dumps(result, indent=4)
    print(formatted_result)
    return result