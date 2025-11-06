from django.db import models
# Estudar o que é ORM (Object Relation Mapper)
# A classe é um conjunto de objetos
# Herança: Uma classse herda outra e implementa suas próprias características
# Filho(Pai) - utilizo o sinal de ( ) para herança
# Toda classe começa com letra Maiúscula(PascalCase)

class Categoria(models.Model):
    nome = models.CharField(max_length=80, null=False, blank=False)

    # max lenght: número limite de caracteres
    # null: nenhuma informação
    # blank: string vazia " "
    def __str__(self):
        return f"Categoria [nome={self.nome}]"

class Autor(models.Model):
    # O campo 'id' com chave primária (Primary Key) é criado
    # automaticamente pelo Django, a menos que você defina um.
    # Se quiser ser explícito e refletir INT(11), pode fazer:
    # id = models.AutoField(primary_key=True)
    # Mas é mais comum e recomendado deixar o padrão.
    nome = models.CharField(max_length=80, null=False, blank=False)

    perfil = models.TextField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nome + self.perfil

# Django ORM

# Python e Flask: SQLAlchemy
# Python e Django: Django ORM
# Java: Hibernate
# C#: Entity Framework
# PHP: Doctrine

# vantagem:
"""
    - Usar a linguagem de fluência
    - Migração (migrar de um banco MySQL para um SQLServer)
    - Menos erros (conexão, segurança entre outros)
    - Toolkit extra interação com banco de dados
"""
# desvantagem:
"""
    - Sistemas legados poder ser um problema
    - Iniciantes criar uma ilusão (não precisa estudar SQL)
"""


