from django.shortcuts import render , redirect
from django.urls import reverse
from django.views import View
from .models import contact
from .form import ContactModelsForm
from django.views.generic.edit import  CreateView
from django.views.generic import ListView


class contact_fun_view(View):
    def get(self, request):
        contact_form = ContactModelsForm()
        return render(request , 'contact_modules/contactt.html' ,{
              'contact_form' : contact_form
                      })
    def post(self, request):
        contact_form = ContactModelsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('contact_page')
        return render(request, 'contact_modules/contactt.html', {
                'contact_form' : contact_form
        })




#
# class contactView(CreateView):
#     form_class = ContactModelsForm
#     template_name = 'contact_modules/contact.html'
#     success_url = '/contact'
# Create your views here.
