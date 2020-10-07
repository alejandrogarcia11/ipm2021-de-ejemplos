#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

w = Gtk.Window(title= "¡Hola contador!")
w.connect('delete-event', Gtk.main_quit)

vbox = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)

label1 = Gtk.Label(label= "Has pulsado")
label1.show()
vbox.pack_start(label1, expand= True, fill= True, padding= 8)

label2 = Gtk.Label(label= "8")
label2.show()
vbox.pack_start(label2, expand= True, fill= True, padding= 8)

button = Gtk.Button(label= "Contar")
button.show()
vbox.pack_start(button, expand= False, fill= False, padding= 8)

w.add(vbox)
w.show_all()

Gtk.main()
