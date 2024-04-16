from django.db import models


class Pan(models.Model):
    gen = [("WOMEN", "women"), ("MEN", "men"), ("BOY", "boy"), ("GIRL", "girl")]
    candidate_name = models.CharField(max_length=20)
    mobile_no = models.IntegerField()
    gender = models.CharField(max_length=20, choices=gen)
    address = models.CharField(max_length=20)
    pan_no = models.CharField(max_length=20)

