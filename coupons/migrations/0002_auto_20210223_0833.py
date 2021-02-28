# Generated by Django 3.1.6 on 2021-02-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='is_unlocked',
            field=models.BooleanField(default=False),
        ),
    ]
