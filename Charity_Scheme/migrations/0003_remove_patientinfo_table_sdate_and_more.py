# Generated by Django 5.0.2 on 2024-03-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Charity_Scheme', '0002_patientinfo_table_sdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinfo_table',
            name='sdate',
        ),
        migrations.AddField(
            model_name='patientinfo_table',
            name='status',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
