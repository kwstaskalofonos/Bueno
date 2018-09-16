from django.views.generic import ListView
from django.shortcuts import render
from .models import Material, Crepe
from django.http import HttpResponse

#class MaterialListView(ListView):
	#materials = Material.objects.get(category='Αλμυρές')
	#queryset = Material.objects.all()
	#template_name = "materialList.html"

	#def get_context_data(self, *args, **kwargs):
	#	context = super(MaterialListView, self).get_context_data(*args, **kwargs)
	#	print(context)
	#	return context

def CrepeListView(request):
	#crepes = Crepe.objects.all()
	saltycrepes = Crepe.objects.filter(category='Αλμυρές')
	sweetcrepes = Crepe.objects.filter(category='Γλυκές')
	meats = Material.objects.filter(mat_category='Κρεατικά')
	cheeses = Material.objects.filter(mat_category='Τυριά')
	groceries = Material.objects.filter(mat_category='Λαχανικα')
	difrs = Material.objects.filter(mat_category='Διάφορα')
	context = {
		'saltyCrepes':saltycrepes[:round(len(saltycrepes)/2)],
		'saltyCrepe2s':saltycrepes[round(len(saltycrepes)/2):],
		'sweetCrepes':sweetcrepes[:round(len(sweetcrepes)/2)],
		'sweetCrepe2s':sweetcrepes[round(len(sweetcrepes)/2):],
		'meats':meats,
		'cheeses':cheeses,
		'groceries':groceries,
		'difrs':difrs
	}
	return render(request,"menu.html",context)

def AjaxCall(request):
	print(request.META.get('HTTP_X_REQUESTED_WITH'))
	if request.is_ajax():
		print('Ajax call')
	else:
		print('No Ajax')
	return HttpResponse('')


