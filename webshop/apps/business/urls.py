from django.urls import path, include
from . import views
from .views import BbCreateView, BbView, RubricView
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'business'


urlpatterns = [
    path('list/', views.index, name='index'),
    path('list/send_message', views.send_message, name='send_message'),
    path('list/<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    path('bb/<int:bb_id>/', views.show_bb, name='show_bb'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/bb', BbView.as_view(), name='bb'),
    path('api/rubrics', RubricView.as_view(), name='rubrics'),
]
