from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, JsonResponse
from django.views import View
from django.views.generic.base import TemplateView
from site_setting.models import SiteSetting, Slider,FooterLink, FooterLinkBox
from product_modules.models import Product , Category, ProductTag, ProductModel, ProductComment
from ins_modules.models import Teacher
from blog_modules.models import Article
from site_setting.models import Slider, SiteSetting, FooterLinkBox, FooterLink

from django.contrib.auth.decorators import login_required
from order_modules.models import Order, OrderDetail

class homeView(TemplateView):
    template_name = 'index_modules/index_page.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        products = Product.objects.filter(is_active=True , is_deleted=False)
        teachers = Teacher.objects.filter(is_active=True)
        blogs = Article.objects.filter(is_Active=True)
        context= {
            'products': products[:6],
            'teachers' : teachers[:4],
            'blogs' : blogs[:3]
        }

        return context

def site_header(request):
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context= {
            'site_setting' :setting
        }
        return render(request, 'header_component.html', context)

def site_footer(request):

    setting = SiteSetting.objects.filter(
        is_main_setting=True
    ).first()

    footer_link_boxes = FooterLinkBox.objects.prefetch_related(
        'footerlink_set'
    ).all()

    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }

    return render(request, 'footer_component.html', context)

class AboutView(TemplateView):
    # template_name = 'index_modules/about_page.html'

    def get_context_data(self, **kwargs):
        context= super(AboutView, self).get_context_data(**kwargs)
        site_setting : SiteSetting= SiteSetting.objects.filter(is_main_setting=True).first()
        sontext['site_setting'] = site_setting
        return  context

#





class AboutView(TemplateView):
    template_name = 'index_modules/about_page.html'

    def get_context_data(self, **kwargs):
        context= super(AboutView, self).get_context_data(**kwargs)
        site_setting : SiteSetting= SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return  context



def not_fount_page(request):
    return render(request, 'index_modules/404.html')
# Create your views here.
