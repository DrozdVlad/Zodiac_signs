from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from api.models import Client


class HomeListView(generic.ListView):
    model = Client
    template_name = 'home.html'


class ClientDetailListView(generic.ListView):
    model = Client
    template_name = 'client_detail.html'

    context_object_name = 'client'

    def get_queryset(self):
        return Client.objects.get(id=self.kwargs['id'])


class ClientCreate(CreateView):
    model = Client
    template_name = 'client_create.html'
    success_url = reverse_lazy('api:home')

    fields = ['first_name', 'last_name', 'date_of_birth', 'address',]


class ClientUpdate(UpdateView):
    model = Client
    template_name = 'client_update.html'
    success_url = reverse_lazy('api:home')

    fields = '__all__'  # Not recommended (potential security issue if more fields added)


class ClientDelete(DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('api:home')

