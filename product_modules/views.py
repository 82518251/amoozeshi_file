from django.shortcuts import render, get_object_or_404, redirect
from product_modules.models import Product, ProductComment
from django.views.generic import ListView , DetailView
from .form import ProductCommentForm
from django.views.generic import DetailView
from .models import Product , Category


class ProductListView(ListView):
    model = Product
    template_name = 'product_modules/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(is_active=True)







class ProductDetailView(DetailView):
    template_name = 'product_modules/product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product = self.object

        # محصولات مرتبط
        related_products = Product.objects.filter(
            category=product.category,
            is_active=True,
            is_deleted=False
        ).exclude(id=product.id)[:3]

        # کامنت‌ها
        comments = ProductComment.objects.filter(
            product=product,
            parent=None
        ).order_by('-created_date')

        context['related_products'] = related_products
        context['comments'] = comments

        context['comments_count'] = ProductComment.objects.filter(
            product=product
        ).count()

        # فرم کامنت
        context['form'] = kwargs.get('form', ProductCommentForm())

        context['categories'] = Category.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = ProductCommentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            comment = form.save(commit=False)

            comment.product = self.object

            # اگر کاربر لاگین بود
            if request.user.is_authenticated:
                comment.user = request.user

            comment.save()

            return redirect(self.object.get_absolute_url())

        context = self.get_context_data(form=form)

        return self.render_to_response(context)



def sidebar(request):
    categories = Category.objects.all()

    return render(request, 'product_modules/product_detail.html', {
        'categories': categories
    })
# Create your views here.
