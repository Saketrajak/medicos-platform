from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Medicine, Category
from .serializers import MedicineSerializer, CategorySerializer


@api_view(['GET'])
def get_medicines(request):

    search = request.GET.get('search')
    category = request.GET.get('category')

    medicines = Medicine.objects.all()

    if search:
        medicines = medicines.filter(name__icontains=search)

    if category:
        medicines = medicines.filter(category_id=category)

    serializer = MedicineSerializer(medicines, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_medicine_detail(request, id):

    medicine = Medicine.objects.get(id=id)
    serializer = MedicineSerializer(medicine)

    return Response(serializer.data)


@api_view(['GET'])
def get_categories(request):

    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)

