from django.urls import path

from .views import index, abonne, confidentialite, choix_status, aide, blogDetail, deleteFormation, contact, charge, desabonne,  formulaire, exportFile, exportPage, getAllFormation, updateFormation, listFormation, detailFormation, getFormation, userFeedback



urlpatterns = [
    path('', index, name='index'),
    path('envoie-de-message/', contact, name='contact'),
    path('envoie-de-feedback/', userFeedback, name='user_feedback'), 
    path('abonnement/', abonne, name='abonnement'),
    path('post-detail/<slug:slug>/<int:id>/', blogDetail, name='post_detail'),
    path('desabonnement/', desabonne, name='desabonnement'),
    path('tous-comprendre-sur-mon-compte-formation-des-organismes-de-formation/', aide, name='aide'),
    path('confidentialite/', confidentialite, name='confidentialite'),
    path('reediter-une-formulaire-edof/', formulaire, name='formulaire'),
    path('liste-de-formations-edof/', listFormation, name='list_formation'),
    path('previsualiser-une-formation-dans-edof/<int:id>/', detailFormation, name='detail_formation'),
    path('choix-status/<int:id>/', choix_status, name='choix_status'),
    path('supprimer-une-formation-edof/<int:id>/', deleteFormation, name='delete_formation'),
    path('modifier-une-formation-dans-edof/<int:id>/update',updateFormation, name='update_formation'), 
    path('importation-de-formation-depuis-edof/', getFormation, name='get_formation'),
    path('importation-de-catalogue-depuis-edof/', getAllFormation, name='get_all_formations'),
    path('enregistrer-une-formation-dans-edof/<int:id>/', exportFile, name='export_file'),
    path('formulaire-envoie-formation-dans-edof/<int:id>/', exportPage, name='export_page'),  
    path('charge/', charge, name='charge'),
    
]