from rest_framework import serializers

from .models import Customer, Product ,Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer', write_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, source='products', write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'products', 'customer_id', 'product_ids', 'total_amount', 'created_at']
        read_only_fields = ['total_amount', 'created_at']