from django.conf import settings
from decimal import Decimal

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PRECENTAGE/100)
        free_delivery = settings.FREE_DELIVERY - total
    else:
        delivery = 0
        free_delivery = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery': delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY,
        'grand_total': grand_total,
    }

    return context
