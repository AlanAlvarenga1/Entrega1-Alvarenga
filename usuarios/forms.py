from django import forms

class lector_formulario(forms.Form):
    nombre_anonimo=forms.CharField(max_length=30)
    pais_de_residencia=forms.CharField(max_length=30)
    correo_electronico=forms.EmailField(max_length=50)

class bloggero_formulario(forms.Form):
    nombre=forms.CharField(max_length=30, required=True)
    apellido=forms.CharField(max_length=30, required=True)
    alias=forms.CharField(max_length=30, required=True)
    pais_de_residencia=forms.CharField(max_length=30, required=True)
    correo_electronico=forms.EmailField(max_length=50, required=True)

class empresa_formulario(forms.Form):
    nombre_de_empresa=forms.CharField(max_length=30)
    rubro=forms.CharField(max_length=30)
    cuit=forms.IntegerField()
    correo_electronico=forms.EmailField(max_length=50)

class lector_busqueda(forms.Form):
    nombre_anonimo=forms.CharField(max_length=30)

class bloggero_busqueda(forms.Form):
    alias=forms.CharField(max_length=30)

class empresa_busqueda(forms.Form):
    nombre_de_empresa=forms.CharField(max_length=30)