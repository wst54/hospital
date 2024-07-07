import requests

app_id = "89935683"
api_key = "cYHV9mnN214t9S8PvbPSPlSw"
secret_key = "cu0hsJAVVzaSUVCpPCKrSfvBTOoHJRcu"


'''
获取access_token，每次的access_token都不一样
'''
def get_access_token():
    # 获取token的URL
    token_url = "https://aip.baidubce.com/oauth/2.0/token"
    # 构造请求数据
    data = {
        "grant_type": "client_credentials",
        "client_id": api_key,
        "client_secret": secret_key
    }
    # 发送POST请求获取token
    response = requests.post(token_url, data=data)
    # 解析响应内容
    if response.ok:
        # 解析为JOSN格式，获得获取access_token
        result = response.json()
        access_token = result.get('access_token')
        # 检查是否成功获取了访问令牌
        if access_token:
            return access_token
        else:
            raise ValueError("Failed to retrieve access token")
    else:
        response.raise_for_status()