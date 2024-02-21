from .models import *
from django import forms
class Quantityform(forms.ModelForm):
    class Meta():
        model=CartItem
        fields=['quantity']
        widgets={'quantity':forms.NumberInput(attrs={'value':model.quantity})}

class WilayatForm(forms.ModelForm):
    class Meta:
        model = Wilaya
        fields = ['name']
        # You can include additional fields here

class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ['name']
        # You can include additional fields here    
""" class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        widgets={
            'fullname':forms.TextInput(attrs={'class':'form-control'}),
            'numero':forms.NumberInput(attrs={'class':'form-control'}),
            'wilaya':forms.ModelChoiceField(queryset=Wilaya.objects.all()),
            'commune':forms.ModelChoiceField(queryset=Commune.objects.none()),
            } """
class OrderForm(forms.Form):
    wilaya = forms.ModelChoiceField(queryset=Wilaya.objects.all())
    commune = forms.ModelChoiceField(queryset=Commune.objects.none())       