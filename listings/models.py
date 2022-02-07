from django.db import models
from django.db.models.signals import post_save
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
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
    )
    isBooked = models.BooleanField(default=False, null=True, blank=True)
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)

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


    def __str__(self):
        if self.listing:
            obj = self.listing
        else:
            obj = self.hotel_room_type

        return f'{obj} {self.price}'


class Reservation(models.Model):
    hotel_room = models.ForeignKey(
        HotelRoom, 
        blank=True, 
        null=True, 
        on_delete=models.CASCADE,
        related_name='reservation'
    )
    hotel_room_type = models.ForeignKey(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='reservation'
    )
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.hotel_room}'


@receiver(post_save, sender=HotelRoom)
def onBooked(instance, **kwargs):
    """
        This signal will create or delete a reservation for everytime BookingInfo instance
        is updated by setting;
        isBooked: True
        check_in: date
        check_out: date
    """
    reservation_instance = Reservation()
    if instance.isBooked == True and (instance.check_in and instance.check_out) is not None:
        if not Reservation.objects.filter(hotel_room_id=instance.id).exists():
            reservation_instance.hotel_room_id = instance.id
            reservation_instance.hotel_room_type_id = instance.hotel_room_type_id
            reservation_instance.check_in = instance.check_in
            reservation_instance.check_out = instance.check_out
            reservation_instance.save()

    elif instance.isBooked == False and (instance.check_in and instance.check_out) is None:
        reservation_instance = Reservation.objects.filter(
            hotel_room_id=instance.id
        )

        if reservation_instance.exists():
            reservation_instance.delete()
