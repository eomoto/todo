from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Item

class IndexView(generic.ListView):
  template_name = 'app/index.html'
  context_object_name = 'item_list'
  def get_queryset(self):
    return Item.objects.all()

class DetailView(generic.DetailView):
  model = Item
  template_name = 'app/detail.html'

def update(request, item_id):
  item = get_object_or_404(Item, pk=item_id)
  if "checkbox" in request.POST:
    item.complete = True
  else:
    item.complete = False
  item.save()
  return HttpResponseRedirect(reverse('app:detail', args=(item.id,)))
