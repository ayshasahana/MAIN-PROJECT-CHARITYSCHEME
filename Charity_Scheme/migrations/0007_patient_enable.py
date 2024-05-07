# Generated by Django 5.0.2 on 2024-04-06 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Charity_Scheme', '0006_delete_patient_enable'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_enable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reson', models.CharField(max_length=100)),
                ('status', models.FileField(upload_to='')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Charity_Scheme.patientinfo_table')),
            ],
        ),
    ]
