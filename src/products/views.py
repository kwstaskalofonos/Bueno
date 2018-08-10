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

def SaltyMaterial(request):
	materials = Material.objects.filter(category='Αλμυρές')
	#materials = Material.objects.all()
	context = {
		'materials':materials
	}
	return render(request,"materialList.html")

def SweetMaterial(request):
	materials = Material.objects.filter(category='Γλυκές')
	#materials = Material.objects.all()
	context = {
		'materials':materials
	}
	return render(request,"materialList.html")

def CrepeListView(request):
	#crepes = Crepe.objects.all()
	saltyCrepes = Crepe.objects.filter(category='Αλμυρές')
	sweetCrepes = Crepe.objects.filter(category='Γλυκές')
	context = {
		'saltyCrepes':saltyCrepes,
		'sweetCrepes':sweetCrepes
	}
	return render(request,"menu.html",context)
