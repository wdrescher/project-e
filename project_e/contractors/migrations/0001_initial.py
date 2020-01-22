# Generated by Django 2.2.7 on 2020-01-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Contractor Name')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Contractor Email')),
                ('address', models.CharField(max_length=500, verbose_name='Address')),
                ('fname', models.CharField(max_length=30, verbose_name='First Name')),
                ('lname', models.CharField(max_length=30, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('notes', models.CharField(max_length=500, verbose_name='Misc Notes')),
                ('num_installs', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
