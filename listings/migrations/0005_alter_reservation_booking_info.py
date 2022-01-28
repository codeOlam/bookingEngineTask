# Generated by Django 3.2 on 2022-01-28 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20220128_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='booking_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reservation', to='listings.bookinginfo'),
        ),
    ]
