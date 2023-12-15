import json
import requests

def load_config(config_file='config\config.json'):
    """
    Load the configuration for both OpenAI and Baidu models.
    """
    # try:
    with open(config_file, 'r') as file:
        config = json.load(file)
    
    print(config)
    # Load OpenAI API Key
    openai_api_key = config.get('openai', {}).get('openai_api_key')

    # Load Baidu API Key and Secret
    baidu_api_key = config.get('baidu_qianfan', {}).get('api_key')
    baidu_api_secret = config.get('baidu_qianfan', {}).get('api_secret')

    return openai_api_key, baidu_api_key, baidu_api_secret
    # except Exception as e:
    #     print(f"Error loading configuration: {e}")
    #     return None, None, None

def get_baiduqianfan_access_token():
    """
    Generate the authentication signature (Access Token) using API_KEY and SECRET_KEY.
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    openai_api_key, baidu_api_key, baidu_api_secret = load_config()
    if not baidu_api_key or not baidu_api_secret:
        print("API key or Secret key not found. Please check the configuration file.")
        return None
    params = {"grant_type": "client_credentials", "client_id": baidu_api_key, "client_secret": baidu_api_secret}
    response = requests.post(url, params=params).json()
    return response.get("access_token")
