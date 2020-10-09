import model
import view

class Controller:
    def __init__(self, model):
        self.model = model
        self.view = view.View(self.model.count)
        self.view.connect_contar_clicked(self.on_contar_clicked)
        self.model.add_observer(self)

        
    def on_contar_clicked(self, widget):
        self.model.count_up()

        
    def update(self):
        self.view.update_count(self.model.count)




def view_start():
    view.start()
