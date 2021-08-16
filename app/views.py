from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.views import generic
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import SignupForm, SearchDetailForm
from .models import Property


User = get_user_model()

class HomeView(generic.ListView, generic.FormView):
    template_name = 'home.html'
    context_object_name = 'prop_list'
    model = Property
    form_class = SearchDetailForm
    success_url = reverse_lazy('app:home')
    paginate_by = 10

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs).order_by("value_rate","difference_normalize").reverse()
        query = self.request.GET.get('query')
        madori = self.request.GET.get('madori')
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

        if madori:
            queryset = queryset.filter(Q(madori__icontains=madori))
        if menseki:
            queryset = queryset.exclude(Q(menseki__lte=menseki))
        if age:
            queryset = queryset.filter(Q(age__lte=age))
        if price:
            queryset = queryset.filter(Q(price__lte=price))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = '?'
        context["q"] += f'query={self.request.GET.get("query")}&' if self.request.GET.get('query') else ""
        context["q"] += f'madori={self.request.GET.get("madori")}&' if self.request.GET.get('madori') else ""
        context["q"] += f'age={self.request.GET.get("age")}&' if self.request.GET.get('age') else ""
        context["q"] += f'menseki={self.request.GET.get("menseki")}&' if self.request.GET.get('menseki') else ""
        context["q"] += f'price={self.request.GET.get("price")}&' if self.request.GET.get('price') else ""
        return context

class TopView(generic.TemplateView):
    template_name = 'top.html'

class MypageView(generic.TemplateView):
    template_name = 'mypage.html'

class LikesView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'prop_list'
    model = Property

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)[:10]

        return queryset

class SignupView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid
