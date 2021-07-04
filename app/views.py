from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from .models import Property, User
from django.contrib import messages

class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'prop_list'
    model = Property
    # paginate_by = 20

    def get_queryset(self):
        queryset = Property.objects.all()
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(address__icontains=query) | Q(access1__icontains=query)
            )
            # messages.add_message(self.request, messages.INFO, query)
        return queryset[:20]



class TopView(generic.TemplateView):
    template_name = 'top.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):

        return Property.objects.all()

class LikesView(generic.TemplateView):
    template_name = ''

class BookmarkView(generic.TemplateView):
    template_name = ''


# class UserView(generic.UserView):
#     model = Question
#     template_name = 'polls/detail.html'

#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

