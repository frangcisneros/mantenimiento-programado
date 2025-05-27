from django.shortcuts import render, redirect
from ..forms import (
    MaquinaForm,
    TareaForm,
    MantenimientoForm,
    TipoMantenimientoForm,
    IntervaloForm,
    EncargadoForm,
    TipoMaquinaForm,
    CodigoForm,
)
from datetime import date
from ..services import MaquinasService, MantenimientoService, TareaService, EncargadoService
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import Group


def es_jefe_area(user):
    return user.groups.filter(name="Jefes de Área").exists()


@login_required
def verificar_codigo(request):
    if request.method == "POST":
        form = CodigoForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data["codigo"]

            # Verifica el código especial
            if codigo == "123":  # TODO! Cambia esto por na verif real
                grupo, creado = Group.objects.get_or_create(name="Jefes de Área")
                request.user.groups.add(grupo)  # Asigna al usuario al grupo
                return redirect("panel-control")  # Redirige al panel de control
            else:
                form.add_error("codigo", "Código incorrecto")
    else:
        form = CodigoForm()
    return render(request, "registration/verif_codigo.html", {"form": form})


def registrar_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect("panel-control")  # Redirige al panel de control
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def panel_control(request):
    es_jefe_area = request.user.groups.filter(name="Jefes de Área").exists()
    tareas_hoy = TareaService().obtener_tareas().filter(fecha_inicio__date=date.today()).order_by("fecha_inicio")
    return render(request, "panel_control.html", {"es_jefe_area": es_jefe_area, "tareas_hoy": tareas_hoy})

@user_passes_test(es_jefe_area)
@login_required
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


@user_passes_test(es_jefe_area)
@login_required
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


@login_required
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


@user_passes_test(es_jefe_area)
@login_required
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


@login_required
def crear_tipo_mantenimiento(request):
    if request.method == "POST":
        form = TipoMantenimientoForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            return redirect("panel-control")
    else:
        form = TipoMantenimientoForm()
    return render(request, "crear_tipo_mantenimiento.html", {"form": form})


@login_required
def crear_encargado(request):
    if request.method == "POST":
        form = EncargadoForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            return redirect("panel-control")
    else:
        form = EncargadoForm()
    return render(request, "crear_encargado.html", {"form": form})


@login_required
def crear_tipo_maquina(request):
    if request.method == "POST":
        form = TipoMaquinaForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            return redirect("panel-control")
    else:
        form = TipoMaquinaForm()
    return render(request, "crear_tipo_maquina.html", {"form": form})


@login_required
def listar_maquinas(request):
    maquinas_service = MaquinasService()
    tareas_service = TareaService()
    tareas = tareas_service.obtener_tareas()
    maquinas = maquinas_service.obtener_maquinas()
    return render(
        request, "ver_maquina_1.html", {"maquinas": maquinas, "tareas": tareas}
    )


@login_required
def ver_mantenimiento(request):
    mantenimiento_service = MantenimientoService()
    mantenimientos = mantenimiento_service.obtener_mantenimientos()
    return render(request, "ver_mantenimiento.html", {"mantenimientos": mantenimientos})





@user_passes_test(es_jefe_area)
@login_required
def crear_maquina_1(request):
    return render(request, "crear_maquina_1.html")


@user_passes_test(es_jefe_area)
@login_required
def crear_maquina_2(request):
    return render(request, "crear_maquina_2.html")


@login_required
def ver_inventario(request):
    return render(request, "ver_inventario.html")


@login_required
def ver_maquina_1(request):
    return render(request, "ver_maquina_1.html")


@login_required
def ver_maquina_2(request):
    return render(request, "ver_maquina_2.html")


@login_required
def ver_tarea(request):
    tarea_service = TareaService()
    tareas = tarea_service.obtener_tareas()
    return render(request, "ver_tarea.html", {"tareas": tareas})


@login_required
def ver_tarea_detalle(request, id_tarea):
    tarea_service = TareaService()
    mantenimiento_service = MantenimientoService()
    encargado_service = EncargadoService()
    maquina_service = MaquinasService()
    tarea = tarea_service.obtener_tarea_por_id(id_tarea)
    mantenimiento = mantenimiento_service.obtener_mantenimiento_por_id(tarea.id_mantenimiento.id_mantenimiento)
    encargado = encargado_service.obtener_encargado_por_id(tarea.id_encargado.id_encargado)
    maquina = maquina_service.obtener_maquina_por_id(tarea.id_maquina.id_maquina)
    if tarea is None:
        return render(request, "404.html", status=404)
    return render(request, "ver_tarea_detalle.html", {"tarea": tarea, "mantenimiento": mantenimiento, "encargado": encargado, "maquina": maquina})


@login_required
def admin_panel(request):
    return render(request, "admin_panel.html")
