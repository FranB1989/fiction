from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import BlogEntryForm
from .models import BlogEntry

def user_has_group(user, group_names):
    return user.groups.filter(name__in=group_names).exists()

@login_required
@permission_required("blog.add_blogentry", raise_exception=True)
def create_blog_entry(request):
    form = BlogEntryForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        blog_entry = form.save(commit=False)
        blog_entry.author = request.user
        blog_entry.save()
        return redirect("blog:index")

    return render(request, "blog/create_blog.html", {"form": form})

def index_view(request):
    blog_entries = BlogEntry.objects.all().order_by("-date_published")
    paginator = Paginator(blog_entries, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    can_delete = user_has_group(request.user, ["Editor", "Administrador"])

    return render(request, "blog/index.html", {
        "page_obj": page_obj,
        "can_delete": can_delete,
    })

@login_required
@permission_required('blog.delete_blogentry', raise_exception=True)
def delete_blog_entry(request, pk):
    entry = get_object_or_404(BlogEntry, id=pk)

    if user_has_group(request.user, ["Administrador", "Editor"]):
        entry.delete()
        return redirect("blog:index")

    if user_has_group(request.user, ["Blogger"]) and entry.author == request.user:
        entry.delete()
        return redirect("blog:index")

    messages.error(request, "No tienes permisos para eliminar esta entrada.")
    return redirect("blog:index")
