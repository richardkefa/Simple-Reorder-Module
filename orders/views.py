from django.shortcuts import render,redirect
from .models import Items,Order

def items_lIst(request):
    item_list =Items.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request,'index.html',context)

def send_order(id):
    item = Items.objects.get(id=id)
    order = Order.objects.create(Item_id=item)
    return redirect('items')

def order_list(request):
    # import pdb;pdb.set_trace();
    dispached_order = Order.objects.filter(dispached=True)
    pending_order = Order.objects.filter(dispached=False)
    
    context = {
       'dispached_orders':dispached_order,
       'pending_orders':list(pending_order),
    }

    return render(request,'order.html',context)

    


def sell_item(request,id):
    item = Items.objects.get(id=id)
    quantity = item.item_qty
    new_quantity = quantity-1
    if new_quantity == 0:
        new_quantity = 0
        return redirect('items')
    item.item_qty = new_quantity
    item.save(update_fields=["item_qty"])

    if new_quantity <= 3:
        send_order(id)
       
        return redirect('items')

    
    return redirect('items')


def dispatch_order(request,id):

    pending_order = Order.objects.get(id=id)
    # import pdb;pdb.set_trace();
    item = pending_order.Item_id
    item = Items.objects.get(item_name=item)
    item.item_qty = 10
    item.save(update_fields=["item_qty"])
    pending_order.dispached = True
    pending_order.save(update_fields=['dispached'])


    return redirect('order_list')

