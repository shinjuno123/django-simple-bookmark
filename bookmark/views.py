from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Bookmark
from django.urls import reverse_lazy,reverse
# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    template_name = 'bookmark_list.html'
    paginate_by = 6


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields= ['site_name','url'] # 데베로부터 어떤필드로 입력받을건지
    success_url = reverse_lazy('list') #글쓰기를 완료하고 이동할 페이지
    template_name = 'bookmark_create.html'


class BookmarkDetailView(DetailView):
    model = Bookmark
    template_name = 'bookmark_detail.html'


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields= ['site_name','url']
    template_name = 'bookmark_update.html'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    template_name = 'bookmark_delete.html'

    

