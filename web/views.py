from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CodigoForm
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
    return render(request, "panel_control.html", {"es_jefe_area": es_jefe_area})


@user_passes_test(es_jefe_area)
@login_required
def crear_mantenimiento(request):
    return render(request, "crear_mantenimiento.html")


@user_passes_test(es_jefe_area)
@login_required
def crear_maquina_1(request):
    return render(request, "crear_maquina_1.html")


@user_passes_test(es_jefe_area)
@login_required
def crear_maquina_2(request):
    return render(request, "crear_maquina_2.html")


@user_passes_test(es_jefe_area)
@login_required
def crear_tarea(request):
    return render(request, "crear_tarea.html")


@login_required
def ver_inventario(request):
    return render(request, "ver_inventario.html")


@login_required
def ver_mantenimiento(request):
    return render(request, "ver_mantenimiento.html")


@login_required
def ver_maquina_1(request):
    return render(request, "ver_maquina_1.html")


@login_required
def ver_maquina_2(request):
    return render(request, "ver_maquina_2.html")


@login_required
def ver_tarea(request):
    return render(request, "ver_tarea.html")
