
from django.shortcuts import render , get_object_or_404 , redirect
from  django.http import  HttpResponse , HttpRequest
from  django.views import View
from  django.views.generic.list import ListView
from  blog_modules.models import Article ,ArticleComment, ArticlaCategory
from  django.views.generic import ListView, DetailView
from  .form import ArticleCommentForm


class ArticleListView(ListView):
    template_name = 'blog_modules/blog_list.html'
    model = Article
    context_object_name = 'article_list'
    paginate_by = 6

    def get_queryset(self):

        query = super().get_queryset()

        query = query.filter(is_Active=True)

        search = self.request.GET.get('q')

        if search:
            query = query.filter(
                title__icontains=search
            )

        category_name = self.kwargs.get('category')

        if category_name is not None:
            query = query.filter(
                selected_categoris__url_title__iexact=category_name
            )

        return query.order_by('-create_date')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)



        return context


class ArticleDetailView(DetailView):
    template_name = 'blog_modules/article_detail.html'
    model = Article
    context_object_name = 'article'

    def get_object(self, queryset=None):

        return get_object_or_404(
            Article,
            id=self.kwargs['id'],
            is_Active=True
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        article = self.object

        context['comments'] = ArticleComment.objects.filter(
            article=article,
            parent=None
        ).order_by('-create_date').prefetch_related(
            'articlecomment_set'
        )

        context['comments_count'] = ArticleComment.objects.filter(
            article=article
        ).count()

        context['comments_form'] = ArticleCommentForm()
        context['categories'] = ArticlaCategory.objects.all()
        context['popular_articles'] = Article.objects.filter(
            is_Active=True
        ).exclude(id=self.object.id).order_by('-id')[:5]

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = ArticleCommentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            comment = form.save(commit=False)

            comment.article = self.object

            comment.save()
            return redirect(self.object.get_absolute_url())

        context = self.get_context_data()

        context['comments_form'] = form


        return self.render_to_response(context)
# Create your views here.
