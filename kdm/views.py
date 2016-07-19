from django.shortcuts import render, redirect
from kdm.models import *
# Create your views here.
# Create your views here.
#from kdm.forms import *
from urllib import quote_plus
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from kdm.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
#from django.template import 
from kdm.models import Blog
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q


def home(request):
	return render_to_response(
		'home.html',
		)
	

def test(request):
    return render_to_response(
        'sem.html',
        )
    
def contact(request):
    return render_to_response('contact.html',
        )

# @csrf_protect
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password1'],
#             email=form.cleaned_data['email']
#             )
#             return HttpResponseRedirect('/register/success')
#     else:
#         form = RegistrationForm()
#         variables = RequestContext(request, {
#         'form': form
#     })
 
#     return render_to_response(
#     'registration/register.html',
#     variables,
#     )
 
# def register_success(request):
#     return render_to_response(
#     'registration/success.html',
#     )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def blog(request):
    return render_to_response(
    'blog.html',
    { 'user': request.user }
    )

def index(request):
    queryset_list = Blog.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(user__username__icontains=query)
            ).distinct()

    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        # If page is not n integer, deliver first page.
        queryset= paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset= paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "page_request_var": page_request_var,
    }
    return render(request, "index.html", context)
    
def work(request):
    queryset = Project.objects.all()
    context = {
    "list" : queryset,
    }
    return render(request,"work.html", context)


def view_post(request, id=None):  
    instance =  get_object_or_404(Blog, id=id)
    # if instance.draft:
    #     if not request.user.is_authenticated():
    #         raise Http404
    share_string = quote_plus(instance.body)
    context = {
        "post" : instance,
        "share_string" : share_string,
    }
    return render(request, "view_post.html", context)
    # return render_to_response('view_post.html', {
    #     'post': get_object_or_404(Blog, id=id)
    # })
    
def project_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return HttpResponseRedirect("/accounts/login")
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        example = form.save(commit=False)
        example.user = request.user
        example.save()

        return HttpResponseRedirect(example.get_absolute_url())

    context = {
    "form":form,
    }
    return render(request, "create_project.html", context)

def post_create(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/accounts/login")
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()

        messages.add_message(request, messages.SUCCESS, "Your article was added")

        return HttpResponseRedirect(instance.get_absolute_url())
   

    context = {
    "form": form,
    }
    return render(request, "create_blog.html", context)
    

def post_update(request, id=None):
    if not request.user.is_authenticated():
        raise Http404
    instance = get_object_or_404(Blog, id=id)
    if not request.user == instance.user:
        raise Http404
    form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    

    context = {
        "title" : instance.title,
        "instance" : instance,
        "form" : form,
    }
    return render(request, "create_blog.html", context)

def post_delete(request, id=None):
    if not request.user.is_authenticated():
        raise Http404
    instance = get_object_or_404(Blog, id=id)
    instance.delete()

    messages.add_message(request,
        settings.DELETE_MESSAGE,"Your article was deleted")
    return redirect("/blogs")




# def view_category(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     return render_to_response('view_category.html', {
#         'category': category,
#         'posts': Blog.objects.filter(category=category)[:5]
#     })
