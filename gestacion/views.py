# gestacion/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Madre, Parto, RecienNacido
from .forms import MadreForm, PartoForm, RNForm

def home(request):
    return render(request, "home.html")

# ===== MADRE =====
class MadreList(LoginRequiredMixin, ListView):
    model = Madre
    paginate_by = 10
    template_name = "madre/list.html"

class MadreCreate(LoginRequiredMixin, CreateView):
    model = Madre
    form_class = MadreForm
    success_url = reverse_lazy("madre_list")
    template_name = "madre/form.html"

class MadreUpdate(LoginRequiredMixin, UpdateView):
    model = Madre
    form_class = MadreForm
    success_url = reverse_lazy("madre_list")
    template_name = "madre/form.html"

class MadreDelete(LoginRequiredMixin, DeleteView):
    model = Madre
    success_url = reverse_lazy("madre_list")
    template_name = "confirm_delete.html"

# ===== PARTO =====
class PartoList(LoginRequiredMixin, ListView):
    model = Parto
    paginate_by = 10
    template_name = "parto/list.html"

class PartoCreate(LoginRequiredMixin, CreateView):
    model = Parto
    form_class = PartoForm
    success_url = reverse_lazy("parto_list")
    template_name = "parto/form.html"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.registrado_por = self.request.user
        return super().form_valid(form)

class PartoUpdate(LoginRequiredMixin, UpdateView):
    model = Parto
    form_class = PartoForm
    success_url = reverse_lazy("parto_list")
    template_name = "parto/form.html"

class PartoDelete(LoginRequiredMixin, DeleteView):
    model = Parto
    success_url = reverse_lazy("parto_list")
    template_name = "confirm_delete.html"

# ===== RECIÉN NACIDO =====
class RNList(LoginRequiredMixin, ListView):
    model = RecienNacido
    paginate_by = 10
    template_name = "rn/list.html"

class RNCreate(LoginRequiredMixin, CreateView):
    model = RecienNacido
    form_class = RNForm
    success_url = reverse_lazy("rn_list")
    template_name = "rn/form.html"

class RNUpdate(LoginRequiredMixin, UpdateView):
    model = RecienNacido
    form_class = RNForm
    success_url = reverse_lazy("rn_list")
    template_name = "rn/form.html"

class RNDelete(LoginRequiredMixin, DeleteView):
    model = RecienNacido
    success_url = reverse_lazy("rn_list")
    template_name = "confirm_delete.html"
