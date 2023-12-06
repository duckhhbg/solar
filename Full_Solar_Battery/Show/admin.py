from django.contrib import admin
from .models import Manager_Model, Info_getTotalData, Info_getPlantEnergyList, Info_getWeatherByPlantId, Info_getInvStatusData, Info_getInvTotalData, Info_getInvEnergyDayChart, Info_getInvEnergyMonthChart, Info_getInvEnergyYearChart

# Register your models here.
@admin.register(Manager_Model)
class Manager_Admin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'userName', 'Jurisdiction')

admin.site.register(Info_getTotalData)
admin.site.register(Info_getPlantEnergyList)
admin.site.register(Info_getWeatherByPlantId)
admin.site.register(Info_getInvStatusData)
admin.site.register(Info_getInvTotalData)
admin.site.register(Info_getInvEnergyDayChart)
admin.site.register(Info_getInvEnergyMonthChart)
admin.site.register(Info_getInvEnergyYearChart)