from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse

from django.views.generic import UpdateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
                          


from django.http import JsonResponse
from .models import Formation, Blog, Contact, FacturationMensuelle, Feedback
from .forms import TinyForm, identifierForm, exportForm, FormationUpdateForm, ContactForm, UserFeedbackForm
import stripe
from acccounts.models import LesAbonnee

from .helpers import get_api_key, get_file_online, update_file_online, get_all_formation
from time import sleep
import json
from edfManage import settings



stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    
    posts = Blog.objects.filter(publier=True).order_by('-date')
    return render(request, 'core/index.html', locals())


def blogDetail(request, slug, id):
    post = get_object_or_404(Blog, id=id, publier=True)
    return render(request, 'core/blogDetail.html', locals())



def confidentialite(request):
     return render(request, 'core/confidentialite.html')


def aide(request):
    Feedback.objects.all().delete()

    return render(request, 'core/aide.html')



def contact(request):
    data = json.loads(request.body) 
    print(data)
    
    Contact.objects.create(
        nom=data['form']['nom'], 
        prenom=data['form']['prenom'],
        email=data['form']['email'],
        phone=data['form']['phone'],
        message=data['form']['message'],
    )
    
    subject = "Nous avons reçu votre message avec succès"
    messages.success(request, subject)
    return JsonResponse({'success': True})







def desabonne(request):
    user = request.user
    if LesAbonnee.objects.filter(user=user).exists():
        LesAbonnee.objects.filter(user=user).delete()
        user.userprofile.status = 'inactif'
        user.userprofile.save()
        #print('vous etes desabonnez')

    return render(request, 'core/desabonne.html')



def abonne(request):
    return render(request, 'core/abonne.html')

def charge(request):
    
    try:
        amount = FacturationMensuelle.objects.all[0]
    except:
        amount = 20

    if request.method == 'POST':
        print('Data', request.POST)

        #amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nom'],
            source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='eur',
            description="Abonnement mensuiel sur le site"
            )
        user = request.user
        if LesAbonnee.objects.filter(user=user).exists():
            LesAbonnee.objects.filter(user=user).delete() 
            
        LesAbonnee.objects.create(user=user)
        user.userprofile.status = 'actif'
        user.userprofile.save()
    return redirect(reverse('list_formation')) #, args=[amount]))






@login_required
def userFeedback(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
       
        if form.is_valid():
            
            Feedback.objects.create(
                sujet = request.POST.get('sujet'),
                message = request.POST.get('message'),
                auteur = request.user
            )
            
            print(request.user)
            
            mess = 'Merci!! nous avons reçu votre message et nous vous répondrons promptement!'
            messages.success(request, mess)
            return HttpResponseRedirect('/liste-de-formations-edof/')
            
    else:
        form = UserFeedbackForm()
    return render(request, 'core/userFeedback.html', {'form': form})






"""
def get_key(request):
    #get_all_stocks_url()
    user = request.user
    key = get_api_key('marc-eric@leseducacteurs.fr','Lpdeamesdemarches@2020')
    data = get_file_online('FormationTEST1',key)

    Formation.objects.create(
        user=user, 
        identifiant=data['shortId'],
        point_fort=data['goal'],
        contenu=data['content'],
        objectif=data['contentSummary'],
        resultat_attendu=data['expectedResults']
    )

    print(key)
    return JsonResponse({'status' : 200, 'key': key})
"""



@login_required
def formulaire(request):
    formations = Formation.objects.all()
    form = TinyForm()
    return render(request, 'core/formulaire.html', locals())





@login_required
def getFormation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = identifierForm(request.POST)
        #print(form)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            id_formation = request.POST.get('id_formation')
            #print("it work!!")
            

            
            user = request.user
            key = get_api_key(username, password)
            if 'null' in str(key):
                messages.success(request, f'Desolé!! la connection a echoué.')
                return HttpResponseRedirect('/importation-de-formation-depuis-edof/')

            data = get_file_online(id_formation, key)
            if 'null pas reçu' == str(data):
                messages.success(request, f"Desolé!! l'importation' a echoué.")
                return HttpResponseRedirect('/importation-de-formation-depuis-edof/')

            if Formation.objects.filter(user=user, identifiant=data['shortId']).exists():
                formation = Formation.objects.get(user=user, identifiant=data['shortId'])
                formation.objectif = data['goal']
                formation.contenu = data['content']
                formation.point_fort = data['contentSummary']
                formation.resultat_attendu = data['expectedResults']
                formation.save(update_fields=['point_fort', 'contenu', 'objectif', 'resultat_attendu'])

            Formation.objects.create(
                user=user, 
                identifiant=data['shortId'],
                objectif=data['goal'],
                contenu=data['content'],
                point_fort=data['contentSummary'],
                resultat_attendu=data['expectedResults']
            )

            

            return HttpResponseRedirect('/liste-de-formations-edof/')
           

    # if a GET (or any other method) we'll create a blank form
    else:
        form = identifierForm()
    return render(request, 'core/getFormation.html', {'form': form})


@login_required
def getAllFormation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = exportForm(request.POST)
        #print(form)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            #print(username)
            
            #user = request.user
            key = get_api_key(username, password)
            if 'null' in str(key):
                messages.success(request, f'Desolé!! la connection a echoué.')
                return HttpResponseRedirect('/importation-de-catalogue-depuis-edof/')
            
            datas = get_all_formation(key)
            if 'null pas reçu' == str(datas):
                messages.success(request, f"Desolé!! l'importation' a echoué.")
                return HttpResponseRedirect('/importation-de-catalogue-depuis-edof/')

            #print(datas)
            user = request.user

            for data in list(datas):
                if Formation.objects.filter(user=user, identifiant=data['shortId']).exists():
                    formation = Formation.objects.get(user=user, identifiant=data['shortId'])
                    formation.objectif = data['goal']
                    formation.contenu = data['content']
                    formation.point_fort = data['contentSummary']
                    formation.resultat_attendu = data['expectedResults']
                    formation.save(update_fields=['object', 'contenu', 'point_fort', 'resultat_attendu'])


                Formation.objects.create(
                    user=user, 
                    identifiant=data['shortId'],
                    objectif=data['goal'],
                    contenu=data['content'],
                    point_fort=data['contentSummary'],
                    resultat_attendu=data['expectedResults']
                )
            
            return HttpResponseRedirect('/liste-de-formations-edof/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = exportForm()
    return render(request, 'core/getAllFormation.html', {'form': form})




@login_required
def listFormation(request):
    formations = Formation.objects.filter(user=request.user).order_by('-id')
    return render(request, 'core/listFormation.html', locals())



@login_required
def detailFormation(request, id):
    formation = get_object_or_404(Formation, id=id)
    print(formation)
    return render(request, 'core/detailFormation.html', locals())


@login_required
def updateFormation(request, id):
    obj = Formation.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        formation = FormationUpdateForm(request.POST,
                             instance=obj)
        if formation.is_valid():
            formation.save()
            messages.success(request, f'votre formation a bien ete mis à jour')
            return redirect('list_formation')
    else:
        formation = FormationUpdateForm(instance=obj)
        print(formation)
        
    return render(request, 'core/formulaire.html', locals())


@login_required
def exportPage(request, id):
    formation = get_object_or_404(Formation, id=id)
    form = exportForm()
    #print(formation)
    return render(request, 'core/exportPage.html', locals())
 

@login_required
def exportFile(request, id):
    formation = get_object_or_404(Formation, id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        id_formation = formation.identifiant
        print(username, id_formation)
        
        key = get_api_key(username, password)
        data = get_file_online(id_formation, key)
        #print(data['goal'])
        data['goal'] = formation.objectif
        data['content'] = formation.contenu
        data['contentSummary'] = formation.point_fort
        data['expectedResults'] = formation.resultat_attendu

        result = update_file_online(data,id_formation,key)
        if f"Fiche {id_formation} modifiée avec succès" in result:
            formation.mis_a_jour = True
            formation.save
        
        messages.success(request, f'{resul}')

    return redirect(reverse('list_formation'))




@login_required
def choix_status(request, id):
    formation = Formation.objects.get(id=id, user=request.user)
    return render(request, 'core/choix_status.html', locals())


  

@login_required
def deleteFormation(request, id):
    Formation.objects.filter(id=id).delete()
    return redirect(reverse('list_formation'))
