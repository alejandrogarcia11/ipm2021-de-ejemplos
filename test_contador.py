#!/usr/bin/env python3


import sys
import textwrap
from collections import namedtuple

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

import e2e

"""Histories:

    GIVEN he lanzado la aplicación
    THEN veo el texto "Has pulsado 0 veces"

    GIVEN he lanzado la aplicación
    WHEN pulso el botón 'Contar'
    THEN veo el texto "Has pulsado 1 vez"

    GIVEN he lanzado la aplicación
    WHEN pulso el botón 'Contar' cuatro veces
    THEN veo el texto "Has pulsado 4 veces"
"""

# Funciones de ayuda

def show(text):
    print(textwrap.dedent(text))

def show_passed():
    print('\033[92m', "    Passed", '\033[0m')

def show_not_passed(e):
    print('\033[91m', "    Not passsed", '\033[0m')
    print(textwrap.indent(str(e), "    "))


# Contexto de las pruebas

Ctx = namedtuple("Ctx", "path process app")


# Implementación de los pasos

def given_he_lanzado_la_aplicacion(ctx):
    process, app = e2e.run(ctx.path)
    assert app is not None
    return Ctx(path= ctx.path, process= process, app= app)

def then_veo_el_texto_has_pulsado_0_veces(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'label' and node.get_text(0, -1).startswith("Has pulsado"))
    label = next(gen, None)
    assert label and label.get_text(0, -1) == "Has pulsado 0 veces", label.get_text(0, -1)
    return ctx

def when_pulso_el_boton_contar(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'push button' and node.get_name() == 'Contar')
    boton = next(gen, None)
    assert boton is not None
    e2e.do_action(boton, 'click')
    return ctx

def then_veo_el_texto_has_pulsado_1_vez(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'label' and node.get_text(0, -1).startswith("Has pulsado"))
    label = next(gen, None)
    assert label and label.get_text(0, -1) == "Has pulsado 1 vez", label.get_text(0, -1)
    return ctx

def when_pulso_el_boton_contar_cuatro_veces(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'push button' and node.get_name() == 'Contar')
    boton = next(gen, None)
    assert boton is not None
    e2e.do_action(boton, 'click')
    e2e.do_action(boton, 'click')
    e2e.do_action(boton, 'click')
    e2e.do_action(boton, 'click')
    return ctx

def then_veo_el_texto_has_pulsado_4_veces(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'label' and node.get_text(0, -1).startswith("Has pulsado"))
    label = next(gen, None)
    assert label and label.get_text(0, -1) == "Has pulsado 4 veces", label.get_text(0, -1)
    return ctx


if __name__ == '__main__':
    sut_path = sys.argv[1]
    initial_ctx = Ctx(path= sut_path, process= None, app= None)

    show("""
    GIVEN he lanzado la aplicación
    THEN veo el texto "Has pulsado 0 veces"
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = then_veo_el_texto_has_pulsado_0_veces(ctx)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)

    
    show("""
    GIVEN he lanzado la aplicación
    WHEN pulso el botón 'Contar'
    THEN veo el texto "Has pulsado 1 vez"
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_pulso_el_boton_contar(ctx)
        ctx = then_veo_el_texto_has_pulsado_1_vez(ctx)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)


    show("""
    GIVEN he lanzado la aplicación
    WHEN pulso el botón 'Contar' cuatro veces
    THEN veo el texto "Has pulsado 4 veces"
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_pulso_el_boton_contar_cuatro_veces(ctx)
        ctx = then_veo_el_texto_has_pulsado_4_veces(ctx)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)
