from django.shortcuts import render
from .models import Items,Order

def items_lIst(request):
    item_list =Items.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request,'index.html',context)

def send_order(request,id):
    item = Items.objects.get(id)
    item_name = item.item_name
    order = Order(item_name=item_name)
    order.save()
    order_number = order.order_number

    context={
        'order_number': order_number,
        'item_name': item_name
    }

    return render(request,'index.html',context)

def sell_item(request,id):
    item = Items.get(id)
    quantity = item.quantity
    new_quantity = quantity-1
    Items.quantity = new_quantity
    Items.save()
    if new_quantity is 3:
        send_order(id)

    else:
        return
    Items.save()

    context = {
        "new_qeantity":quantity
    }
    return render(request,'index.html',quantity)



