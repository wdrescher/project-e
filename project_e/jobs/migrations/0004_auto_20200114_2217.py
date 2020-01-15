# Generated by Django 2.2.7 on 2020-01-15 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200114_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='contractor_completed_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date Completed by Contractor'),
        ),
        migrations.AlterField(
            model_name='job',
            name='contractor_notified_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date Given To Contractor'),
        ),
        migrations.AlterField(
            model_name='job',
            name='pref_inst_day1',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Preferred Installation Time 1'),
        ),
        migrations.AlterField(
            model_name='job',
            name='pref_inst_day2',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Preferred Installation Time 2'),
        ),
        migrations.AlterField(
            model_name='job',
            name='pref_inst_day3',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Preferred Installation Time 3'),
        ),
        migrations.AlterField(
            model_name='job',
            name='sale_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of Sale'),
        ),
    ]
