import requests
import json
import re
from ..utils.util import load_config, get_baiduqianfan_access_token, get_existing_folders
from ..prompts.stage1_prompt import CONCLUDE_DIRECTORY_PROMPT
from ..prompts.stage2_prompt import CLASSIFY_FILE_PROMPT
from ..utils.util import read_ai_reply_from_file

def classify_content(content, config_file='config\config.json'):
    """
    Classify the given content using the Baichuan2-13b-chat-v1 model.
    """
    prompt = CLASSIFY_FILE_PROMPT.format(content, read_ai_reply_from_file(r'src/data/directoryconclusion.txt'))
    print(f"Prompt for baichuan2_7B: {prompt}")
    response = send_request(prompt,config_file)
    responseText = parse_response(response)
    print(f"Response text from Baichuan2-13b-chat-v1: {responseText}")
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
    return responseText

def send_request(content,config_file):
    """
    Send a request to the Baichuan2-13b-chat-v1 model with the provided content.
    """
    config_file='config\config.json'
    with open(config_file, 'r') as file:
            config = json.load(file)
        
    # print(config)
    # Load dashscope API Key
    api_key = config.get('dashscope', {}).get('api_key')
    url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "model": "baichuan2-13b-chat-v1",
        "input": {
            "messages":[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": content
                }
            ]
        },
        "parameters": {
            "result_format": "message"
        }
    })
    return requests.request("POST", url, headers=headers, data=payload)

def parse_response(response):
    """
    Parse the response from the Baichuan2-13b-chat-v1 model.
    """
    if response.status_code != 200:
        print(f"API request failed with status code: {response.status_code}")
        return None

    response_data = response.json()
    return response_data.get("output", {}).get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == '__main__':
    test_content = "你好，请介绍一下故宫"
    result = classify_content(test_content)
    print(f"Classification result: {result}")
