# Generated by Django 4.2.2 on 2023-06-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
    ]
