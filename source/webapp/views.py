from django.shortcuts import render


# Create your views here.

def index_view(request):
    return render(request, "index.html")


def create_solution(request):
    first = int(request.POST.get("first"))
    second = int(request.POST.get("second"))
    if request.method == "GET":
        return render(request, "index.html")
    else:
        if request.POST.get("solution") == "add":
            result = f"{first} + {second} = {first + second}"
        elif request.POST.get("solution") == "subtract":
            result = f"{first} - {second} = {first - second}"
        elif request.POST.get("solution") == "multiply":
            result = f"{first} * {second} = {first * second}"
        else:
            result = f"{first} / {second} = {first / second}"
        context = {
            "solution": result
        }
        return render(request, "solution.html", context)
