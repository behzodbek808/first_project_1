from django.urls import path
from .views import NewsPageView

urlpatterns = [
    path('', NewsPageView.as_view(), name='news')
    ]