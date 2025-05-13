from django.shortcuts import render, redirect
from ..forms import (
    MaquinaForm,
    TareaForm,
    MantenimientoForm,
    TipoMantenimientoForm,
    IntervaloForm,
    EncargadoForm,
    TipoMaquinaForm,
)
from ..services import MaquinasService, MantenimientoService, TareaService


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


def crear_intervalo(request):
    if request.method == "POST":
        form = IntervaloForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            # redirige a donde prefieras; aquí al panel
            return redirect("panel-control")
    else:
        form = IntervaloForm()
    return render(request, "crear_intervalo.html", {"form": form})


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


def crear_tipo_mantenimiento(request):
    if request.method == "POST":
        form = TipoMantenimientoForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            return redirect("panel-control")
    else:
        form = TipoMantenimientoForm()
    return render(request, "crear_tipo_mantenimiento.html", {"form": form})


def crear_encargado(request):
    if request.method == "POST":
        form = EncargadoForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            return redirect("panel-control")
    else:
        form = EncargadoForm()
    return render(request, "crear_encargado.html", {"form": form})


def crear_tipo_maquina(request):
    if request.method == "POST":
        form = TipoMaquinaForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            return redirect("panel-control")
    else:
        form = TipoMaquinaForm()
    return render(request, "crear_tipo_maquina.html", {"form": form})


def listar_maquinas(request):
    maquinas_service = MaquinasService()
    maquinas = maquinas_service.obtener_maquinas()
    return render(request, "ver_maquina_1.html", {"maquinas": maquinas})


def ver_mantenimiento(request):
    mantenimiento_service = MantenimientoService()
    mantenimientos = mantenimiento_service.obtener_mantenimientos()
    return render(request, "ver_mantenimiento.html", {"mantenimientos": mantenimientos})


def panel_control(request):
    return render(request, "panel_control.html")


def crear_maquina_1(request):
    return render(request, "crear_maquina_1.html")


def crear_maquina_2(request):
    return render(request, "crear_maquina_2.html")


def ver_inventario(request):
    return render(request, "ver_inventario.html")


def ver_maquina_1(request):
    return render(request, "ver_maquina_1.html")


def ver_maquina_2(request):
    return render(request, "ver_maquina_2.html")


def ver_tarea(request):
    tarea_service = TareaService()
    tareas = tarea_service.obtener_tareas()
    return render(request, "ver_tarea.html", {"tareas": tareas})


def admin_panel(request):
    return render(request, "admin_panel.html")
