import requests
import json
import re
from ..utils.util import load_config, get_baiduqianfan_access_token, get_existing_folders
from ..prompts.stage1_prompt import CONCLUDE_DIRECTORY_PROMPT

def testApi(testContent, config_file='config\config.json'):
    """
    Classify the given content using the Llama-7B-chat model with a structured response format.
    """
    access_token = get_baiduqianfan_access_token()
    
    # try:
    response = send_request(testContent, access_token)
    # print(f"Response from Llama-7B-chat: {response}")
    responseText = parse_response(response)
    return responseText
    

def send_request(content, access_token):
    """
    Send a request to the Llama-7B-chat model with the provided content.
    """
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/llama_2_7b?access_token={access_token}"
    payload = json.dumps({
        "messages": [
            {"role": "user", "content": content}
        ]
    })
    headers = {'Content-Type': 'application/json'}
    return requests.request("POST", url, headers=headers, data=payload)

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
    result = testApi(test_content)
    print(f"Classification result: {result}")
