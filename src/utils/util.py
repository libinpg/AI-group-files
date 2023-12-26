import json
import requests
import os

def load_config(config_file='config\config.json'):
    """
    Load the configuration for both OpenAI and Baidu models.
    """
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        
        # print(config)
        # Load OpenAI API Key
        openai_api_key = config.get('openai', {}).get('openai_api_key')

        # Load Baidu API Key and Secret
        baidu_api_key = config.get('baidu_qianfan', {}).get('api_key')
        baidu_api_secret = config.get('baidu_qianfan', {}).get('api_secret')
    
        return openai_api_key, baidu_api_key, baidu_api_secret
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return None, None, None

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

def get_existing_folders(directory):
    print(f"Getting existing folders in {directory}")
    """ 获取给定目录中的所有文件夹名称 """
    return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

# 编写一个将string类型的ai reply写入到给定路径的函数
def write_ai_reply_to_file(ai_reply, save_path):
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(ai_reply)
        f.close()
        print(f"AI reply has been written to {save_path}")
        
# 编写一个读取指定路径的ai reply文件的函数
def read_ai_reply_from_file(ai_reply_path):
    with open(ai_reply_path, 'r',encoding='utf-8') as f:
        ai_reply = f.read()
        f.close()
        print(f"AI reply has been read from {ai_reply_path}")
        return ai_reply
