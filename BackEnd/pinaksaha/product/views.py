from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import ItemsForm
from .models import Category, Item
from .serializers import DataStoreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def items(request, category_slug=None):
    categories = Category.objects.all()
    items_queryset = Item.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items_queryset = Item.objects.filter(category=category)
    else:
        category = None

    form = ItemsForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('item')  # Redirect to the product list page after adding the product

    context = {'items': items_queryset, 'categories': categories, 'current_category': category, 'form': form}
    return render(request, 'product.html', context)

@api_view(['POST'])
def add_product_api(request):
    if request.method == 'POST':
        serializer = DataStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_product_api(request, product_id):
    try:
        product = Item.objects.get(pk=product_id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DataStoreSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

api_view(['DELETE'])
def delete_product_api(request, product_id):
    print(product_id)
    try:
        product = Item.objects.get(pk=product_id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
