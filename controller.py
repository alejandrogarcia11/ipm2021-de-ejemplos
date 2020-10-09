import model
import view

class Controller:
    def __init__(self):
        self.model = model.Model()
        self.view = view.View(self.model.count)
        self.view.connect_contar_clicked(self.on_contar_clicked)

        
    def on_contar_clicked(self, widget):
        self.model.count_up()
        self.view.update_count(self.model.count)

    def start(self):
        view.start()
