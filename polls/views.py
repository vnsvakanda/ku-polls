"""This is views file that use for implementation."""

from django.http import HttpResponseRedirect
from .models import Choice, Question, Vote
# from django.template import loader
# from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    """This is the interface class of the app."""

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions \
            (not including those set to be published in the future)."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """This is class for create the result page interface."""

    model = Question
    template_name = 'polls/results.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def vote(request, question_id):
    """Fuction to submitted the vote to the specific polls \
        that get voted."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # record the vote
        user = request.user
        # Get the previous vote for this user (may not have)
        vote = get_vote_for_user(user, question)
        # case 1: user has not voted for this poll question yet
        #         Create a new Vote object
        if not vote:
            vote = Vote(user=user, choice=selected_choice)
        else:
            # case 2: user has already vote
            # Modify the existing vote and save it
            vote.choice = selected_choice
        vote.save()
        # Always redirect after POST request to prevent multiple
        # requests if user presses back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def get_vote_for_user(user, poll_question):
    """Find and return an existing vote for a user on a poll question.

    Returns:
        The user's Vote or None if no vote for this poll_question
    """
    votes = Vote.objects.filter(user=user)\
                .filter(choice__question=poll_question)
    # should be only one
    if votes.count() == 0:
        return None
    else:
        return votes[0]


@login_required
def view_poll(request, pk):
    """Fuction to displayed if the polls is \
        succesfully voted or not."""
    question = get_object_or_404(Question, pk=pk)
    previous_vote = False
    if Vote.objects.filter(user=request.user):
        previous_vote = Vote.objects.filter(user=request.user).first().choice.choice_text
    if not question.can_vote():
        messages.error(request, "Cannot vote!")
        return redirect('polls:index')
    return render(request, 'polls/detail.html', {'question': question, 'previous_vote': previous_vote})

    # messages.success(request, "Voted successfully!")
    # return render(request, 'polls/detail.html', {'question': question})
