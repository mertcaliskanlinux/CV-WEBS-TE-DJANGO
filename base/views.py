from django.shortcuts import redirect, render
from base.forms import ContactForm
from django.views.generic import FormView
from django.urls import reverse_lazy

from .models import Home,About, Post
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def home(request):
    home = Home.objects.all()
    context = {
        'home':home
    }
    return render(request,'base/home.html',context)



def about(request):
    abouts = About.objects.all()
    context={
        'abouts':abouts
    }
    return render(request,'base/about.html', context)



def post(request,):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'base/post.html', context)

def post_new(request, pk):

    post= Post.objects.get(id=pk)
    if request.method == 'POST':
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('post_new', pk=post.id)

    else:
        c_form = ContactForm()

    context = {'post': post,'c_form':c_form,}


    return render(request,'base/post_new.html',context)


class ContactView(SuccessMessageMixin,FormView):
    template_name = 'base/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'MESAJINIZ İLETİLMİŞTİR TEŞEKKÜRLER'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)