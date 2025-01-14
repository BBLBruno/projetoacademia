from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),

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
