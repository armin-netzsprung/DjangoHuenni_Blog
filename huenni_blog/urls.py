
from django.urls import path
from . import views

urlpatterns = [

    path('blog/', views.post_list, name='blog'),                                            # Liste aller Blogeinträge wird dargestellt
    path('post', views.post_list, name='post_list'),                                            # Liste aller Blogeinträge wird dargestellt
    path('post/title/<str:filter>',views.post_list_title, name='post_list_title'),  # Titel Auswahl bei der Liste berücksichtigen
    path('post/rubric/<str:filter>',views.post_list_rubric, name='post_list_rubric'),  # Titel Auswahl bei der Liste berücksichtigen
    path('post/category1/<str:filter>',views.post_list_category1, name='post_list_category1'),  # Kategorie Auswahl bei der Liste berücksichtigen
    
    path("post/neu/", views.post_create, name="post_create"),
    path("comment", views.AddComment, name="AddComment"),
    path("comment/<int:pk>/loeschen/", views.post_comment_delete, name="post_comment_delete"),                     # Löschen-Button wird gedrückt

    path("post/<int:pk>/", views.post_detail, name="post_detail"),                              # Deteilseite Anzeigen pk=PrivateKey sprich DS Nummer id
    path("post/<int:pk>/bearbeiten/", views.post_update, name="post_update"),                   # Editseite aufrufen
    path("post/<int:pk>/loeschen/", views.post_delete, name="post_delete"),                     # Löschen-Button wird gedrückt
    
]



