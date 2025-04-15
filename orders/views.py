from django.shortcuts import render

# Create your views here.

from .models import Customer , Product , Order
from .serializers import CustomerSerializer , ProductSerializer , OrderSerializer
from rest_framework import viewsets
from .permissions import IsAuthenticatedForCreate
from rest_framework.permissions import IsAuthenticated



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedForCreate]  


    def perform_create(self, serializer):
        # 1. Get product IDs from request data
        product_ids = self.request.data.get('product_ids', [])

        # 2. Retrieve the selected products from the database
        products = Product.objects.filter(id__in=product_ids)

        # 3. Calculate total price of selected products
        total = sum(product.price for product in products)

        # 4. Create the order and add products to the order
        order = serializer.save(total_amount=total)

        # 5. Associate the products with the order (many-to-many relationship)
        order.products.set(products)  

        return order
