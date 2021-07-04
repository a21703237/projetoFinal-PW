from django.forms import ModelForm, forms

from .models import Contacto
from .models import Quiz
from .models import Comments


class ContactsForm(ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'nome',
            'apelido',
            'email',
            'telefone',
            'ano_nascimento'

        ]


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'

