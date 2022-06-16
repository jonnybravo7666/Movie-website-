from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from movie.models import Movie
# from django.views.generic import ListView, DetailView
# Create your views here.

def account(request):
    return render(request ,'movie/acount.html')

def about(request):
    return render(request ,'movie/about.html')

def contact(request):
    return render(request ,'movie/contact.html')

def logout(request):
    return render(request,"index.html")

def search(request):
    query=request.GET['query']
    allPosts = Movie.objects.filter(title_icontains=query)
    params={'allPosts':allPosts}
    return render(request,'movie/search.html', params)

def Movielist(request):
    movi = Movie.objects.all()
    paginator = Paginator(movi, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    return render(request,'movie/movie_list.html',{'page_obj':page_obj})


def Moviedetail(request, id):
    
    movi = Movie.objects.get(pk=id)
    movi.views_count += 1
    movi.save()
    return render(request,'movie/movie_detail.html',{'movi':movi })


    
# class MovieDetail(DetailView):
#     model = Movie
    

#     def get_object(self):
#         object = super(Moviedetail, self).get_object()
#         return object

#     def get_context_detail(self, **kwargs):
#         context = super(Moviedetail, self).get_context_data(self, **kwargs)
#         context["links"] = Movielinks.object.filter(movie=self.get_object())
#         return context

# def get_queryset(self):
#     self.category = self.kwargs['category']
#     return Movie.objects.filter(category = self.category)

# def get_context_data(self, **kwargs):
#     context = super(Movielist,self).get_context_data(**kwargs)
#     context["movie_category"] = self.category 
#     return context
   
        
        
   
        
def headfoot(request):
    return render(request,'movie/headerfooter.html')

def head(request):
    return render(request,'movie/hearder.html')