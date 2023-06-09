# Generated by Django 4.2.1 on 2023-05-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('client_no', models.IntegerField()),
                ('client_desc', models.CharField(max_length=100)),
                ('project_no', models.IntegerField()),
                ('project_desc', models.CharField(max_length=100)),
                ('total_working_hour', models.IntegerField()),
                ('working_hour_desc', models.CharField(max_length=100)),
                ('worker_no', models.IntegerField()),
                ('worker_desc', models.CharField(max_length=100)),
            ],
        ),
    ]
