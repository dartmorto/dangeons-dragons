from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.http import HttpResponse
from django.shortcuts import render

from dnd.masterspage.models import *

def index(request):
    pass
class HomeView(TemplateView):
    template_name = "MastersNetwork/index.html" 

class MasterListView(ListView):
    model = Master
    quetryset = Master.objects.all()
    template_name = "MastersNetwork/master_list.html"

class MasterDetailView(DetailView):
    model = Master
    template_name = "MastersNetwork/master_detail.html"

class MasterCreateView(CreateView):
    model = Master
    fields = ["name"]
    success_url = reverse_lazy("master_list")

class MasterUpdateView(UpdateView):
    model = Master
    fields = ["name"]
    
    def get_success_url(self):
        return reverse_lazy("master_detail", kwargs={"pk": self.master.id})
    
class MasterDeleteView(DeleteView):
    model = Master
    success_url = reverse_lazy("master_list")

class CharacterListView(ListView):
    model = Character
    quetryset = Character.objects.all()
    template_name = "MastersNetwork/character_list.html"

class CharacterDetailView(DetailView):
    model = Character
    template_name = "MastersNetwork/character_detail.html"

class CharacterCreateView(CreateView):
    model = Character
    fields = ["name", "master"]
    success_url = reverse_lazy("character_list")

class CharacterUpdateView(UpdateView):
    model = Character
    fields = ["name", "master"]
    
    def get_success_url(self):
        return reverse_lazy("character_detail", kwargs={"pk": self.character.id})
    
class CharacterDeleteView(DeleteView):
    model = Character
    success_url = reverse_lazy("character_list")

class GameListView(ListView):
    model = Game
    quetryset = Game.objects.all()
    template_name = "MastersNetwork/game_list.html"

class GameDetailView(DetailView):
    model = Game
    template_name = "MastersNetwork/game_detail.html"

class GameCreateView(CreateView):
    model = Game
    fields = ["name", "master"]
    success_url = reverse_lazy("game_list")

class GameUpdateView(UpdateView):
    model = Game
    fields = ["name", "master"]
    
    def get_success_url(self):
        return reverse_lazy("game_detail", kwargs={"pk": self.game.id})
    
class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy("game_list")

class CutsceneListView(ListView):
    model = Cutscene
    quetryset = Cutscene.objects.all()
    template_name = "MastersNetwork/cutscene_list.html"

class CutsceneDetailView(DetailView):
    model = Cutscene
    template_name = "MastersNetwork/cutscene_detail.html"

class CutsceneCreateView(CreateView):
    model = Cutscene
    fields = ["name", "master", "image", "audio"]
    success_url = reverse_lazy("cutscene_list")

class CutsceneUpdateView(UpdateView):
    model = Cutscene

    fields = ["name", "master", "image", "audio"]
    
    def get_success_url(self):
        return reverse_lazy("cutscene_detail", kwargs={"pk": self.cutscene.id})
    
class CutsceneDeleteView(DeleteView):
    model = Cutscene
    success_url = reverse_lazy("cutscene_list") 





# Create your views here.
