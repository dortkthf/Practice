# Generated by Django 3.2.13 on 2022-09-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('nickname', models.TextField()),
                ('pw', models.TextField()),
            ],
        ),
    ]
