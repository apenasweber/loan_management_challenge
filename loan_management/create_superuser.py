import os
from django.contrib.auth.models import User

# Define as informações do superusuário padrão
username = "admin"
email = "admin@example.com"
password = "admin123"

# Cria o superusuário se ele não existir
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)

# Imprime uma mensagem indicando a criação do superusuário
print("Superuser created successfully!")
