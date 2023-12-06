from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import snap7


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('User_Name')
            Password = request.POST.get('Password')
            user = authenticate(username=username, password=Password)
            if user is not None:
                # Kiểm tra điều kiện hợp lệ ==> Đăng nhập thành công
                login(request, user)
                return redirect('/Login_Success')
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

class Affter_Login(View):
    def get(self, request):
        # url = "http://solar-ctd.ddns.net/data/line"
        # response = requests.get(url)
        # data = response.json()

        # line1_power = data["data"]["line1"]["power"]
        # line1_volt = data["data"]["line1"]['volt']
        # line1_perform = data["data"]["line1"]["perform"]
        # line1_ampe = data["data"]["line1"]["ampe"]

        # line2_power = data["data"]["line2"]["power"]
        # line2_volt = data["data"]["line2"]['volt']
        # line2_perform = data["data"]["line2"]["perform"]
        # line2_ampe = data["data"]["line2"]["ampe"]

        # conx = {
        #     'line1_power':line1_power,
        #     'line1_volt':line1_volt,
        #     'line1_perform':line1_perform,
        #     'line1_ampe':line1_ampe,
        #     'line2_power':line2_power,
        #     'line2_volt':line2_volt,
        #     'line2_perform':line2_perform,
        #     'line2_ampe':line2_ampe
        # }

        # return render(request, 'index.html', conx)
        return render(request, 'index.html')
    
def index_HTML(req):
    return render(req, 'index.html')

def Connect_PLC():
    client = snap7.client.Client()
    client.connect("192.168.1.202", 0, 0, 102)
    print(client.get_connected())
    print("====================")

def solars_HTML(req):
    client = snap7.client.Client()
    client.connect("192.168.1.202", 0, 0, 102)
    reading = client.db_read(1, 0, 220)

    vi_tri_1 = snap7.util.get_int(reading, 0)
    vi_tri_2 = snap7.util.get_int(reading, 2)
    vi_tri_3 = snap7.util.get_int(reading, 4)
    vi_tri_4 = snap7.util.get_int(reading, 6)
    vi_tri_5 = snap7.util.get_int(reading, 8)
    vi_tri_6 = snap7.util.get_int(reading, 10)
    vi_tri_7 = snap7.util.get_int(reading, 12)
    vi_tri_8 = snap7.util.get_int(reading, 14)
    vi_tri_9 = snap7.util.get_int(reading, 16)
    vi_tri_10 = snap7.util.get_int(reading, 18)
    vi_tri_11 = snap7.util.get_int(reading, 20)
    vi_tri_12 = snap7.util.get_int(reading, 22)
    vi_tri_13 = snap7.util.get_int(reading, 24)
    vi_tri_14 = snap7.util.get_int(reading, 26)
    vi_tri_15 = snap7.util.get_int(reading, 28)
    vi_tri_16 = snap7.util.get_int(reading, 30)

    DienAp_1 = snap7.util.get_real(reading, 32)
    DienAp_2 = snap7.util.get_real(reading, 36)
    DienAp_3 = snap7.util.get_real(reading, 40)
    DienAp_4 = snap7.util.get_real(reading, 44)
    DienAp_5 = snap7.util.get_real(reading, 48)
    DienAp_6 = snap7.util.get_real(reading, 52)
    DienAp_7 = snap7.util.get_real(reading, 56)
    DienAp_8 = snap7.util.get_real(reading, 60)
    DienAp_9 = snap7.util.get_real(reading, 64)
    DienAp_10 = snap7.util.get_real(reading, 68)
    DienAp_11 = snap7.util.get_real(reading, 72)
    DienAp_12 = snap7.util.get_real(reading, 76)
    DienAp_13 = snap7.util.get_real(reading, 80)
    DienAp_14 = snap7.util.get_real(reading, 84)
    DienAp_15 = snap7.util.get_real(reading, 88)
    DienAp_16 = snap7.util.get_real(reading, 92)

    DongDien_1 = snap7.util.get_real(reading, 96)
    DongDien_2 = snap7.util.get_real(reading, 100)
    DongDien_3 = snap7.util.get_real(reading, 104)
    DongDien_4 = snap7.util.get_real(reading, 108)
    DongDien_5 = snap7.util.get_real(reading, 112)
    DongDien_6 = snap7.util.get_real(reading, 116)
    DongDien_7 = snap7.util.get_real(reading, 120)
    DongDien_8 = snap7.util.get_real(reading, 124)
    DongDien_9 = snap7.util.get_real(reading, 128)
    DongDien_10 = snap7.util.get_real(reading, 132)
    DongDien_11 = snap7.util.get_real(reading, 136)
    DongDien_12 = snap7.util.get_real(reading, 140)
    DongDien_13 = snap7.util.get_real(reading, 144)
    DongDien_14 = snap7.util.get_real(reading, 148)
    DongDien_15 = snap7.util.get_real(reading, 152)
    DongDien_16 = snap7.util.get_real(reading, 156)

    CongSua_1 = snap7.util.get_real(reading, 160)
    CongSua_2 = snap7.util.get_real(reading, 164)
    CongSua_3 = snap7.util.get_real(reading, 168)
    CongSua_4 = snap7.util.get_real(reading, 172)
    CongSua_5 = snap7.util.get_real(reading, 176)
    CongSua_6 = snap7.util.get_real(reading, 180)
    CongSua_7 = snap7.util.get_real(reading, 184)
    CongSua_8 = snap7.util.get_real(reading, 188)
    CongSua_9 = snap7.util.get_real(reading, 182)
    CongSua_10 = snap7.util.get_real(reading, 196)
    CongSua_11 = snap7.util.get_real(reading, 200)
    CongSua_12 = snap7.util.get_real(reading, 204)
    CongSua_13 = snap7.util.get_real(reading, 208)
    CongSua_14 = snap7.util.get_real(reading, 212)
    CongSua_15 = snap7.util.get_real(reading, 216)
    # CongSua_16 = snap7.util.get_real(reading, 220)

    Pin_1 = {
        'So_1':vi_tri_1,
        'Dien_Ap_1':DienAp_1,
        'Dong_Dien_1':DongDien_1,
        'Cong_Suat_1':CongSua_1
    }
    Pin_2 = {
        'So_2':vi_tri_2,
        'Dien_Ap_2':DienAp_2,
        'Dong_Dien_2':DongDien_2,
        'Cong_Suat_2':CongSua_2
    }
    Pin_3 = {
        'So_3':vi_tri_3,
        'Dien_Ap_3':DienAp_3,
        'Dong_Dien_3':DongDien_3,
        'Cong_Suat_3':CongSua_3
    }
    Pin_4 = {
        'So_4':vi_tri_4,
        'Dien_Ap_4':DienAp_4,
        'Dong_Dien_4':DongDien_4,
        'Cong_Suat_4':CongSua_4
    }
    Pin_5 = {
        'So_5':vi_tri_5,
        'Dien_Ap_5':DienAp_5,
        'Dong_Dien_5':DongDien_5,
        'Cong_Suat_5':CongSua_5
    }
    Pin_6 = {
        'So_6':vi_tri_6,
        'Dien_Ap_6':DienAp_6,
        'Dong_Dien_6':DongDien_6,
        'Cong_Suat_6':CongSua_6
    }
    Pin_7 = {
        'So_7':vi_tri_7,
        'Dien_Ap_7':DienAp_7,
        'Dong_Dien_7':DongDien_7,
        'Cong_Suat_7':CongSua_7
    }
    Pin_8 = {
        'So_8':vi_tri_8,
        'Dien_Ap_8':DienAp_8,
        'Dong_Dien_8':DongDien_8,
        'Cong_Suat_8':CongSua_8
    }
    Pin_9 = {
        'So_9':vi_tri_9,
        'Dien_Ap_9':DienAp_9,
        'Dong_Dien_9':DongDien_9,
        'Cong_Suat_9':CongSua_9
    }
    Pin_10 = {
        'So_10':vi_tri_10,
        'Dien_Ap_10':DienAp_10,
        'Dong_Dien_10':DongDien_10,
        'Cong_Suat_10':CongSua_10
    }
    Pin_11 = {
        'So_11':vi_tri_11,
        'Dien_Ap_11':DienAp_11,
        'Dong_Dien_11':DongDien_11,
        'Cong_Suat_11':CongSua_11
    }
    Pin_12 = {
        'So_12':vi_tri_12,
        'Dien_Ap_12':DienAp_12,
        'Dong_Dien_12':DongDien_12,
        'Cong_Suat_12':CongSua_12
    }
    Pin_13 = {
        'So_13':vi_tri_13,
        'Dien_Ap_13':DienAp_13,
        'Dong_Dien_13':DongDien_13,
        'Cong_Suat_13':CongSua_13
    }
    Pin_14 = {
        'So_14':vi_tri_14,
        'Dien_Ap_14':DienAp_14,
        'Dong_Dien_14':DongDien_14,
        'Cong_Suat_14':CongSua_14
    }
    Pin_15 = {
        'So_15':vi_tri_15,
        'Dien_Ap_15':DienAp_15,
        'Dong_Dien_15':DongDien_15,
        'Cong_Suat_15':CongSua_15
    }
    Pin_16 = {
        'So_16':vi_tri_16,
        'Dien_Ap_16':DienAp_16,
        'Dong_Dien_16':DongDien_16,
        # 'Cong_Suat_16':CongSua_16
    }
    Solal = {
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
        'Dong_Dien_16':round(DongDien_16, 4)
    }

    return render(req, 'solars.html', Solal)

def configuration_HTML(req):
    return render(req, 'configuration.html')

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


    return render(request, 'changepass.html', context)

def Logout(request):
    logout(request)
    messages.error(request, "Bạn đã đăng xuất")
    return redirect('/')