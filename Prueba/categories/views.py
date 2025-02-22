from django.shortcuts import render, redirect, get_object_or_404
from .models import Tours, Activities

# Vista para mostrar Tours y Actividades
def categories_view(request):
    tours = Tours.objects.prefetch_related('activities').all()
    return render(request, "categories/categories.html", {"tours": tours})

# CRUD para Tours
def create_tour(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        ubicacion = request.POST.get("ubicacion")
        Tours.objects.create(nombre=nombre, descripcion=descripcion, precio=precio, ubicacion=ubicacion)
        return redirect('categories')

def edit_tour(request, tour_id):
    tour = get_object_or_404(Tours, id=tour_id)
    if request.method == "POST":
        tour.nombre = request.POST.get("nombre")
        tour.descripcion = request.POST.get("descripcion")
        tour.precio = request.POST.get("precio")
        tour.ubicacion = request.POST.get("ubicacion")
        tour.save()
        return redirect('categories')
    return render(request, "categories/edit_tour.html", {"tour": tour})

def delete_tour(request, tour_id):
    tour = get_object_or_404(Tours, id=tour_id)
    tour.delete()
    return redirect('categories')

# CRUD para Activities
def create_activity(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        detalle = request.POST.get("detalle")
        precio = request.POST.get("precio")
        horario = request.POST.get("horario")
        tour_id = request.POST.get("tour_id")
        tour = get_object_or_404(Tours, id=tour_id)
        Activities.objects.create(nombre=nombre, detalle=detalle, precio=precio, horario=horario, tour=tour)
        return redirect('categories')

def edit_activity(request, activity_id):
    activity = get_object_or_404(Activities, id=activity_id)
    if request.method == "POST":
        activity.nombre = request.POST.get("nombre")
        activity.detalle = request.POST.get("detalle")
        activity.precio = request.POST.get("precio")
        activity.horario = request.POST.get("horario")
        activity.save()
        return redirect('categories')
    return render(request, "categories/edit_activity.html", {"activity": activity})

def delete_activity(request, activity_id):
    activity = get_object_or_404(Activities, id=activity_id)
    activity.delete()
    return redirect('categories')
