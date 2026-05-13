from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroSencilloForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None 
            field.widget.attrs['class'] = 'form-control'

class PerfilUsuarioForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'})
    )

    INTERESES_CHOICES = [
        ('arte', 'Arte y Creatividad'),
        ('deporte', 'Actividad Física'),
        ('tecnologia', 'Tecnología y Ciencia'),
        ('social', 'Interacción Social'),
        ('naturaleza', 'Naturaleza y Aire Libre'),
    ]
    intereses = forms.MultipleChoiceField(
        label='¿Qué temas te interesan?',
        choices=INTERESES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    HABILIDADES_CHOICES = [
        ('manual', 'Destreza Manual'),
        ('logica', 'Razonamiento Lógico'),
        ('comunicacion', 'Comunicación Asertiva'),
        ('resistencia', 'Resistencia Física'),
    ]
    habilidades = forms.MultipleChoiceField(
        label='¿Qué habilidades posees?',
        choices=HABILIDADES_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    NIVELES_CHOICES = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]
    nivel_experiencia = forms.ChoiceField(
        label='Nivel de experiencia general',
        choices=NIVELES_CHOICES
    )

    RASGOS_CHOICES = [
        ('introvertido', 'Introvertido'),
        ('extrovertido', 'Extrovertido'),
        ('analitico', 'Analítico'),
        ('espontaneo', 'Espontáneo'),
    ]
    rasgos = forms.MultipleChoiceField(
        label='¿Cómo te describes? (Rasgos)',
        choices=RASGOS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )