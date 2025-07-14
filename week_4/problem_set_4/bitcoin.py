import requests
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
try :
    num = float(sys.argv[1])
except:
    print("Command-line argument is not a number")
    sys.exit(1)

# 請將這裡換成你自己的 API 金鑰
API_KEY = "80c727faf5f8d056f20fc51332adb44f0efaf7e48779e2e3a485e21b2bc0fd9a"

# 設定網址與 headers
url = "https://rest.coincap.io/v3/assets/bitcoin"
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# 發送 GET 請求
response = requests.get(url, headers=headers)

# 檢查狀態碼並印出結果
if response.status_code == 200:
    data = response.json()
    #print("成功取得資料：")
    #print(data)
    data = data["data"]
    price_usd = float(data["priceUsd"])
    #print(f"priceUsd: {price_usd:.2f}")
    usd = price_usd * num
    print(f"${usd:,.4f}")
else:
    print(f"取得資料失敗，狀態碼：{response.status_code}")
    print(response.text)

