from django.views.generic import FormView
from .models import Servico, Funcionario, Features
import random
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _

def obter_features():
    all_features = Features.objects.all()
    num_features = len(all_features)
    half_num_features = num_features // 2

    random_features = random.sample(list(all_features), num_features)

    left_features = random_features[:half_num_features]
    right_features = random_features[half_num_features:]

    context = {}
    context['left_features'] = left_features
    context['right_features'] = right_features
    return context

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['features'] = Features.objects.order_by('?').all()

        # Chamando a função para obter as features aleatórias divididas
        features_context = obter_features()
        context.update(features_context)

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('Email enviado com sucesso!'))
        return super().form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar o e-mail'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
