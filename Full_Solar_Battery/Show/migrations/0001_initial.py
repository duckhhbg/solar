# Generated by Django 4.2.6 on 2023-11-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('userName', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('Jurisdiction', models.CharField(choices=[('Giám sát', 'Giám sát'), ('Quản trị', 'Quản trị'), ('Điều khiển', 'Điều khiển')], max_length=20)),
            ],
        ),
    ]