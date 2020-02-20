from builtins import super
from django.shortcuts import render
from .models import Bb, Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm, UserMessageForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse


class BbCreateView(CreateView):
    template_name = 'business/create.html'
    form_class = BbForm
    success_url = reverse_lazy('business:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def send_message(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            '''brief = create(
                user_name=request.POST['user_name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message'],
            )'''
            form.save()
            return HttpResponseRedirect(reverse('business:index'))
        else:
            return HttpResponse('<h1>Form nicht ausgefüllt</h1>')


def show_bb(request, bb_id):
    bb = Bb.objects.get(id=bb_id)
    context = {
        'bb': bb,
    }
    return render(request, 'business/detail.html', context)


def index(request):
    bbs = Bb.objects.all()[:6]
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
    }
    return render(request, 'business/list.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    return render(request, 'business/by_rubric.html', context)
