from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from .models import Property, User
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth import login
class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'prop_list'
    model = Property

    def get_queryset(self):
        queryset = Property.objects.all()
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.filter(
                Q(area__icontains=query) | \
                Q(title__icontains=query) | \
                Q(address__icontains=query) | \
                Q(access1__icontains=query)
            )
        return queryset[:20]

class TopView(generic.TemplateView):
    template_name = 'top.html'
    # ↓これいらなくね？？
    # context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     return Property.objects.all()

class MypageView(generic.TemplateView):
    template_name = 'mypage.html'

class LikesView(generic.ListView):
    template_name = 'like.html'
    context_object_name = 'prop_list'
    model = Property

# class BookmarkView(generic.TemplateView):
#     template_name = ''

class SignupView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid
