from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.cart.models import Cart, CartItem
from apps.medicines.models import Medicine
from .models import Order, OrderItem
from .serializers import OrderSerializer


# CREATE ORDER (Checkout)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):

    user = request.user

    # check if cart exists
    cart = Cart.objects.filter(user=user).first()

    if not cart:
        return Response({"error": "Cart not found"})

    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items:
        return Response({"error": "Cart is empty"})

    total = 0

    # create order
    order = Order.objects.create(user=user, total_price=0)

    for item in cart_items:

        medicine = item.medicine

        # prevent ordering more than stock
        if item.quantity > medicine.stock:
            return Response({
                "error": f"{medicine.name} does not have enough stock"
            })

        price = medicine.discount_price * item.quantity

        OrderItem.objects.create(
            order=order,
            medicine=medicine,
            quantity=item.quantity,
            price=price
        )

        # reduce medicine stock
        medicine.stock -= item.quantity
        medicine.save()

        total += price

    order.total_price = total
    order.save()

    # clear cart
    cart_items.delete()

    return Response({"message": "Order created successfully"})


# ORDER HISTORY
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history(request):

    user = request.user

    orders = Order.objects.filter(user=user)

    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)


# ORDER DETAIL
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_detail(request, id):

    try:
        order = Order.objects.get(id=id, user=request.user)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"})

    serializer = OrderSerializer(order)

    return Response(serializer.data)