from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, Http404
from django.views import View
from .models import *
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

# View para exibir todos os treinos dos alunos
class StudentTrainingListView(View):
    def get(self, request):
        query = request.GET.get('username', '')  # Pega o nome do usuário digitado
        # Filtra todos os treinos, independentemente do usuário logado
        trainings = Training.objects.all()

        # Aplica o filtro se o nome de usuário for fornecido
        if query:
            trainings = trainings.filter(Q(user__username__icontains=query) | Q(user__email__icontains=query))
     
        return render(request, 'trainings/student_training_list.html', {'trainings': trainings})

# View para exibir todos os treinos dos alunos
class StudentTrainingListView(View):
    def get(self, request):
        query = request.GET.get('username', '')  # Pega o nome do usuário digitado
        # Filtra todos os treinos, independentemente do usuário logado
        trainings = Training.objects.all()

        # Aplica o filtro se o nome de usuário for fornecido
        if query:
            trainings = trainings.filter(Q(user__username__icontains=query) | Q(user__email__icontains=query))
     
        return render(request, 'trainings/student_training_list.html', {'trainings': trainings})

# View para exibir todos os alunos para o administrador
class AdminStudentListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'students/admin_student_list.html'
    context_object_name = 'students'
    
    # Redireciona o usuário não autenticado para a página de login
    login_url = '/login/'  # Substitua pelo caminho correto se necessário

    def get_queryset(self):
        # Apenas alunos (não administradores ou instrutores)
        return User.objects.filter(role='aluno')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Dados importantes para o relatório
        total_students = User.objects.filter(role='aluno').count()
        total_payments = Payment.objects.filter(status='pago').count()
        total_pending_payments = Payment.objects.filter(status='pendente').count()
        total_unpaid_payments = Payment.objects.filter(status='atrasado').count()

        context.update({
            'total_students': total_students,
            'total_payments': total_payments,
            'total_pending_payments': total_pending_payments,
            'total_unpaid_payments': total_unpaid_payments,
        })

        return context


# Class para exibir detalhes da frequência
class AttendanceDetailView(View):
    def get(self, request, pk):
        # Obtém o usuário pelo ID (pk)
        user = get_object_or_404(User, pk=pk)
        # Obtém todas as frequências do aluno
        attendances = Attendance.objects.filter(user=user)
        return render(request, 'attendance/detail.html', {'user': user, 'attendances': attendances})

# View para listar instrutores
class InstructorListView(View):
    def get(self, request):
        # Filtra os instrutores (assumindo que "role" é 'instrutor')
        instructors = User.objects.filter(role='instrutor')
        return render(request, "instructors/list.html", {"instructors": instructors})

# Página inicial
def home(request):
    return render(request, "index.html")

# Visualização de Perfil de Usuário (filtrado por tipo)
class UserProfileListView(View):
    def get(self, request, role):
        # Filtrando usuários pelo tipo de papel (role)
        users = User.objects.filter(role=role)
        return render(request, "users/profile_list.html", {"users": users, "role": role})
    
# Visualização de Usuários
class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, "users/list.html", {"users": users})

class UserDetailView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return render(request, "users/detail.html", {"user": user})

# Visualização de Planos
class PlanListView(View):
    def get(self, request):
        plans = Plan.objects.all()
        return render(request, "plans/list.html", {"plans": plans})

class PlanDetailView(View):
    def get(self, request, pk):
        plan = get_object_or_404(Plan, pk=pk)
        return render(request, "plans/detail.html", {"plan": plan})

# Visualização de Pagamentos
class PaymentListView(View):
    def get(self, request):
        payments = Payment.objects.select_related("user", "plan").all()
        return render(request, "payments/list.html", {"payments": payments})

class PaymentDetailView(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        return render(request, "payments/detail.html", {"payment": payment})

# Registro de Frequência
class AttendanceView(View):
    def post(self, request):
        user_id = request.POST.get("user_id")
        user = get_object_or_404(User, pk=user_id)
        Attendance.objects.create(user=user)
        return JsonResponse({"message": "Check-in registrado com sucesso!"})

# Visualização de Treinos
class TrainingListView(View):
    def get(self, request):
        trainings = Training.objects.select_related("user", "instructor").all()
        return render(request, "trainings/list.html", {"trainings": trainings})

class TrainingDetailView(View):
    def get(self, request, pk):
        training = get_object_or_404(Training, pk=pk)
        return render(request, "trainings/detail.html", {"training": training})

# Visualização de Equipamentos
class EquipmentListView(View):
    def get(self, request):
        equipments = Equipment.objects.all()
        return render(request, "equipments/list.html", {"equipments": equipments})

class EquipmentDetailView(View):
    def get(self, request, pk):
        equipment = get_object_or_404(Equipment, pk=pk)
        return render(request, "equipments/detail.html", {"equipment": equipment})

# Visualização de Exercícios
class ExerciseListView(View):
    def get(self, request):
        exercises = Exercise.objects.select_related("equipment").all()
        return render(request, "exercises/list.html", {"exercises": exercises})

class ExerciseDetailView(View):
    def get(self, request, pk):
        exercise = get_object_or_404(Exercise, pk=pk)
        return render(request, "exercises/detail.html", {"exercise": exercise})