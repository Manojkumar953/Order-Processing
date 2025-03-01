from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serlializers import OrderSerializer


# Create your views here.

class OrdersView(APIView):
    def get(self, request):
        serializer = OrderSerializer(Order.objects.filter(status = request.data['status']), many=True)
        return Response(data = serializer.data)

    def post(self, request):
        request.data['status'] = 'Pending'
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"repose": "Error"}, status=status.HTTP_400_BAD_REQUEST)
