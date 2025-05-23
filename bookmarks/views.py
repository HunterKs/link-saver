from django.shortcuts import render
from .models import Bookmark
from .forms import BookmarkForm, CustomUserCreationForm, EmailAuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .utils import fetch_title_and_favicon, fetch_summary, resummarize_summary
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect

def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_bookmarks')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_bookmarks')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
@login_required
def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            # Fetch title and favicon
            title, favicon_url = fetch_title_and_favicon(bookmark.url)
            bookmark.title = title
            bookmark.favicon_url = favicon_url
            # Fetch summary
            bookmark.summary = fetch_summary(bookmark.url)
            bookmark.save()
            return redirect('list_bookmarks')
    else:
        form = BookmarkForm()
    return render(request, 'bookmarks/add_bookmark.html', {'form': form})

@login_required
def list_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookmarks/list_bookmarks.html', {'bookmarks': bookmarks})

def custom_logout(request):
    if request.user.is_authenticated:
        request.user.is_online = False
        request.user.save()
    logout(request)
    return redirect('/accounts/login/')  

@login_required
def resummarize_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id, user=request.user)
    new_summary = resummarize_summary(bookmark.summary)
    bookmark.summary = new_summary
    bookmark.save()
    return redirect('list_bookmarks')