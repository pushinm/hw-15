from django.urls import path

from teachers.urls import app_name

from .views import class_view, class_delete, change_teacher, class_with_students
# from classboard.views import filter_students_group

app_name = 'classes'

urlpatterns = [
    path('', class_view, name='class_view'),
    path('<int:pk>/', class_view, name='class_view'),
    path('delete/<int:pk>/', class_delete, name='class_delete'),
    path('with_students/', class_with_students, name='class_with_students'),
    # path('with_teacher/', show_classes_teacher, name='show_classes_teacher'),
    # path('with_teacher/<int:pk>', show_classes_teacher, name='show_classes_teacher'),
    # path('with_teacher', class_view, name='class_view'),
    path('change_teacher/<int:pk>/<int:tpk>', change_teacher, name='change_teacher'),
    # path('filter_group/', filter_students_group, name='filter_students_group'),
]
