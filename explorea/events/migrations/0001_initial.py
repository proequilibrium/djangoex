# Generated by Django 2.1.2 on 2018-10-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]
