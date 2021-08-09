from django.db.models.query import RawQuerySet
from django.forms.forms import Form
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from .models import Property#, User
from .forms import SignupForm, SearchDetailForm


User = get_user_model()

class HomeView(generic.ListView, generic.FormView):
    template_name = 'home.html'
    context_object_name = 'prop_list'
    model = Property
    form_class = SearchDetailForm
    success_url = reverse_lazy('app:home')
    paginate_by = 25

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs).order_by("value_rate","difference_normalize").reverse()
        query = self.request.GET.get('query')
        address_distance = self.request.GET.get('address_distance')
        age = self.request.GET.get('age')
        menseki = self.request.GET.get('menseki')
        price = self.request.GET.get('price')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | \
                Q(address__icontains=query) | \
                Q(access1__icontains=query) | \
                Q(access2__icontains=query) | \
                Q(access3__icontains=query))

        if address_distance:
            queryset = queryset.filter(Q(address_distance__lte=address_distance))
        if age:
            queryset = queryset.filter(Q(age__lte=age))
        if menseki:
            queryset = queryset.filter(Q(menseki__gte=menseki))
        if price:
            queryset = queryset.filter(Q(price__lte=price))

        return queryset


class TopView(generic.TemplateView):
    template_name = 'top.html'

class MypageView(generic.TemplateView):
    template_name = 'mypage.html'

class LikesView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'prop_list'
    model = Property

class SignupView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid
