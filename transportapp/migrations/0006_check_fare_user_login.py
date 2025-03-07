# Generated by Django 4.2.5 on 2023-10-14 07:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transportapp', '0005_customer_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='check_fare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up', models.CharField(max_length=100)),
                ('drop', models.CharField(max_length=100)),
                ('distance', models.CharField(max_length=5)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='user_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
