# Generated by Django 2.2.1 on 2020-05-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZenoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zenoid', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.CharField(blank=True, max_length=100, null=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
