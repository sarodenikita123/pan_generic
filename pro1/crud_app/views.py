from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Pan


class PanCreate(CreateView):
    model = Pan
    fields = "__all__"


class PanList(ListView):
    model = Pan


class PanDetail(DetailView):
    model = Pan


class PanUpdate(UpdateView):
    model = Pan
    fields = "__all__"
    success_url = "/"


class PanDelete(DeleteView):
    model = Pan
    success_url = "/"
    template_name = "crud_app/pan_delete.html"


