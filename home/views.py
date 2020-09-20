from django.shortcuts import render, HttpResponse
from home.models import Task


# Create your views here.
def home(request):
    context = {'success': False, 'name': 'Evans'}
    if request.method == "POST":
        # Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title + desc)
        ins = Task(taskDesc=desc, taskTitle=title)
        ins.save()
        context = {'success': True}

    # return HttpResponse('works')
    return render(request, 'index.html', context)


def tasks(request):
    allTasks = Task.objects.all()
    print(allTasks)
    # for item in allTasks:
    #     print(item)
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)
    # return HttpResponse('works')
 