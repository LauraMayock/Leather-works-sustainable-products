from django.shortcuts import render

# Create your views here.


def shopping_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')