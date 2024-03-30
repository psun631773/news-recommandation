# Generated by Django 3.1.7 on 2021-03-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('newsid', models.IntegerField()),
                ('comments', models.CharField(max_length=1000)),
                ('userid', models.IntegerField()),
                ('touserid', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('history_newsid', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='hotword',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hotword', models.CharField(max_length=50)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='newssimilar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('new_id_base', models.CharField(max_length=64)),
                ('new_id_sim', models.CharField(max_length=64)),
                ('new_correlation', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='recommend',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('hadread', models.IntegerField()),
                ('cor', models.FloatField()),
                ('newsid', models.ManyToManyField(to='news_api.newsdetail')),
            ],
        ),
    ]