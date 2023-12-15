import requests
import json
import re
def load_config(config_file='./config/config.json'):
    """
    Load API_KEY and SECRET_KEY from the configuration file.
    """
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config.get('api_key'), config.get('secret_key')
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return None, None

def classify_content(content, config_file='./config/config.json'):
    """
    Classify the given content using the ChatGLM2_6B_32K model with a structured response format.
    """
    API_KEY, SECRET_KEY = load_config(config_file)
    if not API_KEY or not SECRET_KEY:
        print("API key or Secret key not found. Please check the configuration file.")
        return None

    access_token = get_access_token()

    prompt = f"You are a file organizing assistant. Based on this content, suggest a concise, valid folder name. this is content: '{content}'. Please format the response like {{folder_name}}, which means that your response should be enclosed within single braces"
    try:
        response = send_request(prompt, access_token)
        responseText = parse_response(response)
        print(f"Response from ChatGLM2_6B_32K: {responseText}")
        # Use regex to extract content within {{folder_name}}
        match = re.search(r'\{(.+?)\}', responseText)
        if match:
            folder_name = match.group(1).strip()
            # Further sanitize and shorten the folder name if necessary
            folder_name = re.sub(r'[^\w\s-]', '', folder_name)
            # folder_name = folder_name[:15].rstrip()
            return folder_name
        else:
            print("No valid folder name format found in the response.")
            return None

    except Exception as e:
        print(f"Error in calling ChatGLM2_6B_32K API: {e}")
        return None

def send_request(content, access_token):
    """
    Send a request to the ChatGLM2_6B_32K model with the provided content.
    """
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/chatglm2_6b_32k?access_token={access_token}"
    payload = json.dumps({
        "messages": [
            {"role": "user", "content": content}
        ]
    })
    headers = {'Content-Type': 'application/json'}
    return requests.request("POST", url, headers=headers, data=payload)

def get_access_token():
    """
    Generate the authentication signature (Access Token) using API_KEY and SECRET_KEY.
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    API_KEY, SECRET_KEY = load_config()
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    response = requests.post(url, params=params).json()
    return response.get("access_token")

def parse_response(response):
    """
    Parse the response from the ChatGLM2_6B_32K model.
    """
    if response.status_code != 200:
        print(f"API request failed with status code: {response.status_code}")
        return None
    
    response_data = response.json()
    # Extract and return the relevant part of the response
    # Modify the below line based on the actual response structure
    return response_data.get("result", {})

if __name__ == '__main__':
    test_content = "Your test content here"
    result = classify_content(test_content)
    print(f"Classification result: {result}")