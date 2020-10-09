import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class View:
    def __init__(self, count):
        w = Gtk.Window(title= "Contador")
        w.connect('delete-event', Gtk.main_quit)

        vbox = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)

        label1 = Gtk.Label()
        label1.show()
        vbox.pack_start(label1, expand= True, fill= True, padding= 8)

        button = Gtk.Button(label= "Contar")
        button.show()
        vbox.pack_start(button, expand= False, fill= False, padding= 8)

        w.add(vbox)
        w.show_all()

        self.button = button
        self.count_label = label1
        self.update_count(count)

        
    def connect_contar_clicked(self, handler):
        self.button.connect('clicked', handler)


    def update_count(self, count):
        veces = "1 vez" if count == 1 else f"{count} veces"
        self.count_label.set_label(f"Has pulsado {veces}")


def start():
    Gtk.main()
