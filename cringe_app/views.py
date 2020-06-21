from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from .forms import ExtendedUserCreationForm, ThreadForm, ReplyForm
from .models import Thread, Reply

# Create your views here.
def index(request):
    form = ThreadForm()

    threads = Thread.objects.all().order_by('-date_created')

    context = {'form':form, 'threads':threads }

    return render(request, 'cringe_app/index.html', context)

@require_POST
def new_thread(request):
    form = ThreadForm(request.POST)
     
    thread = form.save(commit=False)

    thread.user = request.user
    thread.save()
     
    return redirect('index')

def register(request):
    if request.method == 'POST':
    
        form = ExtendedUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
    
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)

            return redirect('index')
    else:
        form = ExtendedUserCreationForm()

    context = {'form': form }

    return render(request, 'cringe_app/register.html', context)

def thread(request, thread_id):
    thread = Thread.objects.get(pk=thread_id)
    
    if request.method == 'POST':
        form = ReplyForm(request.POST)

        if form.is_valid():
            reply = form.save(commit=False)

            reply.thread = thread
            reply.user = request.user

            reply.save()

            return redirect('thread', thread_id=thread.id)
    else:
        form = ReplyForm()

    context = {'thread':thread, 'form':form }

    return render(request, 'cringe_app/thread.html', context)