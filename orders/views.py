from django.shortcuts import render,redirect
from .models import Items,Order

def items_lIst(request):
    item_list =Items.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request,'index.html',context)

def send_order(item_name):
    item = Items.objects.get(item_name=item_name)
    order = Order.objects.create(item_name=item)
    return redirect('items')

def order_list(request):
    dispached_order = Order.objects.filter(dispached=True)
    pending_order = Order.objects.filter(dispached=False)
    context={
       'dispached_orders':dispached_order,
       'pending_orders':pending_order,
    }

    return render(request,'order.html',context)

    


def sell_item(request,id):
    item = Items.objects.get(id=id)
    item_name = item.item_name
    quantity = item.item_qty
    new_quantity = quantity-1
    if new_quantity == 0:
        new_quantity = 0
        return new_quantity
    item.item_qty = new_quantity
    item.save(update_fields=["item_qty"])

    if new_quantity <= 3:
        send_order(item_name)
        message = "Item is criticaly low an order has been sent out to the warehouse"
        context = {
        "message": message,
    }
        return redirect('items',context)

    
    return redirect('items')



