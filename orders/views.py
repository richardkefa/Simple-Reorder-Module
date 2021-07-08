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
    item_name = item.item_name
    quantity = item.item_qty
    new_quantity = quantity-1
    if new_quantity == 0:
        new_quantity = 0
        return redirect('items')
    item.item_qty = new_quantity
    item.save(update_fields=["item_qty"])

    if new_quantity <= 3:
        send_order(item_name)
       
        return redirect('items')

    
    return redirect('items')


def dispatch_order(id):

    pending_order = Order.objects.filter(id)
    item_name = pending_order.item_name
    item = Items.objects.get(item_name=item_name)
    item.item_qty = 10
    item.save(update_fields=("item_qyt"))
    pending_order.dispached = True
    pending_order.save(update_fields=('dispached'))


    return redirect('item_list')

