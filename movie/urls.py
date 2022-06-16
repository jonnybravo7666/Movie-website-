from django.urls import  path 
from . import views
# from.views import MovieDetail

urlpatterns = [ 
              
     path('movie/',views.Movielist , name='movie_list'),
     path('detail/<int:id>',views.Moviedetail , name='movie_detail'),
     # path('category/<int:id>',views.Moviecategory , name='movie_category'),
     path('headfoot/',views.headfoot, name='headfoot'),
     path('head/',views.head, name='head'),
     path('Aboutus/',views.about, name='about'),
     path('contact/',views.contact, name='contact'),
     path('account/',views.account, name='account'),
     path('logout/',views.logout, name='logout'),
     
     path('search/',views.search, name='search'),

     # path('',MovieList.as_view(), name='movie_list'),
     # path('<int:pk>',MovieDetail.as_view(), name='movie_detail'),
]