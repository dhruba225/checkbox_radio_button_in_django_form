from django import forms

g=[('Male','Male'),('Female','Female'),('Others','Others')]
c=[('python','python'),('django','django'),('api','api'),('selenium','selenium')]
class RegistrationFrom(forms.Form):
    Name=forms.CharField(max_length=100)
    Age=forms.IntegerField()
    Password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    Gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #courses=forms.MultipleChoiceField(choices=c)
    Courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    