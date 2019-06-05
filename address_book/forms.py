from django import forms
from .models import Person, Email, Phone


# def validate_first_name(str):
#     if any(char.isdigit() for char in str):
#         raise forms.ValidationError('Pole Imię musi zawierać tylko litery')


# def validate_name(str):
#     if any(char.isdigit() for char in str):
#         raise forms.ValidationError('Pole Imię i Nazwisko mogą zawierać tylko litery')


# def validate_phone(str):
#     if any(char.isalpha() for char in str):
#         raise forms.ValidationError('Telefon musi zawierać tylko cyfry')


class PersonForm(forms.ModelForm):

    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')

    class Meta:
        model = Person
        fields = '__all__'

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError('Pole Imię może zawierać tylko litery')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if any(char.isdigit() for char in last_name):
            raise forms.ValidationError('Pole Nazwisko może zawierać tylko litery')
        return last_name

class PhoneForm(forms.ModelForm):

    phone = forms.IntegerField(label='Telefon', required=False)

    class Meta:
        model = Phone
        fields = ['phone']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not Phone.objects.filter(phone=phone).exists() or not phone:
            return phone
        raise forms.ValidationError('Podany telefon już widnieje w bazie')


class EmailForm(forms.ModelForm):

    email = forms.EmailField(label='Email', required=False)

    class Meta:
        model = Email
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not Email.objects.filter(email=email).exists() or not email:
            return email
        raise forms.ValidationError('Podany email już widnieje w bazie')

