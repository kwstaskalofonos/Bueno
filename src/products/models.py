from django.db import models

# Create your models here.
class Material(models.Model):
	SALTY = 'Αλμυρές'
	SWEET = 'Γλυκές'
	KREATIKA = 'Κρεατικά'
	TIRIA = 'Τυριά'
	LAXANIKA = 'Λαχανικα'
	DIAFORA = 'Διάφορα'
	MATERIAL_CHOICES = (
		(SALTY,'Αλμυρές'),
		(SWEET,'Γλυκές')
	)
	MATERIAL_CATEGORIES = (
		(KREATIKA,'Κρεατικά'),
		(TIRIA,'Τυριά'),
		(LAXANIKA,'Λαχανικα'),
		(DIAFORA,'Διάφορα')
	)
	title = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
	category = models.CharField(max_length=9,choices=MATERIAL_CHOICES,default=SALTY)
	mat_category = models.CharField(max_length=9,choices=MATERIAL_CATEGORIES,default=KREATIKA)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

class Crepe(models.Model):
	SALTY = 'Αλμυρές'
	SWEET = 'Γλυκές'
	MATERIAL_CHOICES = (
		(SALTY,'Αλμυρές'),
		(SWEET,'Γλυκές')
	)
	title = models.CharField(max_length=50)
	descritpion = models.TextField()
	price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
	category = models.CharField(max_length=9,choices=MATERIAL_CHOICES,default=SALTY)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title
