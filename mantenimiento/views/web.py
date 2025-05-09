from django.shortcuts import render, redirect
from ..forms import MaquinaForm, TareaForm, MantenimientoForm
from ..services.maquinas_service import MaquinasService


def crear_maquina(request):
    if request.method == "POST":
        form = MaquinaForm(request.POST)
        if form.is_valid():
            nueva = form.save()
            # redirige a donde prefieras; aquí al panel
            return redirect("panel-control")
    else:
        form = MaquinaForm()
    return render(request, "crear_maquina.html", {"form": form})


def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            nueva = form.save()
            # redirige a donde prefieras; aquí al panel
            return redirect("panel-control")
    else:
        form = TareaForm()
    return render(request, "crear_tarea.html", {"form": form})


def crear_mantenimiento(request):
    if request.method == "POST":
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            # redirige a donde prefieras; aquí al panel
            return redirect("panel-control")
    else:
        form = MantenimientoForm()
    return render(request, "crear_mantenimiento.html", {"form": form})


def listar_maquinas(request):
    maquinas_service = MaquinasService()
    maquinas = maquinas_service.mostrar_maquinas()
    return render(request, "ver_maquina_1.html", {"maquinas": maquinas})


def panel_control(request):
    return render(request, "panel_control.html")


# def crear_mantenimiento(request):
#     return render(request, "crear_mantenimiento.html")


def crear_maquina_1(request):
    return render(request, "crear_maquina_1.html")


def crear_maquina_2(request):
    return render(request, "crear_maquina_2.html")


# def crear_tarea(request):
#     return render(request, "crear_tarea.html")


def ver_inventario(request):
    return render(request, "ver_inventario.html")


def ver_mantenimiento(request):
    return render(request, "ver_mantenimiento.html")


def ver_maquina_1(request):
    return render(request, "ver_maquina_1.html")


def ver_maquina_2(request):
    return render(request, "ver_maquina_2.html")


def ver_tarea(request):
    return render(request, "ver_tarea.html")
