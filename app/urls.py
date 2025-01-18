from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# Usuário Aluno
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login e Logout
    path('login/', auth_views.LoginView.as_view(template_name="auth/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Página inicial
    path('', views.home, name='home'),

    # Página de administradores - Exibir todos os alunos
    path('perfil/alunos/', views.AdminStudentListView.as_view(), name='admin_student_list'),

    # Página de instrutores.
    path('instrutores/', views.InstructorListView.as_view(), name='instructor_list'),

    # URL para a área do aluno com os treinos
    path('area_do_aluno/', views.StudentTrainingListView.as_view(), name='student_training_list'),

    # URL para detalhes do treino
    path('treino/<int:pk>/', views.TrainingDetailView.as_view(), name='training_detail'),

    # Detalhes Treino
    path('treino/<int:pk>/', views.TrainingDetailView.as_view(), name='training_detail'),
    path('frequencia/<int:pk>/', views.AttendanceDetailView.as_view(), name='attendance_detail'),

    # Perfil de Usuário por tipo
    path('perfil/<str:role>/', views.UserProfileListView.as_view(), name='user_profile_list'),

    # Usuários
    path('usuarios/', views.UserListView.as_view(), name='user_list'),
    path('usuarios/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

    # Planos
    path('planos/', views.PlanListView.as_view(), name='plan_list'),
    path('planos/<int:pk>/', views.PlanDetailView.as_view(), name='plan_detail'),

    # Pagamentos
    path('pagamentos/', views.PaymentListView.as_view(), name='payment_list'),
    path('pagamentos/<int:pk>/', views.PaymentDetailView.as_view(), name='payment_detail'),

    # Registro de Frequência
    path('frequencia/', views.AttendanceView.as_view(), name='attendance'),

    # Treinos
    path('treinos/', views.TrainingListView.as_view(), name='training_list'),
    path('treinos/<int:pk>/', views.TrainingDetailView.as_view(), name='training_detail'),

    # Equipamentos
    path('equipamentos/', views.EquipmentListView.as_view(), name='equipment_list'),
    path('equipamentos/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment_detail'),

    # Exercícios
    path('exercicios/', views.ExerciseListView.as_view(), name='exercise_list'),
    path('exercicios/<int:pk>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
]