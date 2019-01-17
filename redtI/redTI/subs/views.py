from django.shortcuts import render
from django.views import generic
from .models import Subrediti, Thread, Post, Subscription
from .form import CreatePostForm, CreateThreadForm

class SubreditisView(generic.ListView):
    template_name = 'subs/subreditis.html'
    model = Subrediti
    context_object_name = 'subreditis'

class SubreditiDetailView(generic.DetailView):
    template_name = 'subs/sibrediti.html'
    model = Subrediti

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subscription, created = Subscription.objects.get_ot_create(user=self.request.user, subrediti=self.object)
        context['susbcribed'] = True if subscription.subscribed else False
        return context


class CreateSubreditiViews(generic.CreateViews):
    model = Subrediti
    template_name = 'subs/create_sub.html'
    fields = ['title', 'description']
    success_url = reverse_lazy['common:home']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object,creator_id = self.request.user.id
        slug = self.object.title
        slug = slug.replace(' ', '-')
        self.object.slug = slug
        self.object.save
        return super(generic.edit,ModelFormMixin)


class ThreadDetailView(generic.DetailView):
    template_name = 'subs/thread.html'
    model =  Thread


class CreateThreadView(generic.CreateView):
    template_name = 'subs/create_thread.html'
    model = Thread
    form_class = CreateThreadForm

    def get_initial(self):
        self.subrediti = self.request.GET.get('sub', None) #get (min) é pq estamos recebendo um dicionario e GET url
        return { #passa argumentos para a funçao init
            'subrediti': Subrediti.objects.get(id=self.subrediti)
            'author':self.request.user
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread'] = Thread.objects.get(id=self.thread)
        return context
    
    def get_success_url(self):
        subrediti = subrediti.objects.get(id=self.subrediti)
        return reverse_lazy('subs:subrediti', kwargs={'slug': subrediti.slug})


class CreatePostView(generic.CreateView):
    template_name = 'subs/create_post.html'
    model = Post
    form_class = CreatePostForm

    def get_initial(self):
        self.thread = self.request.GET.get('thread', None) #caso não tenha nada pass none
        return {
            'thread': Thread.objects.get(id=self.thread),
            'author': self.request.user,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread'] = Thread.objects.get(id=self.thread)
        return context

    def get_success_url(self):
        thread = Thread.objects.get(id=self.thread)
        return reverse_lazy('subs:thread', kwargs={'pk': thread.pk})

class DeletePostView(generic.DeleteView):
    template_name = 'subs/post_confirm_delete.html'
    model = Post
    success_url = 'home'