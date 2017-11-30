from django.shortcuts import render
from main.models import Post

# Create your views here.
def show_main(request):
	post = Post.objects.all().order_by('-posted_at')
	return render(request, 'index.html', {'post': post})

def main_detail(request, pk):
	post = Post.objects.get(pk=pk)
	address = "http://ubuntu.poapper.com:33333/admin/main/post/"+"{{ post.pk }}"
	return render(request, 'main_detail.html', {'post':post,'address':address})