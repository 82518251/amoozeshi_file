from django import  forms
from .models import ArticleComment, Article , ArticlaCategory, Newsletter

class ArticleCommentForm(forms.ModelForm):
    class Meta :
        model= ArticleComment
        fields= ['name', 'email', 'text','image','description']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder': 'نام شما' }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل شما'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'پیغام تو'})
        }
        labels = {
            'name' :'نام و نام خانوادگی',
            'email' : 'ایمیل',
            'text' : ' موضوع نظر شما',
            'description' :'نظر شما'

        }

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        text = cleaned_data.get('text')

        if not name:
            raise forms.ValidationError("لطفا نام خود را وارد کنید")

        if not email:
            raise forms.ValidationError("لطفا ایمیل خود را وارد کنید")

        if not text:
            raise forms.ValidationError("لطفا متن نظر را وارد کنید")

        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta :
        model = Article
        fields = ['title' , 'selected_categoris' , 'short_description', 'Text' , 'image']

class ArticlaCategoryForm(forms.ModelForm) :
    class Meta :
        model = ArticlaCategory
        fields = ['title', 'parent', 'url_title']

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ['email']



