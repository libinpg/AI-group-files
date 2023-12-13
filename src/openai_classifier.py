import openai
import json
import os

def load_config(config_file='./config/config.json'):
    """
    从配置文件加载 OpenAI API 密钥。
    """
    if not os.path.exists(config_file):
        print(f"配置文件 {config_file} 不存在。")
        return None

    with open(config_file, 'r') as file:
        config = json.load(file)
    return config.get('openai_api_key', '')

def classify_content(content, config_file='./config/config.json'):
    """
    Classify the given content using OpenAI's GPT-3.5 API with the latest chat completion method.
    """
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        openai_api_key = config.get('openai_api_key')

        if not openai_api_key:
            print("API key not found. Please check the configuration file.")
            return None

        openai.api_key = openai_api_key

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or other appropriate model
            messages=[
                {"role": "system", "content": "You are an assistant who classifies files based on their content."},
                {"role": "user", "content": content}
            ]
        )
        return completion.choices[0].message['content']
    except Exception as e:
        print(f"Error in calling OpenAI API: {e}")
        return None
