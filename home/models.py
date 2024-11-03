from django.db import models
import uuid

# Create your models here.

class NullableModel(models.Model):
    class Meta:
        abstract = True  # Ensures this model is not created as a table in the database

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Automatically set `null=True` for all fields
        for field in self._meta.fields:
            if not isinstance(field, models.AutoField):  # Skip AutoFields (e.g., primary key)
                field.null = True



class Forts(models.Model):
    fort_id = models.AutoField(primary_key=True)
    fort_name = models.CharField(max_length=100)
    fort_district = models.CharField(max_length=100)
    fort_latitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    fort_longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    link = models.URLField()

    class Meta:
        ordering = ['fort_id']  # Order by `fort_id` in ascending order


    def __str__(self):
        return self.fort_name



class latitude_longitude(models.Model):
    plan_id = models.AutoField(primary_key=True)
    origin_latitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    origin_longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    destination_latitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    destination_longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)

    class Meta:
        ordering = ['plan_id'] 

    def __str__(self) :
          return f"{self.plan_id}"


class user_location(models.Model):
  u_id = models.AutoField(primary_key=True)
  user_latitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
  user_longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)

  class Meta:
        ordering = ['u_id'] 

  def __str__(self) :
      return f"{self.u_id},{self.user_latitude},{self.user_longitude}"
  

class Route(NullableModel):
    id = models.AutoField(primary_key=True)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    mode = models.CharField(max_length=50)
    traffic_model = models.CharField(max_length=50)
    departure_time = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self) :
        return f"{self.id}"
        


class Result(NullableModel):
    id = models.AutoField(primary_key=True)
    request_time = models.DateTimeField()
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    origin_addresses = models.CharField(max_length=500)
    destination_addresses = models.CharField(max_length=500)
    mode = models.CharField(max_length=50)
    traffic_model = models.CharField(max_length=50)
    departure_time = models.CharField(max_length=50)
    distance_value = models.IntegerField()
    distance_text = models.CharField(max_length=50)
    duration_value = models.IntegerField()
    duration_text = models.CharField(max_length=50)
    duration_in_traffic_value = models.IntegerField()
    duration_in_traffic_text = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self) :
        return f"{self.id},{self.origin},{self.destination},{self.distance_text},{self.duration_text}"



    