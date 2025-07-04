
# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth.decorators import login_required

# from .models import Task
# # Create your views here.
# @login_required(login_url='sign_in')
# def home(request):
#     tasks = Task.objects.filter(is_completed=False)
#     completed_tasks = Task.objects.filter(is_completed=True)
#     context = {
#             'tasks': tasks,
#             'completed_tasks' : completed_tasks,
#         }
#     return render(request, 'home.html', context)



# def addTask(request):
#     task = request.POST['task']
#     Task.objects.create(task=task)
#     return redirect('home')


# def mark_as_done(request, pk):
#     mark_as_done = get_object_or_404(Task, pk=pk)
#     mark_as_done.is_completed=True
#     mark_as_done.save()
#     return redirect('home')

# def mark_as_undone(request, pk):
#     mark_as_undone = get_object_or_404(Task, pk=pk)
#     mark_as_undone.is_completed=False
#     mark_as_undone.save()
#     return redirect('home')

# def deleteTask(request,pk):
#     task = get_object_or_404(Task, pk=pk)
#     task.delete()
#     return redirect('home')


# @login_required(login_url='sign_in')
# def edit(request, pk):
#     get_task = get_object_or_404(Task, pk=pk)

#     if request.method == 'POST':

#         new_task = request.POST['new_task']
#         get_task.task=new_task
#         get_task.save()
#         return redirect('home')
#     else:
#         context = {
#             'get_task': get_task,
#         }


#     return render(request, 'edit.html', {'get_task': get_task})

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.
@login_required(login_url='sign_in')
def home(request):
    # فقط تسک‌های کاربر جاری را نمایش بده
    tasks = Task.objects.filter(user=request.user, is_completed=False)
    completed_tasks = Task.objects.filter(user=request.user, is_completed=True)
    context = {
        'tasks': tasks,
        'completed_tasks' : completed_tasks,
    }
    return render(request, 'home.html', context)

@login_required(login_url='sign_in')  # اضافه کردن دکوراتور برای احراز هویت
def addTask(request):
    task = request.POST['task']
    # ایجاد تسک جدید و نسبت دادن به کاربر جاری
    Task.objects.create(task=task, user=request.user)
    return redirect('home')

@login_required(login_url='sign_in')
def mark_as_done(request, pk):
    # فقط تسک‌های کاربر جاری قابل تغییر هستند
    mark_as_done = get_object_or_404(Task, pk=pk, user=request.user)
    mark_as_done.is_completed = True
    mark_as_done.save()
    return redirect('home')

@login_required(login_url='sign_in')
def mark_as_undone(request, pk):
    # فقط تسک‌های کاربر جاری قابل تغییر هستند
    mark_as_undone = get_object_or_404(Task, pk=pk, user=request.user)
    mark_as_undone.is_completed = False
    mark_as_undone.save()
    return redirect('home')

@login_required(login_url='sign_in')
def deleteTask(request, pk):
    # فقط تسک‌های کاربر جاری قابل حذف هستند
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('home')

@login_required(login_url='sign_in')
def edit(request, pk):
    # فقط تسک‌های کاربر جاری قابل ویرایش هستند
    get_task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        new_task = request.POST['new_task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
    return render(request, 'edit.html', context)