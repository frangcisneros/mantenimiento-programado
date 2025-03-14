# Generated by Django 5.1.7 on 2025-03-10 23:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TareaMantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_programada', models.DateField()),
                ('descripcion', models.TextField()),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.maquina')),
            ],
        ),
    ]
