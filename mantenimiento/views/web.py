from django.shortcuts import render


def panel_control(request):
    return render(request, "panel_control.html")


def crear_mantenimiento(request):
    return render(request, "crear_mantenimiento.html")


def crear_maquina_1(request):
    return render(request, "crear_maquina_1.html")


def crear_maquina_2(request):
    return render(request, "crear_maquina_2.html")


def crear_tarea(request):
    return render(request, "crear_tarea.html")


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
