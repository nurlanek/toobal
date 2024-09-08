from django.shortcuts import render, redirect


def index(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    return render(request, "main/index.html")