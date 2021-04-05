# Generated by Django 3.1.7 on 2021-04-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('unnamed_0', models.BigIntegerField(blank=True, db_column='Unnamed: 0', null=True)),
                ('movie', models.TextField(blank=True, null=True)),
                ('year', models.BigIntegerField(blank=True, null=True)),
                ('timemin', models.BigIntegerField(blank=True, db_column='timeMin', null=True)),
                ('imdb', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Movies',
                'managed': False,
            },
        ),
    ]
