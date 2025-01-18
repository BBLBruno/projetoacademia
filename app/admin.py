from django.contrib import admin
from .models import *

# Customização do modelo User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "CPF", "role", "is_active")
    search_fields = ("username", "email", "CPF")
    list_filter = ("role", "is_active", "is_staff")
    ordering = ("username",)

# Admin para o modelo Plan
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "duration_in_months", "price")
    search_fields = ("name",)
    ordering = ("name",)

# Admin para o modelo Payment
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "plan", "status", "due_date", "payment_date")
    search_fields = ("user__username", "plan__name", "status")
    list_filter = ("status", "due_date")
    ordering = ("due_date",)

# Admin para o modelo Attendance
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "check_in_time")
    search_fields = ("user__username", "date")
    list_filter = ("date",)
    ordering = ("date", "check_in_time")

# Admin para o modelo FichaDeTreino
@admin.register(FichaDeTreino)
class FichaDeTreinoAdmin(admin.ModelAdmin):
    list_display = ("training", "exercise", "repetitions", "rest_time")
    search_fields = ("training__user__username", "exercise__name")
    list_filter = ("training__user__username", "exercise__name")
    ordering = ("training", "exercise")

# Inline para a ficha de treino
class FichaDeTreinoInline(admin.TabularInline):
    model = FichaDeTreino
    extra = 1  # Define o número de fichas de treino extras que podem ser adicionadas

# Admin para o modelo Training
@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ("user", "instructor", "created_at")
    search_fields = ("user__username", "instructor__username")
    list_filter = ("created_at",)
    ordering = ("created_at",)
    inlines = [FichaDeTreinoInline]

# Admin para o modelo Equipment
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    ordering = ("name",)

# Admin para o modelo Exercise
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "equipment")
    search_fields = ("name", "equipment__name")
    list_filter = ("equipment",)
    ordering = ("name",)
