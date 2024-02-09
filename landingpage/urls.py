# tu mapujemy URL wraz z funkcjami ktore maja wywolywac w view
from django.urls import path
from . import views # kropka oznacza aktualny folder

urlpatterns = [
    path('', views.index), # nie trzeba wzywac funkcji index czyli nie trzeba dawac jej nawiasow bo django zrobi to sam w momencie wywolania
    path('new', views.new), #zakladka new -> landingpage/new dlatego trzeba to wpisac w apostrofy
    path('items', views.items)

]