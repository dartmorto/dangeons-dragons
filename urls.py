from django.urls import path
from dnd.masterspage import views

urlpatterns=[
    path("master/", views.MasterListView.as_view(), name="master_list"),

    path("master/<int:pk>/", views.MasterDetailView.as_view(), name="master_detail"),

    path("character/", views.CharacterListView.as_view(), name="character_list"),

    path("character/<int:pk>/", views.CharacterDetailView.as_view(), name="character_detail"),

    path("game/", views.GameListView.as_view(), name="game_list"),

    path("game/<int:pk>/", views.GameDetailView.as_view(), name="game_detail"),

    path("", views.HomeView.as_view(), name="index"),

    path("create/", views.MasterCreateView.as_view(), name="master_create"),

    path("master/<int:pk>/update/", views.MasterUpdateView.as_view(), name="master_update"),

    path("master/<int:pk>/delete/", views.MasterDeleteView.as_view(), name="master_delete"),

    path("character/create/", views.CharacterCreateView.as_view(), name="character_create"),

    path("character/<int:pk>/update/", views.CharacterUpdateView.as_view(), name="character_update"),

    path("character/<int:pk>/delete/", views.CharacterDeleteView.as_view(), name="character_delete"),

    path("game/create/", views.GameCreateView.as_view(), name="game_create"),

    path("game/<int:pk>/update/", views.GameUpdateView.as_view(), name="game_update"),

    path("game/<int:pk>/delete/", views.GameDeleteView.as_view(), name="game_delete"),



]