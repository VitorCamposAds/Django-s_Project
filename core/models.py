from django.db import models
import uuid #gera valores hexadecimais aleatórios
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _




def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.

class Base(models.Model):
    criados = models.DateField(_('Criação'), auto_now_add=True)
    modificado = models.DateField(_('Atualização'), auto_now=True)
    ativo = models.BooleanField(_("Ativo?"), default=True)

    class Meta:
        abstract=True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', _('Engranagem')),
        ('lni-stats-up', _('Gráfico')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
    )
    servico = models.CharField(_("Serviço"), max_length=100)
    descricao = models.TextField(_("Descrição"), max_length=200)
    icone = models.CharField(_("Icone"), max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField(_('cargo'), max_length=100)

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField(_('nome'), max_length=100)
    cargo = models.ForeignKey(Cargo, verbose_name=_("Cargo"), on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    imagem = StdImageField(_('Imagem'), upload_to=get_file_path, variations={'thumb' :{'width': 350, 'height': 350, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twiter = models.CharField('Twiter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')

    def __str__(self):
        return self.nome

class Features(Base):
    ICONE_CHOICES = (
        ('lni-cog', _('Engranagem')),
        ('lni-laptop-phone', _('Laptop')),
        ('lni-leaf', _('Folha')),
        ('lni-layers', _('Design')),
        ('lni-rocket', _('Foguete')),
    )
    feature = models.CharField(_("Feature"), max_length=50)
    descricao = models.TextField(_("Descrição"), max_length=200)
    icone = models.CharField(_("Icone"), max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.feature