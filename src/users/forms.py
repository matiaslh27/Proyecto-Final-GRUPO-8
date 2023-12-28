from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2','email','telefono','domicilio','imagen_perfil']
        


"""        labels = {
            'first_name': 'Nombre',
            'last_name' : 'Apellido',
            'username' : 'Nombre de Usuario',
            'password1' : 'Contraseña',
            'password2' : 'Confirmar Contraseña',
        }"""