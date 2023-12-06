import requests

url = "https://server.luxpowertek.com/WManage/api/inverter/getInverterEnergyInfo?serialNum=1233022323"

headers = {
    'Cookie': 'JSESSIONID=D4D147C82616D55D90A5275F8A744DFD-n1',
    # 'Cookie': 'JSESSIONID=CBAFD977E00EC266BBF2E27956C70FDD-n1',
  # 'API-Key': 'YOUR_API_KEY'
}

response = requests.request("POST", url, headers=headers)

# print(response.text)
# Kiểm tra xem yêu cầu có thành công hay không
if response.status_code == 200:
    # Phân tích nội dung JSON từ phản hồi
    data = response.json()
    
    # Trích xuất giá trị của totalImportText
    # totalImportText = data.get('totalImportText')

    # In giá trị totalImportText
    print("totalImportText:", data)
else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
