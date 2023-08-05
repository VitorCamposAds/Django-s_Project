from django.db import models
import uuid #gera valores hexadecimais aleatórios
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser, BaseUserManager
'''
class UsuarioManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True.')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email

    objects = UsuarioManager()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_usuario_set',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_usuario_set',
    )

'''
# Create your models here.

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename
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