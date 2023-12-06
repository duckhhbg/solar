from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Manager_Model, Info_getTotalData, Info_getPlantEnergyList, Info_getWeatherByPlantId, Info_getInvStatusData, Info_getInvTotalData, Info_getInvEnergyDayChart, Info_getInvEnergyMonthChart, Info_getInvEnergyYearChart
import snap7
import datetime
import json
import requests

from django.db.models import Sum
from django.utils import timezone

# Create your views here.
def login_to_growatt():
    # xác định URL đăng nhập
    login_url = "https://server.growatt.com/login"

    # Xác định thông tin đăng nhập
    payload = {
        "account": "CDT_TNUT",
        "password": "Cdt@12345",
    }

    # Xác đinh Header, thể hiện rằng yêu cầu HTTP này được gửi từ một trình duyệt giả mạo, cụ thể là một trình duyệt giả mạo mô phỏng Chrome (58.0.3029.110) trên một máy tính chạy Windows (Windows NT 10.0; Win64; x64).
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    }

    # Tạo một phiên và đặt tiêu đề
    session = requests.Session()
    session.headers.update(headers)

    # Gửi yêu cầu POST và tự động xử lý cookie
    response = session.post(login_url, data=payload)

    # Kiểm tra phiên đăng nhập có thành công hay không
    if response.status_code == 200:
        return session
    else:
        print(f"Login Failed. Status Code: {response.status_code}")

def Save_Data():
    now = datetime.datetime.now()
    format_datetime = now.strftime("%Y-%m-%d")
    session = login_to_growatt()

    payload = {
        "plantId": "2283430"
    }
    response_getTotalData = session.post("https://server.growatt.com/indexbC/getTotalData", data=payload)
    if response_getTotalData.status_code == 200:
        response_json = response_getTotalData.json()
        save_day = format_datetime
        TotalData_mTotal = response_json['obj']['mTotal']
        TotalData_mToday = response_json['obj']['mToday']
        TotalData_co2 = response_json['obj']['co2']
        response_getTotalData = json.loads(response_getTotalData.content)
        TotalData_onlineNum = response_getTotalData['obj']['onlineNum']
        TotalData_eMonth = response_getTotalData['obj']['eMonth']
        TotalData_pac = response_getTotalData['obj']['pac']
        TotalData_lostNum = response_getTotalData['obj']['lostNum']
        TotalData_waitNum = response_getTotalData['obj']['waitNum']
        TotalData_mMonth = response_getTotalData['obj']['mMonth']
        TotalData_nominalPower = response_getTotalData['obj']['nominalPower']
        TotalData_eToday = response_getTotalData['obj']['eToday']
        TotalData_eTotal = response_getTotalData['obj']['eTotal']
        TotalData_coa = response_getTotalData['obj']['coa']
        TotalData_gridDate = response_getTotalData['obj']['gridDate']
        TotalData_runDay = response_getTotalData['obj']['runDay']

        # Kiểm tra xem dữ liệu đã tồn tại cho ngày này chưa
        existing_data = Info_getTotalData.objects.filter(save_day=save_day).first()
        if existing_data:
        # Nếu đã tồn tại, xóa dữ liệu cũ
            existing_data.delete()
        Info_getTotalData.objects.create(
            save_day=save_day,
            TotalData_mTotal=TotalData_mTotal,
            TotalData_mToday=TotalData_mToday,
            TotalData_co2=TotalData_co2,
            TotalData_onlineNum=TotalData_onlineNum,
            TotalData_eMonth=TotalData_eMonth,
            TotalData_pac=TotalData_pac,
            TotalData_lostNum=TotalData_lostNum,
            TotalData_waitNum=TotalData_waitNum,
            TotalData_mMonth=TotalData_mMonth,
            TotalData_nominalPower=TotalData_nominalPower,
            TotalData_eToday=TotalData_eToday,
            TotalData_eTotal=TotalData_eTotal,
            TotalData_coa=TotalData_coa,
            TotalData_gridDate=TotalData_gridDate,
            TotalData_runDay=TotalData_runDay
        )
        print("Info_getTotalData đã xong")
    else:
        print(f"Failed to retrieve data. Status Code: {response_getTotalData.status_code}")
    
    response_getWeatherByPlantId = session.post("https://server.growatt.com/indexbC/getWeatherByPlantId", data=payload)
    if response_getWeatherByPlantId.status_code == 200:
        response_json = response_getWeatherByPlantId.json()
        save_day = format_datetime
        WeatherByPlantId_parent_city = response_json['obj']['data']['HeWeather6'][0]['basic']['parent_city']
        WeatherByPlantId_cloud = response_json['obj']['data']['HeWeather6'][0]['now']['cloud']
        WeatherByPlantId_hum = response_json['obj']['data']['HeWeather6'][0]['now']['hum']
        WeatherByPlantId_wind_deg = response_json['obj']['data']['HeWeather6'][0]['now']['wind_deg']
        WeatherByPlantId_pres = response_json['obj']['data']['HeWeather6'][0]['now']['pres']
        WeatherByPlantId_fl = response_json['obj']['data']['HeWeather6'][0]['now']['fl']
        WeatherByPlantId_tmp = response_json['obj']['data']['HeWeather6'][0]['now']['tmp']
        WeatherByPlantId_wind_sc = response_json['obj']['data']['HeWeather6'][0]['now']['wind_sc']
        WeatherByPlantId_wind_spd = response_json['obj']['data']['HeWeather6'][0]['now']['wind_spd']
        # Kiểm tra xem dữ liệu đã tồn tại cho ngày này chưa
        existing_data = Info_getWeatherByPlantId.objects.filter(save_day=save_day).first()
        if existing_data:
        # Nếu đã tồn tại, xóa dữ liệu cũ
            existing_data.delete()
        Info_getWeatherByPlantId.objects.create(
            save_day=save_day,
            WeatherByPlantId_parent_city=WeatherByPlantId_parent_city,
            WeatherByPlantId_cloud=WeatherByPlantId_cloud,
            WeatherByPlantId_hum=WeatherByPlantId_hum,
            WeatherByPlantId_wind_deg=WeatherByPlantId_wind_deg,
            WeatherByPlantId_pres=WeatherByPlantId_pres,
            WeatherByPlantId_fl=WeatherByPlantId_fl,
            WeatherByPlantId_tmp=WeatherByPlantId_tmp,
            WeatherByPlantId_wind_sc=WeatherByPlantId_wind_sc,
            WeatherByPlantId_wind_spd=WeatherByPlantId_wind_spd
        )
        print("Info_getWeatherByPlantId đã xong")
    else:
        print(f"Failed to retrieve data. Status Code: {response_getWeatherByPlantId.status_code}")

    response_getInvStatusData = session.post("https://server.growatt.com/indexbC/inv/getInvStatusData", data=payload)
    if response_getInvStatusData.status_code == 200:
        response_json = response_getInvStatusData.json()
        save_day = format_datetime
        InvStatusData_pac = response_json['obj']['pac']
        InvStatusData_subarrayNum = response_json['obj']['subarrayNum']
        InvStatusData_subarrayShowType = response_json['obj']['subarrayShowType']
        # Kiểm tra xem dữ liệu đã tồn tại cho ngày này chưa
        existing_data = Info_getInvStatusData.objects.filter(save_day=save_day).first()
        if existing_data:
        # Nếu đã tồn tại, xóa dữ liệu cũ
            existing_data.delete()
        Info_getInvStatusData.objects.create(
            save_day=save_day,
            InvStatusData_pac=InvStatusData_pac,
            InvStatusData_subarrayNum=InvStatusData_subarrayNum,
            InvStatusData_subarrayShowType=InvStatusData_subarrayShowType
        )
        print("Info_getInvStatusData đã xong")
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvStatusData.status_code}")
    
    response_getInvTotalData = session.post("https://server.growatt.com/indexbC/inv/getInvTotalData", data=payload)
    if response_getInvTotalData.status_code == 200:
        response_json = response_getInvTotalData.json()
        save_day = format_datetime
        InvTotalData_epvToday = response_json['obj']['epvToday']
        InvTotalData_epvTotal = response_json['obj']['epvTotal']
        InvTotalData_pac = response_json['obj']['pac']
        # Kiểm tra xem dữ liệu đã tồn tại cho ngày này chưa
        existing_data = Info_getInvTotalData.objects.filter(save_day=save_day).first()
        if existing_data:
        # Nếu đã tồn tại, xóa dữ liệu cũ
            existing_data.delete()
        Info_getInvTotalData.objects.create(
            save_day=save_day,
            InvTotalData_epvToday=InvTotalData_epvToday,
            InvTotalData_epvTotal=InvTotalData_epvTotal,
            InvTotalData_pac=InvTotalData_pac
        )
        print("Info_getInvTotalData đã xong")
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvTotalData.status_code}")
    
    payload = {
        "plantId": "2283430",
        "date": format_datetime
    }
    response_getInvEnergyDayChart = session.post("https://server.growatt.com/indexbC/inv/getInvEnergyDayChart", data=payload)
    if response_getInvEnergyDayChart.status_code == 200:
        response_json = response_getInvEnergyDayChart.json()
        save_day = format_datetime
        inv_energyDay_data = response_json['obj']['pac']
        # Kiểm tra xem dữ liệu đã tồn tại cho ngày này chưa
        existing_data = Info_getInvEnergyDayChart.objects.filter(save_day=save_day).first()
        if existing_data:
        # Nếu đã tồn tại, xóa dữ liệu cũ
            existing_data.delete()
        Info_getInvEnergyDayChart.objects.create(
            save_day=save_day,
            inv_energyDay_data=inv_energyDay_data
        )
        print("Info_getInvEnergyDayChart đã xong")
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvEnergyDayChart.status_code}")
    
    payload = {
        "plantId": "2283430",
        "date": now.strftime("%Y-%m")
    }
    response_getInvEnergyMonthChart = session.post("https://server.growatt.com/indexbC/inv/getInvEnergyMonthChart", data=payload)
    if response_getInvEnergyMonthChart.status_code == 200:
        response_json = response_getInvEnergyMonthChart.json()
        save_month = now.strftime("%m")
        inv_energyMonth_data = response_json['obj']['energy']
        # Kiểm tra xem dữ liệu đã tồn tại cho ngày này chưa
        existing_data = Info_getInvEnergyMonthChart.objects.filter(save_month=save_month).first()
        if existing_data:
        # Nếu đã tồn tại, xóa dữ liệu cũ
            existing_data.delete()
        Info_getInvEnergyMonthChart.objects.create(
            save_month=save_month,
            inv_energyMonth_data=inv_energyMonth_data
        )
        print("Info_getInvEnergyMonthChart đã xong")
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvEnergyMonthChart.status_code}")
    
    payload = {
        "plantId": "2283430",
        "date": now.strftime("%Y")
    }
    response_getInvEnergyYearChart = session.post("https://server.growatt.com/indexbC/inv/getInvEnergyYearChart", data=payload)
    if response_getInvEnergyYearChart.status_code == 200:
        response_json = response_getInvEnergyYearChart.json()
        year = now.strftime("%Y")
        inv_energyYear_data = response_json['obj']['energy']
        # Kiểm tra xem dữ liệu đã tồn tại cho ngày này chưa
        existing_data = Info_getInvEnergyYearChart.objects.filter(year=year).first()
        if existing_data:
        # Nếu đã tồn tại, xóa dữ liệu cũ
            existing_data.delete()
        Info_getInvEnergyYearChart.objects.create(
            year=year,
            inv_energyYear_data=inv_energyYear_data
        )
        print("Info_getInvEnergyYearChart đã xong")
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvEnergyYearChart.status_code}")
    
    payload = {
        "plantId": "2283430",
        "date": now.strftime("%Y-%m"),
        "currPage": 1,
        "pageSize": 20,
        "type":1
    }
    response_getPlantEnergyList = session.post("https://server.growatt.com/logbC/energyReport/getPlantEnergyList", data=payload)
    if response_getPlantEnergyList.status_code == 200:
        response_json = response_getPlantEnergyList.json()
        # print(response_json)
        nominalPower = response_json['obj']['datas'][0]['nominalPower']
        income = response_json['obj']['datas'][0]['income']
        date = response_json['obj']['datas'][0]['date']
        c02 = response_json['obj']['datas'][0]['c02']
        userLoad = response_json['obj']['datas'][0]['userLoad']
        pacToUser = response_json['obj']['datas'][0]['pacToUser']
        energy = response_json['obj']['datas'][0]['energy']
        # print(pacToUser)

        # Kiểm tra xem dữ liệu đã tồn tại cho ngày này chưa
        existing_data = Info_getPlantEnergyList.objects.filter(date=date).first()
        if existing_data:
        # Nếu đã tồn tại, xóa dữ liệu cũ
            existing_data.delete()
        Info_getPlantEnergyList.objects.create(
            nominalPower=nominalPower,
            income=income,
            date=date,
            c02=c02,
            userLoad=userLoad,
            pacToUser=pacToUser,
            energy=energy
        )
        print("Info_getPlantEnergyList đã xong")
    else:
        print(f"Failed to retrieve data. Status Code: {response_getPlantEnergyList.status_code}")
    

def Not_Login(req):
    return redirect('/')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('User_Name')
            Password = request.POST.get('Password')
            # global user
            user = authenticate(username=username, password=Password)
            if user is not None:
                # Kiểm tra điều kiện hợp lệ ==> Đăng nhập thành công
                login(request, user)
                Save_Data()
                filtered_data = Manager_Model.objects.all().filter(userName=user)
                # return redirect('/index_HTML')
                return render(request, 'index.html', {'filter':filtered_data, 'user': user})
            else:
                try:
                    # Kiểm tra điều kiện tên người dùng nhập vào có tồn tại hay không
                    User.objects.get(username=username)
                    # Nếu người dùng có tồn tại, nhưng mật khẩu sai ==> Reload lại trang web để người dùng đăng nhập lại
                    messages.error(request, "Sai thông tin đăng nhập!!!!")
                    return redirect('/')
                except User.DoesNotExist:
                    messages.error(request, "Không tồn tại tài khoản này")
                    return redirect('/')

def index_HTML(request):
    Month = str(datetime.datetime.now().month)
    session = login_to_growatt()
    payload = {
        "plantId": "2283430"
    }
    response_getInvTotalData = session.post("https://server.growatt.com/indexbC/inv/getInvTotalData", data=payload)
    if response_getInvTotalData.status_code == 200:
        response_json = response_getInvTotalData.json()
        epvToday = response_json['obj']['epvToday']
    else:
        print(f"Lỗi lấy dữ liệu từ getInvTotalData: {response_getInvTotalData.status_code}")
        
    response_getTotalData = session.post("https://server.growatt.com/indexbC/getTotalData", data=payload)
    if response_getTotalData.status_code == 200:
        response_json = response_getTotalData.json()
        response_getTotalData = json.loads(response_getTotalData.content)
        eMonth = response_getTotalData['obj']['eMonth']
    else:
        print(f"Lỗi lấy dữ liệu từ getTotalData: {response_getInvTotalData.status_code}")
    
    now = datetime.datetime.now()
    payload = {
        "plantId": "2283430",
        "date": now.strftime("%Y-%m"),
        "currPage": 1,
        "pageSize": 20,
        "type":1
    }
    response_getPlantEnergyList = session.post("https://server.growatt.com/logbC/energyReport/getPlantEnergyList", data=payload)
    if response_getPlantEnergyList.status_code == 200:
        response_json = response_getPlantEnergyList.json()
        pacToUser = response_json['obj']['datas'][0]['pacToUser']
    else:
        print(f"Lỗi lấy dữ liệu từ getPlantEnergyList: {response_getPlantEnergyList.status_code}")

    # Lấy ngày đầu tiên và cuối cùng trong tháng hiện tại
    today = timezone.now()
    first_day_of_month = today.replace(day=1)
    last_day_of_month = first_day_of_month.replace(year=first_day_of_month.year + 1, month=first_day_of_month.month % 12 + 1, day=1) - timezone.timedelta(days=1)
    # # Lọc các bản ghi trong cùng một tháng
    records_in_month = Info_getPlantEnergyList.objects.filter(date__gte=first_day_of_month, date__lte=last_day_of_month)

    # # Tính tổng của trường pacToUser
    total_pac_to_user = records_in_month.aggregate(total_pac=Sum('pacToUser'))['total_pac'] or 0
    print(total_pac_to_user)


    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_Model.objects.all().filter(userName=user)
    # inv_energyDay_data = [0 if x is None else x for x in response_json['obj']['pac']]
    now = datetime.datetime.now()
    format_datetime = now.strftime("%Y-%m-%d")
    payload = {
        "plantId": "2283430",
        "date": format_datetime
    }
    response_getInvEnergyDayChart = session.post("https://server.growatt.com/indexbC/inv/getInvEnergyDayChart", data=payload)
    if response_getInvEnergyDayChart.status_code == 200:
        response_json = response_getInvEnergyDayChart.json()
        # inv_energyDay_data = response_json['obj']['pac']
        inv_energyDay_data = [0 if x is None else x for x in response_json['obj']['pac']]
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvEnergyDayChart.status_code}")
    
    payload = {
        "plantId": "2283430",
        "date": now.strftime("%Y")
    }
    response_getInvEnergyMonthChart = session.post("https://server.growatt.com/indexbC/inv/getInvEnergyYearChart", data=payload)
    if response_getInvEnergyMonthChart.status_code == 200:
        response_json = response_getInvEnergyMonthChart.json()
        inv_energyMonth_data = response_json['obj']['energy']
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvEnergyMonthChart.status_code}")
    
    payload = {
        "plantId": "2283430",
        "date": now.strftime("%Y")
    }
    response_getInvEnergyYearChart = session.post("https://server.growatt.com/indexbC/inv/getInvEnergyTotalChart", data=payload)
    if response_getInvEnergyYearChart.status_code == 200:
        response_json = response_getInvEnergyYearChart.json()
        inv_energyYear_data = response_json['obj']['energy']
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvEnergyYearChart.status_code}")
    
    return render(request, 'index.html', {'MONTH':Month, 'epvToday':epvToday, 'eMonth':eMonth, 'pacToUser':pacToUser, 'filter':filtered_data, 'total_pac_to_user':total_pac_to_user, 'inv_energyDay_data': inv_energyDay_data,'inv_energyMonth_data':inv_energyMonth_data,'inv_energyYear_data':inv_energyYear_data})

# def BASE(request):
#     # if request.method == 'POST':
#     user_login = request.POST.get('data')
#     print("==> Người đăng nhập có user là: ", user_login)
#     print('===> 1: ', type(str(user_login)))
#     filtered_data = Manager_Model.objects.all().filter(userName=user_login)
#     return render(request, 'base.html', {'filter':filtered_data})
#     # user_login = request.POST.get('data')
#     # # print(type(str(user_login)))
#     # print("==> Người đăng nhập có user là: ", user_login)
#     # string_value = str(user_login)
#     # # filtered_data = Manager_Model.objects.all().filter(userName=user_login)
#     # filtered_data = Manager_Model.objects.all().filter(userName='Anh')
#     # print("=======> ", filtered_data)
#     # for item in filtered_data:
#     #     print(item.Name)
#     #     print(item.userName)
#     #     print(item.Password)
#     #     print(item.Jurisdiction)
#     #     return render(request, "te.html", {'filter':item.Jurisdiction})
#     # return render(request, "te.html", {'filter':filtered_data})

def solars_HTML(request):
    # client = snap7.client.Client()
    # client.connect("192.168.1.202", 0, 0, 102)
    # reading = client.db_read(1, 0, 220)

    # vi_tri_1 = snap7.util.get_int(reading, 0)
    # vi_tri_2 = snap7.util.get_int(reading, 2)
    # vi_tri_3 = snap7.util.get_int(reading, 4)
    # vi_tri_4 = snap7.util.get_int(reading, 6)
    # vi_tri_5 = snap7.util.get_int(reading, 8)
    # vi_tri_6 = snap7.util.get_int(reading, 10)
    # vi_tri_7 = snap7.util.get_int(reading, 12)
    # vi_tri_8 = snap7.util.get_int(reading, 14)
    # vi_tri_9 = snap7.util.get_int(reading, 16)
    # vi_tri_10 = snap7.util.get_int(reading, 18)
    # vi_tri_11 = snap7.util.get_int(reading, 20)
    # vi_tri_12 = snap7.util.get_int(reading, 22)
    # vi_tri_13 = snap7.util.get_int(reading, 24)
    # vi_tri_14 = snap7.util.get_int(reading, 26)
    # vi_tri_15 = snap7.util.get_int(reading, 28)
    # vi_tri_16 = snap7.util.get_int(reading, 30)

    # DienAp_1 = snap7.util.get_real(reading, 32)
    # DienAp_2 = snap7.util.get_real(reading, 36)
    # DienAp_3 = snap7.util.get_real(reading, 40)
    # DienAp_4 = snap7.util.get_real(reading, 44)
    # DienAp_5 = snap7.util.get_real(reading, 48)
    # DienAp_6 = snap7.util.get_real(reading, 52)
    # DienAp_7 = snap7.util.get_real(reading, 56)
    # DienAp_8 = snap7.util.get_real(reading, 60)
    # DienAp_9 = snap7.util.get_real(reading, 64)
    # DienAp_10 = snap7.util.get_real(reading, 68)
    # DienAp_11 = snap7.util.get_real(reading, 72)
    # DienAp_12 = snap7.util.get_real(reading, 76)
    # DienAp_13 = snap7.util.get_real(reading, 80)
    # DienAp_14 = snap7.util.get_real(reading, 84)
    # DienAp_15 = snap7.util.get_real(reading, 88)
    # DienAp_16 = snap7.util.get_real(reading, 92)

    # DongDien_1 = snap7.util.get_real(reading, 96)
    # DongDien_2 = snap7.util.get_real(reading, 100)
    # DongDien_3 = snap7.util.get_real(reading, 104)
    # DongDien_4 = snap7.util.get_real(reading, 108)
    # DongDien_5 = snap7.util.get_real(reading, 112)
    # DongDien_6 = snap7.util.get_real(reading, 116)
    # DongDien_7 = snap7.util.get_real(reading, 120)
    # DongDien_8 = snap7.util.get_real(reading, 124)
    # DongDien_9 = snap7.util.get_real(reading, 128)
    # DongDien_10 = snap7.util.get_real(reading, 132)
    # DongDien_11 = snap7.util.get_real(reading, 136)
    # DongDien_12 = snap7.util.get_real(reading, 140)
    # DongDien_13 = snap7.util.get_real(reading, 144)
    # DongDien_14 = snap7.util.get_real(reading, 148)
    # DongDien_15 = snap7.util.get_real(reading, 152)
    # DongDien_16 = snap7.util.get_real(reading, 156)

    # CongSua_1 = snap7.util.get_real(reading, 160)
    # CongSua_2 = snap7.util.get_real(reading, 164)
    # CongSua_3 = snap7.util.get_real(reading, 168)
    # CongSua_4 = snap7.util.get_real(reading, 172)
    # CongSua_5 = snap7.util.get_real(reading, 176)
    # CongSua_6 = snap7.util.get_real(reading, 180)
    # CongSua_7 = snap7.util.get_real(reading, 184)
    # CongSua_8 = snap7.util.get_real(reading, 188)
    # CongSua_9 = snap7.util.get_real(reading, 182)
    # CongSua_10 = snap7.util.get_real(reading, 196)
    # CongSua_11 = snap7.util.get_real(reading, 200)
    # CongSua_12 = snap7.util.get_real(reading, 204)
    # CongSua_13 = snap7.util.get_real(reading, 208)
    # CongSua_14 = snap7.util.get_real(reading, 212)
    # CongSua_15 = snap7.util.get_real(reading, 216)
    # CongSua_16 = snap7.util.get_real(reading, 220)

    








    vi_tri_1 = 1
    vi_tri_2 = 2
    vi_tri_3 = 3
    vi_tri_4 = 4
    vi_tri_5 = 5
    vi_tri_6 = 6
    vi_tri_7 = 7
    vi_tri_8 = 8
    vi_tri_9 = 9
    vi_tri_10 = 10
    vi_tri_11 = 11
    vi_tri_12 = 12
    vi_tri_13 = 13
    vi_tri_14 = 14
    vi_tri_15 = 15
    vi_tri_16 = 16

    DienAp_1 = 115.9034
    DienAp_2 = 125.9034
    DienAp_3 = 135.9034
    DienAp_4 = 145.9034
    DienAp_5 = 155.9034
    DienAp_6 = 165.9034
    DienAp_7 = 175.9034
    DienAp_8 = 185.9034
    DienAp_9 = 195.9034
    DienAp_10 = 110.59034
    DienAp_11 = 111.59034
    DienAp_12 = 112.59034
    DienAp_13 = 113.59034
    DienAp_14 = 114.59034
    DienAp_15 = 115.59034
    DienAp_16 = 116.59034

    DongDien_1 = 101.203
    DongDien_2 = 201.203
    DongDien_3 = 301.203
    DongDien_4 = 401.203
    DongDien_5 = 501.203
    DongDien_6 = 601.203
    DongDien_7 = 701.203
    DongDien_8 = 801.203
    DongDien_9 = 901.203
    DongDien_10 = 100.1203
    DongDien_11 = 110.1203
    DongDien_12 = 120.1203
    DongDien_13 = 130.1203
    DongDien_14 = 140.1203
    DongDien_15 = 150.1203
    DongDien_16 = 160.1203

    CongSua_1 = 101.203
    CongSua_2 = 201.203
    CongSua_3 = 301.203
    CongSua_4 = 401.203
    CongSua_5 = 501.203
    CongSua_6 = 601.203
    CongSua_7 = 701.203
    CongSua_8 = 801.203
    CongSua_9 = 901.203
    CongSua_10 = 100.1203
    CongSua_11 = 110.1203
    CongSua_12 = 120.1203
    CongSua_13 = 130.1203
    CongSua_14 = 140.1203
    CongSua_15 = 150.1203
    CongSua_16 = 160.1203

    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_Model.objects.all().filter(userName=user)

    Solal = {
        'filter':filtered_data,

        'So_1':vi_tri_1,
        'Dien_Ap_1':round(DienAp_1, 4),
        'Dong_Dien_1':round(DongDien_1, 4),
        'Cong_Suat_1':round(CongSua_1, 4),
        'So_2':vi_tri_2,
        'Dien_Ap_2':round(DienAp_2, 4),
        'Dong_Dien_2':round(DongDien_2, 4),
        'Cong_Suat_2':round(CongSua_2, 4),
        'So_3':vi_tri_3,
        'Dien_Ap_3':round(DienAp_3, 4),
        'Dong_Dien_3':round(DongDien_3, 4),
        'Cong_Suat_3':round(CongSua_3, 4),
        'So_4':vi_tri_4,
        'Dien_Ap_4':round(DienAp_4, 4),
        'Dong_Dien_4':round(DongDien_4, 4),
        'Cong_Suat_4':round(CongSua_4, 4),
        'So_5':vi_tri_5,
        'Dien_Ap_5':round(DienAp_5, 4),
        'Dong_Dien_5':round(DongDien_5, 4),
        'Cong_Suat_5':round(CongSua_5, 4),
        'So_6':vi_tri_6,
        'Dien_Ap_6':round(DienAp_6, 4),
        'Dong_Dien_6':round(DongDien_6, 4),
        'Cong_Suat_6':round(CongSua_6, 4),
        'So_7':vi_tri_7,
        'Dien_Ap_7':round(DienAp_7, 4),
        'Dong_Dien_7':round(DongDien_7, 4),
        'Cong_Suat_7':round(CongSua_7, 4),
        'So_8':vi_tri_8,
        'Dien_Ap_8':round(DienAp_8, 4),
        'Dong_Dien_8':round(DongDien_8, 4),
        'Cong_Suat_8':round(CongSua_8, 4),
        'So_9':vi_tri_9,
        'Dien_Ap_9':round(DienAp_9, 4),
        'Dong_Dien_9':round(DongDien_9, 4),
        'Cong_Suat_9':round(CongSua_9, 4),
        'So_10':vi_tri_10,
        'Dien_Ap_10':round(DienAp_10, 4),
        'Dong_Dien_10':round(DongDien_10, 4),
        'Cong_Suat_10':round(CongSua_10, 4),
        'So_11':vi_tri_11,
        'Dien_Ap_11':round(DienAp_11, 4),
        'Dong_Dien_11':round(DongDien_11, 4),
        'Cong_Suat_11':round(CongSua_11, 4),
        'So_12':vi_tri_12,
        'Dien_Ap_12':round(DienAp_12, 4),
        'Dong_Dien_12':round(DongDien_12, 4),
        'Cong_Suat_12':round(CongSua_12, 4),
        'So_13':vi_tri_13,
        'Dien_Ap_13':round(DienAp_13, 4),
        'Dong_Dien_13':round(DongDien_13, 4),
        'Cong_Suat_13':round(CongSua_13, 4),
        'So_14':vi_tri_14,
        'Dien_Ap_14':round(DienAp_14, 4),
        'Dong_Dien_14':round(DongDien_14, 4),
        'Cong_Suat_14':round(CongSua_14, 4),
        'So_15':vi_tri_15,
        'Dien_Ap_15':round(DienAp_15, 4),
        'Dong_Dien_15':round(DongDien_15, 4),
        'Cong_Suat_15':round(CongSua_15, 4),
        'So_16':vi_tri_16,
        'Dien_Ap_16':round(DienAp_16, 4),
        'Dong_Dien_16':round(DongDien_16, 4),
        'Cong_Suat_16':round(CongSua_16, 4)
    }
    return render(request, 'solars.html', Solal)

def configuration_HTML(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_Model.objects.all().filter(userName=user)
    return render(request, 'configuration.html', {'filter':filtered_data})

def manager_HTML(request):
    if request.method == "POST":
        Name = request.POST.get('add_name')
        userName = request.POST.get('add_userName')
        Password = request.POST.get('add_password')
        Press = request.POST.get('add_press')
        print(Name, userName, Password, Press)
        if Name and userName and Password and Press:
            create_user = User.objects.create_user(userName, password=Password)
            create_user.is_staff = True
            save_info = Manager_Model(Name=Name, userName=userName, Password=Password, Jurisdiction=Press)
            save_info.save()
            create_user.save()
        return redirect('/manager_HTML/')
    user_ = Manager_Model.objects.all()
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_Model.objects.all().filter(userName=user)
    return render(request, 'manager.html', {'user_list': user_, 'filter':filtered_data})

def manager_Delete(request, id):
    if request.method == 'POST':
        id_delete = Manager_Model.objects.get(pk=id)
        id_delete.delete()
        user_to_delete = User.objects.filter(id=id + 1).first()
        if user_to_delete:
            print(f"Thực hiện xóa user có ID {user_to_delete.id} và tên là {user_to_delete.username}")
            user_to_delete.delete()
        return redirect('/manager_HTML/')

def manager_Update(request, id):
    if request.method == "POST":
        edit_name = request.POST.get('edit_name')
        edit_user = request.POST.get('edit_userName')
        edit_password = request.POST.get('edit_password')
        edit_permission = request.POST.get('edit_permission')
        int_detele = int(id) + 1
        # print(int_detele)
        if edit_name and edit_user and edit_password and edit_permission:
            id_delete = Manager_Model.objects.get(pk=id)
            id_delete.delete()
            user_to_delete = User.objects.filter(id=int_detele).first()
            if user_to_delete:
                print(f"Thực hiện xóa user có ID {user_to_delete.id} và tên là {user_to_delete.username}")
                user_to_delete.delete()
            create_user = User.objects.create_user(edit_user, password=edit_password)
            create_user.is_staff = True
            create_user.save()
            save_info = Manager_Model(id=id, Name=edit_name, userName=edit_user, Password=edit_password, Jurisdiction=edit_permission)
            save_info.save()
            return redirect('/manager_HTML/')
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_Model.objects.all().filter(userName=user)
    return render(request, 'manager.html', {'filter':filtered_data})

def changepass_HTML(request):
    context = {}
    if request.method=='POST':
        pass_old = request.POST['pass_old']
        pass_new  = request.POST['pass_new']
        user = User.objects.get(id=request.user.id)
        check = user.check_password(pass_old)
        print(check)
        if check==True:
            user.set_password(pass_new)
            user.save()
            context['mess'] = 'Thay đổi mật khẩu thành công!!!'
            context['error'] = 'success_mess'
        else:
            context['mess'] = 'Mật khẩu bạn nhập không đúng'
            context['error'] = 'error_mess'

    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_Model.objects.all().filter(userName=user)
    context['filter'] = filtered_data  # Thêm filtered_data vào context
    return render(request, 'changepass.html', context)

def Logout(request):
    logout(request)
    messages.error(request, "Bạn đã đăng xuất")
    return redirect('/')