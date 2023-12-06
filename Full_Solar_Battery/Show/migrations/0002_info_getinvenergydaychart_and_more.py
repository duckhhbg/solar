# Generated by Django 4.2.6 on 2023-11-30 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info_getInvEnergyDayChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_day', models.DateField()),
                ('inv_energyDay_data', models.JSONField(blank=True, default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Info_getInvEnergyMonthChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_month', models.CharField(max_length=10)),
                ('inv_energyMonth_data', models.JSONField(blank=True, default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Info_getInvEnergyYearChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
                ('inv_energyYear_data', models.JSONField(blank=True, default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Info_getInvStatusData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_day', models.DateField()),
                ('InvStatusData_pac', models.CharField(blank=True, max_length=10)),
                ('InvStatusData_subarrayNum', models.CharField(blank=True, max_length=10)),
                ('InvStatusData_subarrayShowType', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Info_getInvTotalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_day', models.DateField()),
                ('InvTotalData_epvToday', models.CharField(blank=True, max_length=10)),
                ('InvTotalData_epvTotal', models.CharField(blank=True, max_length=10)),
                ('InvTotalData_pac', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Info_getPlantEnergyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominalPower', models.CharField(blank=True, max_length=10)),
                ('income', models.CharField(blank=True, max_length=10)),
                ('date', models.DateField()),
                ('c02', models.CharField(blank=True, max_length=5)),
                ('userLoad', models.CharField(blank=True, max_length=5)),
                ('pacToUser', models.CharField(blank=True, max_length=5)),
                ('energy', models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Info_getTotalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_day', models.DateField(blank=True, null=True)),
                ('TotalData_mTotal', models.CharField(blank=True, max_length=10, null=True)),
                ('TotalData_mToday', models.CharField(blank=True, max_length=10, null=True)),
                ('TotalData_co2', models.CharField(blank=True, max_length=5, null=True)),
                ('TotalData_onlineNum', models.CharField(blank=True, max_length=5, null=True)),
                ('TotalData_eMonth', models.CharField(blank=True, max_length=10, null=True)),
                ('TotalData_pac', models.CharField(blank=True, max_length=10, null=True)),
                ('TotalData_lostNum', models.CharField(blank=True, max_length=5, null=True)),
                ('TotalData_waitNum', models.CharField(blank=True, max_length=5, null=True)),
                ('TotalData_mMonth', models.CharField(blank=True, max_length=10, null=True)),
                ('TotalData_nominalPower', models.CharField(blank=True, max_length=10, null=True)),
                ('TotalData_eToday', models.CharField(blank=True, max_length=10, null=True)),
                ('TotalData_eTotal', models.CharField(blank=True, max_length=10, null=True)),
                ('TotalData_coa', models.CharField(blank=True, max_length=10, null=True)),
                ('TotalData_gridDate', models.CharField(blank=True, max_length=50, null=True)),
                ('TotalData_runDay', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info_getWeatherByPlantId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_day', models.DateField()),
                ('WeatherByPlantId_parent_city', models.CharField(blank=True, max_length=100)),
                ('WeatherByPlantId_cloud', models.CharField(blank=True, max_length=5)),
                ('WeatherByPlantId_hum', models.CharField(blank=True, max_length=5)),
                ('WeatherByPlantId_wind_deg', models.CharField(blank=True, max_length=5)),
                ('WeatherByPlantId_pres', models.CharField(blank=True, max_length=5)),
                ('WeatherByPlantId_pcpn', models.CharField(blank=True, max_length=5)),
                ('WeatherByPlantId_fl', models.CharField(blank=True, max_length=5)),
                ('WeatherByPlantId_tmp', models.CharField(blank=True, max_length=5)),
                ('WeatherByPlantId_wind_sc', models.CharField(blank=True, max_length=5)),
                ('WeatherByPlantId_wind_spd', models.CharField(blank=True, max_length=5)),
            ],
        ),
    ]
