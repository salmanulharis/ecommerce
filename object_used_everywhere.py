from products.models import Products, Category, AddCart
from django.shortcuts import HttpResponse
def include_groups(request):
    #perform your logic to create your list of groups
    if request.user.is_authenticated:
        cart_count = AddCart.objects.filter(user=request.user).count()
        categories = Category.objects.all()
        return {'cart_count':cart_count, 'categories': categories}
    else:
        categories = Category.objects.all()
        return {'categories': categories}