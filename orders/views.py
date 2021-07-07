from django.shortcuts import render
from .models import Items,Order

def items_lIst(request):
    item_list =Items.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request,'index.html',context)

def sell_item(request,id):
    item = Items.get(id)
    quantity = item.quantity
    new_quantity = quantity-1
    Items.quantity = new_quantity
    Items.save()

    context = {
        "new_qeantity":quantity
    }
    return render(request,'index.html',quantity)
