# Generated by Django 5.0.2 on 2024-03-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Charity_Scheme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo_table',
            name='sdate',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
    ]
