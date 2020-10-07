#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

w = Gtk.Window(title= "¡Hola mundo!")
w.connect('delete-event', Gtk.main_quit)
w.show()

Gtk.main()
