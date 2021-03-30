# Generated by Django 3.1.7 on 2021-03-29 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(default=None, max_length=200, null=True)),
                ('keyword', models.CharField(default=None, max_length=200, null=True)),
                ('search_date', models.DateTimeField(default=None, null=True)),
            ],
        ),
    ]
