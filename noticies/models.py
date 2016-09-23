from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

# Dades noticies
class categoria(models.Model):
	id_categoria = models.AutoField(primary_key=True)
	titol_categoria = models.CharField('Titol de la categoria',max_length=50)
	#pare_categoria = models.ForeignKey(categoria)

	def __unicode__(self):
		return u'%s' % (self.titol_categoria)

	class Meta:
		ordering = ['titol_categoria']

class post(models.Model):
	id_post = models.AutoField(primary_key=True)
	titol_post = models.CharField('Titol de la noticia',max_length=100)
	text_post = models.TextField('Contingut de la Noticia')
	autor_post = models.ForeignKey('auth.User')
	#auth.User, auth.Pass, auth.Address,... ja te el modul creat el propi Django
	creacio_post = models.DateTimeField(default=timezone.now)
	#afegir la linia 4 perque agafi la utilitat de hora del sistema
	#cod_categoria = models.ForeignKey(categoria)

	def __unicode__(self):
		return u'%s' % (self.titol_post)

	class Meta:
		ordering = ['creacio_post']

