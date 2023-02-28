from django.shortcuts import render, get_object_or_404

from .models import Class
from teachers.models import Teacher
from students.models import Student

from django.db.models import Q

# Create your views here.

def class_view(request, pk=None) -> render:
    if pk:
        template = 'class_detail.html'
        class_ = get_object_or_404(Class, pk=pk)
        context = {
            'class': class_,
        }
    else:
        template = 'classes.html'
        classes = Class.objects.all()
        teachers = Teacher.objects.all()
        context = {
            'classes': classes,
            'teachers': teachers,
        }
        
    return render(request=request, template_name=template, context=context)
    
    
def class_delete(request, pk) -> render:
    template = 'classes.html'
    
    class_ = get_object_or_404(Class, pk=pk)
    
    class_.delete()
    
    classes = Class.objects.all()
        
    context = {
        'classes': classes,
    }
    
    return render(request=request, template_name=template, context=context)
    
def change_teacher(request, pk, tpk) -> render:
    template = 'classes.html'

    
    class_ = get_object_or_404(Class, pk=pk)
    teacher = get_object_or_404(Teacher, pk=tpk)
    
    class_.teacher = teacher
    class_.save()
    
    # class_ = Class.objects.filter(pk=pk).update(teacher=teacher)
    
    classes = Class.objects.all()
    teachers = Teacher.objects.all()

    # teachers = Teacher.objects.filter(Q(pk__lte=3))
    
    context = {
        'classes': classes,
        'teachers': teachers,
    }

    return render(request=request, template_name=template, context=context)

def class_with_students(request):
    return render(request=request, template_name='class_with_students.html', context={'classes': Class.objects.all()})

# def show_classes_teacher(request, pk=None) -> render:
#     if pk:
#         template = 'classes_with_teachers_detail.html'
#         class_ = get_object_or_404(ClassWithTeacher, pk=pk)
#
#         teacher_first_name = []
#         q_ = Q(teacher__first_name='Кравец') | Q(teacher__first_name='Макаренко')
#
#
#         for teacher_first_name_item in ClassWithTeacher.objects.filter(teacher__first_name='Кравец').prefetch_related().values('teacher__first_name', 'teacher__last_name'):
#         # for teacher_first_name_item in ClassWithTeacher.objects.filter().prefetch_related().values('teacher__first_name', 'teacher__last_name'):
#         # for teacher_first_name_item in ClassWithTeacher.objects.filter().prefetch_related().values('teacher__first_name', 'teacher__last_name').distinct():
#             teacher_first_name.append(teacher_first_name_item)
#
#         context = {
#             'class': class_,
#             'teacher_first_name': teacher_first_name,
#         }
#     else:
#         template = 'classes_with_teachers.html'
#
#
#         # class_.teacher = teacher
#         # class_.save()
#
#         # class_ = Class.objects.filter(pk=pk).update(teacher=teacher)
#
#         classes = ClassWithTeacher.objects.all()
#         teachers = Teacher.objects.all()
#
#
#
#         # teachers = Teacher.objects.filter(Q(pk__lte=3))
#
#         context = {
#             'classes': classes,
#             'teachers': teachers,
#         }
#
#     return render(request=request, template_name=template, context=context)