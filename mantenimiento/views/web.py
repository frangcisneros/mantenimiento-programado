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
from ..models import Mantenimiento, Maquina, Tarea, Encargado, OpcionesMantenimiento, OpcionesIntervalo
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt




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

@login_required
def admin_planes_mantenimiento(request):
    objetos = Mantenimiento.objects.all()
    seleccionado = None
    id_sel = request.GET.get('id')
    if id_sel:
        seleccionado = Mantenimiento.objects.filter(id_mantenimiento=id_sel).first()
    return render(request, "admin_planes_mantenimiento.html", {
        "objetos": objetos,
        "seleccionado": seleccionado,
    })

@login_required
def admin_maquinas(request):
    objetos = Maquina.objects.all()
    seleccionado = None
    id_sel = request.GET.get('id')
    if id_sel:
        seleccionado = Maquina.objects.filter(id_maquina=id_sel).first()
    return render(request, "admin_maquinas.html", {
        "objetos": objetos,
        "seleccionado": seleccionado,
    })

@login_required
def admin_mantenimientos(request):
    objetos = Tarea.objects.all()
    seleccionado = None
    id_sel = request.GET.get('id')
    if id_sel:
        seleccionado = Tarea.objects.filter(id_tarea=id_sel).first()
    return render(request, "admin_mantenimientos.html", {
        "objetos": objetos,
        "seleccionado": seleccionado,
    })

@login_required
def admin_personal(request):
    objetos = Encargado.objects.all()
    seleccionado = None
    id_sel = request.GET.get('id')
    if id_sel:
        seleccionado = Encargado.objects.filter(id_encargado=id_sel).first()
    return render(request, "admin_personal.html", {
        "objetos": objetos,
        "seleccionado": seleccionado,
    })

@user_passes_test(es_jefe_area)
@login_required
def crear_maquina(request, id_maquina=None):
    if id_maquina:
        maquina = Maquina.objects.get(id_maquina=id_maquina)
    else:
        maquina = None

    if request.method == "POST":
        form = MaquinaForm(request.POST, instance=maquina)
        if form.is_valid():
            form.save()
            return redirect("admin-maquinas")
    else:
        form = MaquinaForm(instance=maquina)
    return render(request, "crear_maquina.html", {"form": form, "maquina": maquina})

@login_required
def eliminar_maquina(request, id_maquina):
    maquina = Maquina.objects.get(id_maquina=id_maquina)
    if request.method == "POST":
        maquina.delete()
        return redirect("admin-maquinas")
    return render(request, "eliminar_maquina.html", {"maquina": maquina})

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
    maquinas = Maquina.objects.all()
    maquina_id = request.GET.get('id')
    maquina_seleccionada = None
    operario = None
    plan_mantenimiento = None
    from typing import Optional
    tareas: dict[str, Optional[Tarea]] = {'anterior': None, 'actual': None, 'proxima': None}

    if maquina_id:
        try:
            maquina_seleccionada = Maquina.objects.get(id_maquina=maquina_id)
            operario = maquina_seleccionada.operario

            # Plan de mantenimiento (puedes ajustar la lógica según tu modelo)
            plan_mantenimiento = Mantenimiento.objects.filter(
                tarea__id_maquina=maquina_seleccionada
            ).order_by('-id_mantenimiento').first()

            # Tareas relevantes
            tareas_qs = Tarea.objects.filter(id_maquina=maquina_seleccionada).order_by('fecha_inicio')
            ahora = timezone.now()
            tareas['anterior'] = tareas_qs.filter(fecha_inicio__lt=ahora).last()
            tareas['actual'] = tareas_qs.filter(fecha_inicio__lte=ahora, fecha_fin__gte=ahora).first()
            tareas['proxima'] = tareas_qs.filter(fecha_inicio__gt=ahora).first()

        except Maquina.DoesNotExist:
            maquina_seleccionada = None

    return render(request, "ver_maquina_1.html", {
        "maquinas": maquinas,
        "maquina_seleccionada": maquina_seleccionada,
        "operario": operario,
        "plan_mantenimiento": plan_mantenimiento,
        "tareas": tareas,
    })


@login_required
def ver_maquina_2(request):
    return render(request, "ver_maquina_2.html")


@login_required
def ver_tarea(request):
    tarea_service = TareaService()
    tareas = tarea_service.obtener_tareas()
    return render(request, "ver_tarea.html", {"tareas": tareas})

@login_required
def eliminar_encargado(request, id_encargado):
    encargado = Encargado.objects.get(id_encargado=id_encargado)
    if request.method == "POST":
        encargado.delete()
        return redirect("admin-personal")
    return render(request, "confirmar_eliminar_encargado.html", {"encargado": encargado})

@login_required
def editar_encargado(request, id_encargado):
    encargado = Encargado.objects.get(id_encargado=id_encargado)
    if request.method == "POST":
        form = EncargadoForm(request.POST, instance=encargado)
        if form.is_valid():
            form.save()
            return redirect("admin-personal")
    else:
        form = EncargadoForm(instance=encargado)
    return render(request, "editar_encargado.html", {"form": form, "encargado": encargado})

@login_required
def ver_tarea_detalle(request, id_tarea):
    tarea_service = TareaService()
    mantenimiento_service = MantenimientoService()
    encargado_service = EncargadoService()
    maquina_service = MaquinasService()
    tarea = tarea_service.obtener_tarea_por_id(id_tarea)
    if tarea is None or tarea.id_mantenimiento is None or tarea.id_encargado is None or tarea.id_maquina is None:
        return render(request, "404.html", status=404)
    mantenimiento = mantenimiento_service.obtener_mantenimiento_por_id(tarea.id_mantenimiento.id_mantenimiento)
    encargado = encargado_service.obtener_encargado_por_id(tarea.id_encargado.id_encargado)
    maquina = maquina_service.obtener_maquina_por_id(tarea.id_maquina.id_maquina)
    return render(request, "ver_tarea_detalle.html", {"tarea": tarea, "mantenimiento": mantenimiento, "encargado": encargado, "maquina": maquina})


@login_required
def admin_panel(request):
    return render(request, "admin_panel.html")
