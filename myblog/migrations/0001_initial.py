# Generated by Django 2.2 on 2019-04-28 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=10)),
                ('sex', models.CharField(choices=[('F', '女'), ('M', '男')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('excerpt', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'published')], max_length=1)),
                ('comment_num', models.PositiveIntegerField(default=0)),
                ('inspect_num', models.PositiveIntegerField(default=0)),
                ('author', models.ManyToManyField(to='myblog.User')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myblog.Category')),
                ('tag', models.ManyToManyField(blank=True, null=True, to='myblog.Tag')),
            ],
        ),
    ]
