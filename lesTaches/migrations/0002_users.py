# Generated by Django 4.1.1 on 2022-09-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesTaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email adress')),
            ],
        ),
    ]