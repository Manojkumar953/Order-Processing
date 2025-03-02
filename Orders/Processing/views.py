from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .queue import add_task
from .serlializers import OrderSerializer
import time


# Create your views here.

class OrdersView(APIView):
    def get(self, request):
        serializer = OrderSerializer(Order.objects.filter(status=request.data['status']), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        if Order.objects.filter(order_id=request.data['order_id']):
            return Response({"status": "Record already present"}, status=status.HTTP_400_BAD_REQUEST)
        request.data['status'] = 'Pending'
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            add_task((request.data['order_id'], self.current_milli_time()))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"repose": "Error"}, status=status.HTTP_400_BAD_REQUEST)

    def current_milli_time(self):
        return round(time.time() * 1000)

class MetricsView(APIView):
    def get(self, request):
        processed_orders_count = len(Order.objects.filter(status = 'Completed'))
        pending_order_count = len(Order.objects.filter(status = 'Pending'))
        processing_order_count = len(Order.objects.filter(status = 'Processing'))
        records = Order.objects.filter(status = 'Completed')
        average_time = 0
        count = 0
        for record in records:
            if record.processing_time is not None:
                average_time += record.processing_time
                count += 1
        if count > 0:
            average_time /= count
        return Response({
            'Total-Records-Processed': processed_orders_count,
            'Average-Processing-Time': average_time,
            'Orders-Status': {
                'Pending': pending_order_count,
                'Processing': processing_order_count,
                'Processed': processed_orders_count
            }
        }, status=status.HTTP_200_OK)