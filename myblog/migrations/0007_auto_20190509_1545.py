# Generated by Django 2.1.7 on 2019-05-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20190509_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='host_name',
            field=models.CharField(max_length=30, verbose_name='主机名'),
        ),
    ]