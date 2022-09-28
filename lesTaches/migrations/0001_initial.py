# Generated by Django 4.1.1 on 2022-09-28 19:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('creation_date', models.DateField(auto_now=True)),
                ('closed', models.BooleanField(default=False)),
                ('due_date', models.DateField(null=True)),
                ('schedule_date', models.DateField(default=datetime.date(2022, 10, 5))),
                ('owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='lesTaches.user')),
            ],
        ),
    ]
