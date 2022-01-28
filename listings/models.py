from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Listing(models.Model):
    HOTEL = 'hotel'
    APARTMENT = 'apartment'
    LISTING_TYPE_CHOICES = (
        ('hotel', 'Hotel'),
        ('apartment', 'Apartment'),
    )

    listing_type = models.CharField(
        max_length=16,
        choices=LISTING_TYPE_CHOICES,
        default=APARTMENT
    )
    title = models.CharField(max_length=255,)
    country = models.CharField(max_length=255,)
    city = models.CharField(max_length=255,)

    def __str__(self):
        return self.title


class HotelRoomType(models.Model):
    hotel = models.ForeignKey(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hotel_room_types'
    )
    title = models.CharField(max_length=255,)

    def __str__(self):
        return f'{self.hotel} - {self.title}'


class HotelRoom(models.Model):
    hotel_room_type = models.ForeignKey(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hotel_rooms'
    )
    room_number = models.CharField(max_length=255,)

    def __str__(self):
        return self.room_number


class BookingInfo(models.Model):
    listing = models.OneToOneField(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info'
    )
    hotel_room_type = models.OneToOneField(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info',
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    isBooked = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        if self.listing:
            obj = self.listing
        else:
            obj = self.hotel_room_type

        return f'{obj} {self.price}'


class Reservation(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    booking_info = models.ForeignKey(
        BookingInfo,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info'
    )

    def __str__(self):
        return f'{self.booking_info}'


@receiver(post_save, sender=Reservation)
def onReservation(sender, created, instance, **kwargs):
    booking_info_instance = BookingInfo.objects.get(
        pk=instance.booking_info.id)
    if created:
        booking_info_instance.isBooked = True
        booking_info_instance.save()
