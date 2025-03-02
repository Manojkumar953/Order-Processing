from django.db import models


# Create your models here.
class Order(models.Model):
    order_id = models.CharField(primary_key = True, max_length=36)
    user_id = models.CharField(max_length=36)
    item_id = models.CharField(max_length=36)
    total_amount = models.IntegerField()
    status = models.CharField(choices=(('Pending', 1), ('Processing', 2), ('Completed', 3)), max_length=10)
    processing_time = models.IntegerField(null=True)

