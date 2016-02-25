from django import forms
from models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='raw_put category name')
    views = forms.CharField(widget=forms.HiddenInput(), initial=0)
    likes = forms.CharField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name', 'views', 'likes')

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='raw_input title ')
    views = forms.CharField(widget=forms.HiddenInput, initial=0)
    url = forms.CharField(max_length=200, help_text='raw_inpu url ')

    def clean(self):
        cleaned_data = self.cleaned_data
        print cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Page
        exclude = ('category',)  #or fields = ('titles', 'views', 'url')  to show
