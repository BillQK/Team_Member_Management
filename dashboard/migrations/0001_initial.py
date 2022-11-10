# Generated by Django 4.1.3 on 2022-11-10 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('admin', models.BooleanField(default=False)),
                ('PhoneNumber', models.BigIntegerField(unique=True)),
            ],
        ),
    ]