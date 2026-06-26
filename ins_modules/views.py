from django.shortcuts import render
from .models import Teacher
from django.views.generic import ListView , DetailView

class TeacherListView(ListView):
    template_name = 'ins_modules/ins_list.html'
    model = Teacher
    context_object_name = 'teachers'

    def get_queryset(self):
        return Teacher.objects.filter(is_active=True)

class TeacherDetailView(DetailView):
    template_name = 'ins_modules/ins_detail.html'
    model = Teacher
    context_object_name = 'teacher'


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    teacher = self.object

    context['related_teachers'] = Teacher.objects.filter(
        is_active=True
    ).exclude(id=teacher.id)[:4]

    return context



