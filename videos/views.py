from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Video
from django.db.models import Q


def home(request):
    vids = Video.objects.all()
    search_query = request.GET.get('q', '')
    if search_query:
        vids = vids.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    return render(request, 'videos/home.html', {'vids': vids, 'search_query': search_query})


def watch(request, id):
    video = get_object_or_404(Video, id=id)
    return render(request, 'videos/player.html', {'video': video})


@login_required
def upload(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('description')
        video = request.FILES.get('video')
        thumbnail = request.FILES.get('thumbnail')

        if not title or not video or not thumbnail:
            messages.error(request, "Title, Video, and Thumbnail are must-haves, baby! 😤")
            return redirect('upload')

        video_obj = Video.objects.create(
            title=title,
            description=desc,
            video=video,
            thumbnail=thumbnail,
            uploaded_by=request.user
        )
        video_obj.save()
        messages.success(request, "Your video is live! Time to shine, superstar! 🌟")
        return redirect('home')

    return render(request, 'videos/upload.html')