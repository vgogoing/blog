from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from models import Category, Page
from forms import CategoryForm, PageForm
# Create your views here.


def index(request):
    # context_dict = {'somemessage': 'some message text'}
    category_list = Category.objects.order_by('-likes')[:5]
    # category_list = Category.objects.all()
    page_list = Page.objects.order_by('-views')[:5]
    # print type(category_list)
    context_dict = {'category': category_list, 'page': page_list}
    return render(request, 'blog/index.html', context_dict)

def about_page(requeet):
    # return HttpResponse('this is about')
    context_dict = {'message': 'aboutmessage'}
    return render(requeet, 'blog/about.html', context_dict)

def category(request, category_name_slug):
    context_dic = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        print category.name
        context_dic['category_name'] = category.name
        page_by_category = Page.objects.filter(category=category)
        context_dic['pages'] = page_by_category
        context_dic['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'blog/category.html', context_dic)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        print type(form)
        if form.is_valid():
            """  func doc::
            Returns True if the form has no errors. Otherwise, False. If errors are
            being ignored, returns False.
            """
            print 'form will save'
            form.save(commit=True)
        else:
            print 'form err'
            print form.errors

    else:
        form = CategoryForm()

    return render(request, 'blog/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    print category_name_slug
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.views = 0
                page.category = cat
                page.save()
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dic = {'form': form, 'category': cat, 'slug': category_name_slug}
    print context_dic
    return render(request, 'blog/add_page.html', context_dic)







