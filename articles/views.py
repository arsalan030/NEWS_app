from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView,FormView # new
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls import reverse_lazy # new
from .models import Article
from django.views.generic.edit import (
UpdateView, DeleteView, CreateView # new
)
from django.contrib.auth.mixins import LoginRequiredMixin
UserPassesTestMixin
from django.views import View
from django.views.generic.detail import SingleObjectMixin

# Create your views here.
from django.views.generic import ListView
from .forms import CommentForm
from django.urls import reverse_lazy, reverse
class CommentGet(DetailView): # new
    model = Article
    template_name = "article_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context





class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"
# new
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})


class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = "article_list.html"
    
class ArticleDetailView(DetailView): # new
    model = Article
    template_name = "registration/article_detail.html"

    def get_context_data(self, **kwargs): # new
        
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
        
        
class ArticleUpdateView(LoginRequiredMixin,UpdateView): # new
        model = Article
        fields = (
        "title",
        "body",
        )
        template_name = "registration/article_edit.html"
        def test_func(self): # new
            obj = self.get_object()
            return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin,DeleteView): # new
    model = Article
    template_name = "registration/article_delete.html"
    success_url = reverse_lazy("article_list")
    
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.use

class ArticleCreateView(LoginRequiredMixin,CreateView): # new
    model = Article
    template_name = "registration//article_new.html"
    fields = (
    "title",
    "body", )
    
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)



