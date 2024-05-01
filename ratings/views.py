from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Restaurant, Review
from .forms import ReviewForm  


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('restaurant_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('restaurant_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('restaurant_list')

@login_required
def leave_review(request, restaurant_id):
    
    ...

@login_required
def search_view(request):
    query = request.GET.get('q')
    restaurants = Restaurant.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'restaurants': restaurants, 'query': query})


@login_required
def leave_review(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
            return redirect('restaurant_detail', restaurant_id=restaurant_id)
    else:
        form = ReviewForm()
    return render(request, 'ratings/leave_review.html', {'form': form, 'restaurant': restaurant})

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'ratings/restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    return render(request, 'ratings/restaurant_detail.html', {'restaurant': restaurant})

# views.py
def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.annotate(avg_rating=Avg('reviews__rating')).get(pk=restaurant_id)
    reviews = restaurant.reviews.all()
    return render(request, 'ratings/restaurant_detail.html', {'restaurant': restaurant, 'reviews': reviews})
