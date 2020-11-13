from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="firecalculator-home"),
    path('about', views.about, name="firecalculator-about"),
    path('methodology', views.methodology, name="firecalculator-methodology"),
    path('result', views.result, name="firecalculator-result"),
    path('recalculate',views.recalculate,name="firecalculator-recalculate"),
]



