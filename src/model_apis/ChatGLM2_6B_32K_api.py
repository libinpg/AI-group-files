import requests
import json
import re
from utils.utils import load_config, get_baiduqianfan_access_token, get_existing_folders
from prompts.stage1_prompt import CONCLUDE_DIRECTORY_PROMPT

def classify_content(content ,config_file='./config/config.json'):
    """
    Classify the given content using the ChatGLM2_6B_32K model with a structured response format.
    """
    openai_api_key, baidu_api_key, baidu_api_secret = load_config(config_file)
    if not baidu_api_key or not baidu_api_secret:
        print("API key or Secret key not found. Please check the configuration file.")
        return None

    access_token = get_baiduqianfan_access_token()

    # 将现有文件夹列表作为上下文信息
    # context = "Existing folders(你先需要分析这些文件夹名，看是不是和待分类文件相关，当现存文件夹的列表中有可以直接用的时候，你相当于一个简单的选择程序，选择对应的名字即可，原原本本的保留名字既可,简单说就是以已有的文件名为主): " + str(get_existing_folders(save_path)) + "."
    # print(context)
    prompt =  CONCLUDE_DIRECTORY_PROMPT.format(content)
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
