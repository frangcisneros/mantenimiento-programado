from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


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
    return render(request, "panel_control.html")


@login_required
def crear_mantenimiento(request):
    return render(request, "crear_mantenimiento.html")


@login_required
def crear_maquina_1(request):
    return render(request, "crear_maquina_1.html")


@login_required
def crear_maquina_2(request):
    return render(request, "crear_maquina_2.html")


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
