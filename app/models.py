from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(AbstractUser):
    CPF = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    date_of_birth = models.DateField(verbose_name="Data de Nascimento", null=True, blank=True)
    phone = models.CharField(max_length=15, verbose_name="Telefone")
    especialidade = models.CharField(max_length=255, blank=True, null=True)  # Novo campo
    address = models.TextField(verbose_name="Endereço")
    ROLE_CHOICES = [
        ("aluno", "Aluno"),
        ("instrutor", "Instrutor"),
        ("administrador", "Administrador"),
    ]

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Novo nome de reverso para o relacionamento
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Novo nome de reverso para o relacionamento
        blank=True,
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default="aluno")

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"  

# Plano de Adesão
class Plan(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome do Plano")
    duration_in_months = models.IntegerField(verbose_name="Duração (em meses)")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Planos" 

# Pagamento
class Payment(models.Model):
    STATUS_CHOICES = [
        ("pago", "Pago"),
        ("pendente", "Pendente"),
        ("atrasado", "Atrasado"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, verbose_name="Plano")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pendente")
    due_date = models.DateField(verbose_name="Data de Vencimento")
    payment_date = models.DateField(null=True, blank=True, verbose_name="Data de Pagamento")

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos" 

# Frequência
class Attendance(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Usuário")
    date = models.DateField(auto_now_add=True, verbose_name="Data")
    check_in_time = models.TimeField(auto_now_add=True, verbose_name="Horário de Check-in")

    def __str__(self):
        return f"Frequência de {self.user.username} - {self.date.strftime('%d/%m/%Y %H:%M')}"
    
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências" 

# Equipamento
class Equipment(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome do Equipamento")
    description = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"    

# Exercício
class Exercise(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome do Exercício")
    description = models.TextField(verbose_name="Descrição")
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, verbose_name="Equipamento")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Exercício"
        verbose_name_plural = "Exercício"

# Ficha de Treino
class TrainingSheet(models.Model):
    training = models.ForeignKey('Training', on_delete=models.CASCADE, verbose_name="Treino")
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, verbose_name="Exercício")
    series = models.IntegerField(default=12, verbose_name="Número de Séries")
    repetitions = models.IntegerField(default=12, verbose_name="Número de Repetições")
    rest_time = models.IntegerField(default=90, verbose_name="Tempo de Descanso (segundos)")

    def __str__(self):
        return f"{self.training.user.username} - {self.exercise.name}"
    
    class Meta:
        verbose_name = "Ficha de Treino"
        verbose_name_plural = "Fichas de Treino"

# Treino
class Training(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome do Treino")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Aluno")
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="treinos", verbose_name="Instrutor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    
    def __str__(self):
        return f"Treino de {self.user.username} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"
    
    class Meta:
        verbose_name = "Treinamento"
        verbose_name_plural = "Treinamentos"
