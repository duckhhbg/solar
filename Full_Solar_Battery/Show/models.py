from django.db import models

# Create your models here.
class Manager_Model(models.Model):
    Jurisdiction_choices = [
        ("Giám sát", "Giám sát"),
        ("Quản trị", "Quản trị"),
        ("Điều khiển", "Điều khiển")
    ]
    Name = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Jurisdiction = models.CharField(choices=Jurisdiction_choices, max_length=20)

class Info_getTotalData(models.Model):
    save_day = models.DateField(blank=True, null=True)
    TotalData_mTotal = models.CharField(max_length=10, blank=True, null=True)
    TotalData_mToday = models.CharField(max_length=10, blank=True, null=True)
    TotalData_co2 = models.CharField(max_length=5, blank=True, null=True)
    TotalData_onlineNum = models.CharField(max_length=5, blank=True, null=True)
    TotalData_eMonth = models.CharField(max_length=10, blank=True, null=True)
    TotalData_pac = models.CharField(max_length=10, blank=True, null=True)
    TotalData_lostNum = models.CharField(max_length=5, blank=True, null=True)
    TotalData_waitNum = models.CharField(max_length=5, blank=True, null=True)
    TotalData_mMonth = models.CharField(max_length=10, blank=True, null=True)
    TotalData_nominalPower = models.CharField(max_length=10, blank=True, null=True)
    TotalData_eToday = models.CharField(max_length=10, blank=True, null=True)
    TotalData_eTotal = models.CharField(max_length=10, blank=True, null=True)
    TotalData_coa = models.CharField(max_length=10, blank=True, null=True)
    TotalData_gridDate = models.CharField(max_length=50, blank=True, null=True)
    TotalData_runDay = models.CharField(max_length=10, blank=True, null=True)

class Info_getPlantEnergyList(models.Model):
    nominalPower = models.CharField(max_length=10, blank=True)
    income = models.CharField(max_length=10, blank=True)
    date = models.DateField()
    c02 = models.CharField(max_length=5, blank=True)
    userLoad = models.CharField(max_length=5, blank=True)
    pacToUser = models.CharField(max_length=5, blank=True)
    energy = models.CharField(max_length=5, blank=True)

class Info_getWeatherByPlantId(models.Model):
    save_day = models.DateField()
    WeatherByPlantId_parent_city = models.CharField(max_length=100, blank=True)
    WeatherByPlantId_cloud = models.CharField(max_length=5, blank=True)
    WeatherByPlantId_hum = models.CharField(max_length=5, blank=True)
    WeatherByPlantId_wind_deg = models.CharField(max_length=5, blank=True)
    WeatherByPlantId_pres = models.CharField(max_length=5, blank=True)
    WeatherByPlantId_pcpn = models.CharField(max_length=5, blank=True)
    WeatherByPlantId_fl = models.CharField(max_length=5, blank=True)
    WeatherByPlantId_tmp = models.CharField(max_length=5, blank=True)
    WeatherByPlantId_wind_sc = models.CharField(max_length=5, blank=True)
    WeatherByPlantId_wind_spd = models.CharField(max_length=5, blank=True)

class Info_getInvStatusData(models.Model):
    save_day = models.DateField()
    InvStatusData_pac = models.CharField(max_length=10, blank=True)
    InvStatusData_subarrayNum = models.CharField(max_length=10, blank=True)
    InvStatusData_subarrayShowType = models.CharField(max_length=10, blank=True)

class Info_getInvTotalData(models.Model):
    save_day = models.DateField()
    InvTotalData_epvToday = models.CharField(max_length=10, blank=True)
    InvTotalData_epvTotal = models.CharField(max_length=10, blank=True)
    InvTotalData_pac = models.CharField(max_length=10, blank=True)

# Theo giờ
class Info_getInvEnergyDayChart(models.Model):
    save_day = models.DateField()
    inv_energyDay_data = models.JSONField(default=list, blank=True)

# Theo ngày
class Info_getInvEnergyMonthChart(models.Model):
    save_month = models.CharField(max_length=10)
    inv_energyMonth_data = models.JSONField(default=list, blank=True)

# Theo tháng
class Info_getInvEnergyYearChart(models.Model):
    year = models.CharField(max_length=10)
    inv_energyYear_data = models.JSONField(default=list, blank=True)