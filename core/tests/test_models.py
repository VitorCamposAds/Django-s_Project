from django.test import TestCase
from core.models import get_file_path
from unittest.mock import patch
import uuid
from fileinput import filename
from model_mommy import mommy



class GetFilePathTestCase(TestCase):
    def test_get_file_path(self):
        filename = 'teste.png'
        expected_result = '82f6f1d-9907-4ac7-a2a1-7adbba8326da.png'
        with patch('uuid.uuid4', return_value=expected_result.split('.')[0]):
            arquivo = get_file_path(None, filename)
            self.assertEqual(arquivo, expected_result)

class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str_servico(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)

class FeaturesTestCase(TestCase):

    def setUp(self):
        self.features = mommy.make('Features')

    def test_str(self):
        self.assertEquals(str(self.features), self.features.feature)



