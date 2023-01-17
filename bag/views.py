from django.shortcuts import render, redirect

# Create your views here.


def shopping_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')

def add_item(request, item_id):
    """ Add quantity of an item to shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request. session.get('bag',{})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
