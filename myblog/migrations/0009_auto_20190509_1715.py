# Generated by Django 2.1.7 on 2019-05-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_auto_20190509_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='like_user',
            field=models.ManyToManyField(blank=True, null=True, to='myblog.Likes', verbose_name='点赞人'),
        ),
    ]
