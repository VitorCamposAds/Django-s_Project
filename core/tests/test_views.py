from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexView(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Paula Fernandes',
            'email': "vitorbeatle@gmail.com",
            'assunto': "Meu assunto",
            'mensagem': 'Minha mensagem'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Paula Fernades',
            'assunto': "Meu assunto"
        }
        request = self.client.post(reverse_lazy('index'), data=dados)  # corrigido para dados
        self.assertEquals(request.status_code, 200)




