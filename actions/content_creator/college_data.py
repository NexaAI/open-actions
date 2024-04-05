import requests

url = "http://api.data.gov/ed/collegescorecard/v1/schools"

params = {
    'api_key': 'UaCGXU28T1tPDng2fjBcj1yaCQTaJtRZbv2sUtDC',  
    'per_page': '2'  
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    if 'results' in data and data['results']:
        first_result = data['results'][0]

        if 'school' in first_result:
            school_data = first_result['school']
            print("\n'school' 数据结构:")
            for key, value in school_data.items():
                print(f"{key}: {type(value)}")
        else:
            print("'school' 字段不存在于数据中")
    else:
        print("无结果返回")
else:
    print("请求失败，状态码：", response.status_code)
