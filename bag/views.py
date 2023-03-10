from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


# Create your views here.


def shopping_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_item(request, item_id):
    """ Add quantity of an item to shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    bag = request.session.get('bag', {})

    if color:
        if item_id in list(bag.keys()):
            if color in bag[item_id]['items_by_color'].keys():
                bag[item_id]['items_by_color'][color] += quantity
                messages.success(
                    request, f'Updated color {color.upper()} {product.name} \
                        quantity to {bag[item_id]["items_by_color"][color]}')
            else:
                bag[item_id]['items_by_color'][color] = quantity
                messages.success(request, f'\
                    Added color{color.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_color': {color: quantity}}
            messages.success(request, f'\
                Added color{color.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'\
                Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {quantity}|{product.name}\
                 to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Add quantity of an item to shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    bag = request.session.get('bag', {})

    if color:
        if quantity > 0:
            bag[item_id]['items_by_color'][color] = quantity
            messages.success(request, f'\
                Updated color{color.upper()}{product.name} \
                    quantity to {bag[item_id]["items_by_color"][color]}')
        else:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
                messages.success(request, f'\
                    Remove color{color.upper()}{product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'\
                Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def remove_item(request, item_id):
    """ Remove item from shopping bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
        color: None
        if 'product_color' in request.POST:
            color = request.POST['product_color']
        bag = request.session.get('bag', {})

        if color:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
                messages.success(request, f'\
                    Removed {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
