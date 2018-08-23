from django.views.generic import ListView
from django.shortcuts import render
from .models import Material, Crepe

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
	saltmaterials = Material.objects.filter(category='Αλμυρές')
	sweetmaterials = Material.objects.filter(category='Γλυκές')
	context = {
		'saltyCrepes':saltycrepes[:round(len(saltycrepes)/2)],
		'saltyCrepe2s':saltycrepes[round(len(saltycrepes)/2):],
		'sweetCrepes':sweetcrepes[:round(len(sweetcrepes)/2)],
		'sweetCrepe2s':sweetcrepes[round(len(sweetcrepes)/2):],
		'saltmaterials':saltmaterials,
		'sweetmaterials':sweetmaterials
	}
	return render(request,"menu.html",context)

