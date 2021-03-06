# Generated by Django 2.0.2 on 2018-02-12 23:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RateLimitedPhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('messages_remaining', models.PositiveIntegerField()),
            ],
        ),
    ]
