from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Digite Seu Nome'
            }
        ),
        label='Primeiro Nome',
        help_text='Ajuda usuarios'
    )


    """ def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

     self.fields['first_name'].widget.attrs.update({
            'class': 'classe-a classe-b',
            'placeholder': 'Digite Seu Nome'

        }) """

    class Meta: 
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
    """   widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'classe-a classe-b',
                    'placeholder': 'Digite Seu Nome'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'classe-a classe-b',
                    'placeholder': 'Digite Seu Sobrenome'
                }
            ),
             'phone': forms.TextInput(
                attrs={
                    'class': 'classe-a classe-b',
                    'placeholder': 'Digite Seu Numero de Telefone'
                }
            )
            
        } """

    def clean(self) :
        #cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        return super().clean()
    
    def clean_first_name(self):
        first_name= self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Mensagem de erro 3',
                    code='invalid'
                )
            )
            
        
        return first_name
    
    
    