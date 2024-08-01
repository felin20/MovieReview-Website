from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Movie, Userreview
from .forms import Regform, revform
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin



# Home views
def home(request):
    return render(request, 'home.html')

def home1(request):
    return render(request, 'home1.html')

# Search functionality
def search(request):
    q = request.GET.get('q', '')
    data = Movie.objects.filter(Moviename__icontains=q) if q else Movie.objects.all()
    return render(request, 'search.html', {'data': data})

# User login and registration views
def ulogin(request):
    return render(request, 'ulogin.html')

def clogin(request):
    return render(request, 'clogin.html')

def welcome(request):
    return render(request, 'welcome.html')

def movlist(request):
    mov = Movie.objects.all()
    return render(request, 'movlist.html', {'mov': mov})

def mdetail(request, Moviename):
    det = get_object_or_404(Movie, Moviename=Moviename)
    urev = Userreview.objects.filter(Moviename=det)  # Get reviews for the specific movie
    return render(request, 'mdet.html', {'det': det, 'urev': urev})


def register(request):
    if request.method == 'POST':
        form = Regform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = Regform()
    return render(request, 'regform.html', {'form': form})

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

@login_required
def adrev(request):
    if request.method == 'POST':
        form = revform(request.POST, request.FILES)
        if form.is_valid():
            user_review = form.save(commit=False)
            user_review.Username = request.user.username  # Set the username
            user_review.save()
            form.save_m2m()  # Save ManyToMany relationships
            messages.success(request, 'Review added successfully')
            return redirect('home')
    else:
        form = revform()
    return render(request, 'adrev.html', {'form': form})

@login_required
def my_reviews(request):
    user_reviews = Userreview.objects.filter(Username=request.user.username)
    return render(request, 'my_reviews.html', {'user_reviews': user_reviews})


@login_required
def editto(request, id):
    edit = get_object_or_404(Userreview, id=id)
    if request.method == 'POST':
        form = revform(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully')
            return redirect('home')
    else:
        form = revform(instance=edit)
    return render(request, 'editadrev.html', {'form': form, 'edit': edit})


@login_required
def todelete(request, id):
    td = get_object_or_404(Userreview, id=id)
    if request.method == 'POST':
        td.delete()
        messages.success(request, 'Review deleted successfully')
        return redirect('home')
    return render(request, 'todelete.html', {'td': td})


class MyReviewsView(LoginRequiredMixin, ListView):
    model = Userreview
    template_name = 'my_reviews.html'
    context_object_name = 'user_reviews'

    def get_queryset(self):
        # Ensure that the field name matches the one in your model
        return Userreview.objects.filter(Username=self.request.user.username)

@login_required
def edit_review(request, id):
    review = get_object_or_404(Userreview, id=id, Username=request.user.username)
    if request.method == 'POST':
        form = revform(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully')
            return redirect('myrev')  # Redirect to My Reviews page
    else:
        form = revform(instance=review)
    return render(request, 'edit_review.html', {'form': form})

@login_required
def delete_review(request, id):
    review = get_object_or_404(Userreview, id=id, Username=request.user.username)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully')
        return redirect('myrev')  # Redirect to My Reviews page
    return render(request, 'delete_review.html', {'review': review})
