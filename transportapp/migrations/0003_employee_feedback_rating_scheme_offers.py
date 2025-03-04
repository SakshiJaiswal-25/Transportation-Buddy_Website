# Generated by Django 4.2.5 on 2023-10-09 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transportapp', '0002_rename_contect_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('phone', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=20)),
                ('experience', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('employee_pic', models.FileField(default='', max_length=200, upload_to='transportapp/employee_pic')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack_Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('feedback_text', models.TextField()),
                ('ratings', models.CharField(max_length=6)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Scheme_Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=45)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
