import openai
import json
import os
import re
import time

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
    Classify the given content using OpenAI's GPT-3.5 API with rate limit handling.
    """
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        openai_api_key = config.get('openai_api_key')

        if not openai_api_key:
            print("API key not found. Please check the configuration file.")
            return None

        openai.api_key = openai_api_key

        prompt = f"Classify this content and suggest a short, valid folder name:\nContent: {content}\nFolder Name:"
        for attempt in range(3):  # Retry up to 3 times
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": prompt}
                    ]
                )
                folder_name = completion.choices[0].message['content']
                break  # Break the loop if successful
            except openai.error.RateLimitError:
                if attempt < 2:  # Wait only if more attempts are left
                    time.sleep(20)  # Wait for 20 seconds before retrying
                else:
                    raise  # Raise the exception if out of attempts

        folder_name = re.sub(r'[^\w\s-]', '', folder_name).strip()
        folder_name = folder_name[:15].rstrip()
        return folder_name

    except Exception as e:
        print(f"Error in calling OpenAI API: {e}")
        return None
