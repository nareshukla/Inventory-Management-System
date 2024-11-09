from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import InventoryItemForm
from .models import InventoryItem

def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})

def add_inventory_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/add_inventory_item.html', {'form': form})

def update_inventory_item(request, pk):
    item = InventoryItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm(instance=item)
    return render(request, 'inventory/update_inventory_item.html', {'form': form})

def delete_inventory_item(request, pk):
    item = InventoryItem.objects.get(pk=pk)
    item.delete()
    return redirect('inventory_list')
