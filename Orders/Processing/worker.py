from django.db import transaction
from .models import Order
import time

# takes event and process that and stores the record back into db
def worker(event):
    request_id, start_time = event
    try:
        with transaction.atomic():
            request = Order.objects.select_for_update().get(order_id = request_id)
            if request.status == 'Pending':
                request.status = 'Processing'
                request.save()
                request.status = 'Completed'
                end_time = round(time.time() * 1000)
                processing_time = end_time - start_time
                request.processing_time = processing_time
                request.save()
    except Exception:
        print("error")