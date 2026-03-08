from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Cart, CartItem
from apps.medicines.models import Medicine
from .serializers import CartItemSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):

    user = request.user
    medicine_id = request.data['medicine_id']
    quantity = request.data.get('quantity', 1)

    medicine = Medicine.objects.get(id=medicine_id)

    cart, created = Cart.objects.get_or_create(user=user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        medicine=medicine
    )

    cart_item.quantity += int(quantity)
    cart_item.save()

    return Response({"message": "Added to cart"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):

    cart = Cart.objects.get(user=request.user)

    items = CartItem.objects.filter(cart=cart)

    serializer = CartItemSerializer(items, many=True)

    return Response(serializer.data)