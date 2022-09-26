from django import forms
from . models import Formation, Contact
from tinymce.widgets import TinyMCE


class ContactForm(forms.ModelForm):
    #message = forms.CharField(label="", widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Qu'attendez vous de nous?" , "rows":4}))
    class Meta:
        model = Contact
        fields = ['nom','prenom', 'phone', 'email', 'message']
  

class TinyForm(forms.ModelForm):
    point_fort = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':30}))
    contenu = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':30}))
    objectif = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':30}))
    resultat_attendu = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':30}))
    
    
    class Meta:
        model = Formation
        fields = ('point_fort', 'contenu', 'objectif', 'resultat_attendu',)  #'__all__'
        #exclude = ('user', 'identifiant', 'fiche', 'update' )


class UserFeedbackForm(forms.Form):
    sujet = forms.CharField(label="sujet", max_length=50)
    message = forms.CharField(label="", widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Inscrivez ici votre avis, question, remarque, preocupation..." , "rows":4}))

  

class identifierForm(forms.Form):
    username = forms.EmailField(label='username', max_length=255)
    id_formation = forms.CharField(label='id_formation', max_length=255)
    password = forms.CharField(label='password', widget=forms.PasswordInput)



class exportForm(forms.Form):
    username = forms.EmailField(label='username', max_length=255)
    #id_formation = forms.CharField(label='id_formation', max_length=255)
    password = forms.CharField(label='password', widget=forms.PasswordInput)
  

    

class FormationUpdateForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['point_fort', 'contenu', 'objectif', 'resultat_attendu']

