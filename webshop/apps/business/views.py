from builtins import super
from django.shortcuts import render
from .models import Bb, Rubric, UserMessage
from django.views.generic.edit import CreateView
from django.core.mail import send_mail, EmailMessage
from .forms import BbForm, UserMessageForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BbSerializer, RubricSerializer
from .tasks import sleepy, send_email_task

class BbView(APIView):
    def get(self, request):
        content = Bb.objects.all()
        serializer = BbSerializer(content, many=True)
        context = {
            'content': serializer.data,
        }
        return Response(context)

class RubricView(APIView):
    def get(self, request):
        rubrics = Rubric.objects.all()
        serializer = RubricSerializer(rubrics, many=True)
        context = {
            'rubrics': serializer.data,
        }
        return Response(context)

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
            user_message = form.save()
            '''
            user_name = request.POST.get('user_name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')

            send_mail(
                user_name + " : " + email,
                subject + " : " + message,
                send_from,
                ['bernar.berdikul@mail.ru'],
                fail_silently=False,
            )
            '''
            sleepy.delay(20)
            send_email_task.delay(user_message.id)
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
