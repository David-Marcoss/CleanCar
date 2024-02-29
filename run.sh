#!/bin/bash

# espera o banco de dados ser iniciado
sleep 5

# Aplica as migrações do banco de dados
python manage.py migrate

# Inicia o servidor de desenvolvimento
python manage.py runserver 0.0.0.0:8000
