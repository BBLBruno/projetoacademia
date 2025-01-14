from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import *

# Página inicial
def home(request):
    return render(request, "index.html")
    
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
