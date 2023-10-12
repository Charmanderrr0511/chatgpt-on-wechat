import requests
import schedule
import time
import json

# 您的微信公众号的AppID和AppSecret
app_id = "wx0f0ee60215bf86d3"
app_secret = "f53ea8167a6a468076300f8af7066d7a"
access_token = None

def get_stable_access_token():
    url = "https://api.weixin.qq.com/cgi-bin/token"
    params = {
        "grant_type": "client_credential",
        "appid": app_id,
        "secret": app_secret
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "access_token" in data:
        return data["access_token"]
    else:
        print("Failed to get stable access token:", data)
        return None
    
def create_custom_menu():
    access_token = get_stable_access_token()
    menu_data = {
        "button": [
            {
                "name": "体检信息",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "查看体检报告",
                        "url": "http://bg.kktijian.com/ReportSearch/Index?Login_YYBH=1070"
                    },
                    {
                        "type": "view",
                        "name": "体检排队",
                        "url" : "http://daojian.dtxd.com.cn/"

                    }

                ]
            },
            {
                "name" : "预约挂号",
                "sub_button":
                [
                    {
                        "name": "小程序按钮",
                        "type": "miniprogram",
                        "url": "http://mp.weixin.qq.com",
                        "appid": "wx0827f7b96e0f8948",
                        "pagepath": "/pages/index/index"
                    },
                    {
                        "type": "view",
                        "name": "住院流程",
                        "url" : "https://mp.weixin.qq.com/s/seZ5ENIx84ZoJUVP0EvTJQ"
                    },
                    {
                        "type": "view",
                        "name": "出院流程",
                        "url" : "https://mp.weixin.qq.com/s/VRIbTm6y_8emlIwHrFDCUA"
                    }
                ]
            },
            {
                "type": "view",
                "name": "北京专家",
                "url": "https://mp.weixin.qq.com/s/taOrv2wiSNECSi5Yhskxmg"
            }

        ]
    }
    # 使用 Unicode 字符来表示特殊字符
    menu_data_str = json.dumps(menu_data, ensure_ascii=False).encode('utf-8')
    
    create_menu_url = f"https://api.weixin.qq.com/cgi-bin/menu/create?access_token={access_token}"
    response = requests.post(create_menu_url, data=menu_data_str)
    if response.status_code == 200:
        print("自定义菜单创建成功！", response.text)
    else:
        print("自定义菜单创建失败：", response.text)

def update_menu_and_access_token():
    get_stable_access_token()  # 更新 Access Token
    create_custom_menu()  # 创建自定义菜单

# 每半小时更新一次自定义菜单和 Access Token
schedule.every(90).minutes.do(update_menu_and_access_token)

if __name__ == "__main__":
    get_stable_access_token()  # 获取初始 Access Token
    create_custom_menu()  # 初始创建自定义菜单
    while True:
        schedule.run_pending()
        time.sleep(1)

