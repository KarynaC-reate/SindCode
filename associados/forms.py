from django import forms

class AssociadoForm(forms.Form):
    GENERO_CHOICES = (
        ('', 'Escolha'),
        ('F', 'Mulher'),
        ('M', 'Homem'),
        ('NB', 'Não Binário'),
        ('O', 'Outro'),
        ('PND', 'Prefiro Não Declarar'),
    )
    nome_completo = forms.CharField(
        label="Nome completo",
        required=True, # Obrigatório
        max_length=100)
    nome_social = forms.CharField(
        label="Nome social (como você prefere ser chamado (a)",
        required=False, # Não obrigatório
        max_length=100
    )
    identidade_genero = forms.ChoiceField(
        label='Qual sua identidade de gênero?',
        choices=GENERO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    genero_outro = forms.CharField(
        label='Selecione "Outro" acima e especifique',
        max_length=100,
        required=False,
        help_text='Use apenas se a opção "Outro" tiver sido selecionada.'
    )
    data_nascimento = forms.DateField(
        label='Data de nascimento',
        required=True,
    )
    email = forms.CharField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}),
    )
    senha1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
    )

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome login",
        required=True,
        max_length=100,
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(),
    )