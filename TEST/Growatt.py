import growattServer

api = growattServer.GrowattApi()
login_response = api.login("CDT_TNUT", "Cdt@12345")
data = api.plant_list(login_response['user']['id'])['data']
plant_ids = int(data[0]["plantId"])
print(plant_ids)
print(' ==> ', api.plant_info(plant_ids))
API = api.plant_info(plant_ids)
totalMoneyText = API['totalMoneyText']
print(totalMoneyText)
print(api.inverter_list(plant_ids))


# import requests

# def login_to_growatt():
#     # Define the login URL
#     login_url = "https://server.growatt.com/login"

#     # Define the login credentials
#     payload = {
#         "account": "USER_NAME",
#         "password": "PASSWORD",
#     }

#     # Define user agent for the request headers
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#     }

#     # Create a session and set the headers
#     session = requests.Session()
#     session.headers.update(headers)

#     # Send the POST request to login
#     response = session.post(login_url, data=payload)

#     # Check the response status code
#     if response.status_code == 200:
#         return session
#     else:
#         print(f"Login Failed. Status Code: {response.status_code}")



# def getInvTotalData():
#     session = login_to_growatt()
#     payload = {
#         "plantId": "2283430"
#     }
#     response_get_inv_total_data = session.post("https://server.growatt.com/indexbC/inv/getInvTotalData", data=payload)
#     if response_get_inv_total_data.status_code == 200:
#         response_json = response_get_inv_total_data.json()
#         print(response_json)
#     else:
#         print(f"Failed to retrieve data. Status Code: {response_get_inv_total_data.status_code}")


# getInvTotalData()
