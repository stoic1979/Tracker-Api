from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal



class UserLocation(models.Model):
    """
    Model for storing user location at given timestamp
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # NOTE
    # quick geography tips !!!
    # 3 digits will be need for lat/lng and 6 for decimal places
    # max lat 90 and max lng 180
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return 'UserLocation: (' + str(Decimal(self.lat)) + ', ' + str(Decimal(self.lng)) + ')'
