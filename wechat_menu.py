import requests
import json

def create_menu():
    appid = "wxf873a70dfb7d4518" # 替换为你的AppID
    appsecret = "2db6a473b0fe0e62be1512a74ec968f1"
    url_accessToken = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={appsecret}"
    response = requests.get(url_accessToken)
    
    if response.status_code == 200:
        data = response.json()
        access_token = data.get("access_token")
        expires_in = data.get("expires_in")
        print(access_token, expires_in)
    else:
        print("请求失败，状态码：", response.status_code)
        return None, None
    
    url = f"https://api.weixin.qq.com/cgi-bin/menu/create?access_token={access_token}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "button": [
            {
                "type": "click",
                "name": "菜单1",
                "key": "menu1"
            },
            {
                "name": "菜单2",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "子菜单1",
                        "url": "http://example.com"
                    },
                    {
                        "type": "click",
                        "name": "子菜单2",
                        "key": "submenu2"
                    }
                ]
            }
        ]
    }
    json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
    response = requests.post(url, data=json_data, headers=headers)
    
    if response.status_code == 200:
        print("菜单创建成功")
    else:
        print("菜单创建失败")

if __name__ == '__main__':
    create_menu()
