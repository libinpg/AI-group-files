import json

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
