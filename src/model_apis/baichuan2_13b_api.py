import requests
import json
import re
from ..utils.util import load_config, get_baiduqianfan_access_token, get_existing_folders
from ..prompts.stage1_prompt import CONCLUDE_DIRECTORY_PROMPT

def testApi(testContent, config_file='config\config.json'):
    """
    Classify the given content using the Llama-7B-chat model with a structured response format.
    """
    response = send_request(testContent,config_file)
    responseText = parse_response(response)
    print("responseText: ", responseText)
    return responseText
    
def send_request(content,config_file):
    """
    Send a request to the Baichuan2-13b-chat-v1 model with the provided content.
    """
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
    test_content = "Your test content here"
    result = testApi(test_content)
    print(f"Classification result: {result}")
