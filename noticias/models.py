from django.db import models

# Categoria: filho, Model: pai
class Categoria(models.Model): # () - Categoria extends Model
    nome = models.CharField(max_length=80, null=False, blank=False)
    # max lenght: número limite de caracteres
    # null: nenhuma informação
    # blank: string vazia " "
    def __str__(self): # def: método (Dentro da classe)
        return f"Categoria [nome={self.nome}]"

class Autor(models.Model):
    # O campo 'id' com chave primária (Primary Key) é criado
    # automaticamente pelo Django, a menos que você defina um.
    # Se quiser ser explícito e refletir INT(11), pode fazer:
    # id = models.AutoField(primary_key=True)
    # Mas é mais comum e recomendado deixar o padrão.
    nome = models.CharField(max_length=80, null=False, blank=False)
    perfil = models.TextField(max_length=400, null=False, blank=False)
    def __str__(self):
        return self.nome + self.perfil

class Noticia(models.Model):
    titulo = models.CharField(max_length=90, null=False, blank=False)
    conteudo = models.TextField(null=False, blank=False)
    data_publicacao = models.DateTimeField(auto_now=True, null=False, blank=False)
    destaque = models.CharField(max_length=5 , choices=[
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5') # <--- MUST BE ADDED TO CHOICES
    ],default='5') # <--- DEFAULT VALUE SET HERE
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", null=False, blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='noticias_autor', null=False)  # nome do relacionamento reverso (autor.noticias.all())
    #Relacionamento N-1(Muitas Noticias para um Autor)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias_categoria', null=False)
    def __str__(self):
        return self.titulo

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