# Generated by Django 3.2 on 2022-01-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_bookinginfo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginfo',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]