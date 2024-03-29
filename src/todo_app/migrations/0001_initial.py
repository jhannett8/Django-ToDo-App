# Generated by Django 2.2.4 on 2019-08-23 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeframe', models.CharField(choices=[('td', 'Today'), ('wk', 'This Week'), ('mnth', 'This Month'), ('sp', 'In My Spare Time')], default='Today', max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, default=datetime.date.today)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
