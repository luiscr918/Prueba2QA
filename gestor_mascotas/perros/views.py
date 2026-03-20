from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Raza

def lista_razas(request):
    todas_las_razas = Raza.objects.all()
    # Mostramos 5 razas por página (puedes cambiar este número)
    paginator = Paginator(todas_las_razas, 5) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'breeds/lista.html', {'page_obj': page_obj})

def detalle_raza(request, raza_id):
    raza = get_object_or_404(Raza, id=raza_id)
    return render(request, 'breeds/detalle.html', {'raza': raza})