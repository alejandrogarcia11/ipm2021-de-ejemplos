#!/usr/bin/env python3

import threading

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

w = Gtk.Window(title= "hitchhiker's guide to the galaxy")
w.connect('delete-event', Gtk.main_quit)

vbox = Gtk.VBox(spacing= 8, margin= 12)

label1 = Gtk.Label(label= "The Answer to The Ultimate Question of Life, the Universe, and Everything...",
                   justify= Gtk.Justification.FILL)
label1.set_line_wrap(True)
vbox.add(label1)

spinner = Gtk.Spinner()
vbox.pack_start(spinner, expand= False, fill= False, padding= 8)

hbox = Gtk.HBox(spacing= 8, halign= Gtk.Align.CENTER)
button1 = Gtk.Button(label= "Get ultimate answer")
hbox.pack_start(button1, expand= False, fill= False, padding= 8)
vbox.pack_start(hbox, expand= False, fill= False, padding= 8)

separator = Gtk.Separator(orientation= Gtk.Orientation.VERTICAL)
vbox.pack_start(separator, expand= False, fill= False, padding= 12)

label2 = Gtk.Label(label= "You've picked 0 towels")
vbox.add(label2)

hbox = Gtk.HBox(spacing= 8, halign= Gtk.Align.CENTER)
button2 = Gtk.Button(label= "Pick one towel")
hbox.pack_start(button2, expand= False, fill= False, padding= 8)
vbox.pack_start(hbox, expand= False, fill= False, padding= 8)

w.add(vbox)
w.show_all()

def update_answer(answer):
    spinner.stop()
    label1.set_label(f"The Answer to The Ultimate Question of Life, the Universe, and Everything is {answer}")
    
def get_ultimate_answer():
    # Code by Deep Thought
    #   The Answer to The Ultimate Question of Life, the Universe, and Everything...")
    #   ...are you F@#$&!G kidding me?
    import time
    years = 7_500_000 * 365 * 24 * 60 * 60
    #time.sleep(7_500_00)
    time.sleep(2)
    GLib.idle_add(update_answer, "42")

def on_get_ultimate_answer_clicked(widget):
    spinner.start()
    threading.Thread(target= get_ultimate_answer, daemon= True).start()

button1.connect('clicked', on_get_ultimate_answer_clicked)


n_towels = 0

def on_pick_towel_clicked(widget):
    global n_towels
    n_towels += 1
    towels = "1 towel" if n_towels == 1 else f"{n_towels} towels"
    label2.set_label(f"You've picked {towels}")

button2.connect('clicked', on_pick_towel_clicked)

Gtk.main()
