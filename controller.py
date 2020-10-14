import datetime

import model

class Controller:
    def set_model(self, model):
        self.model = model

    def set_view(self, view):
        self.view = view
        view.build_view(date_sample= datetime.datetime.today().isoformat())
        sdate = self.model.start_date
        rdate = self.model.return_date
        self._update_view(flight_type= 0 if self.model.one_way else 1,
                          start_date= "" if sdate is None else sdate.isoformat(),
                          return_date= "" if rdate is None else rdate.isoformat())
        view.connect_delete_event(self.view.main_quit)
        view.connect_flight_type_changed(self.on_flight_type_changed)
        view.connect_start_date_changed(self.on_start_date_changed)
        view.connect_return_date_changed(self.on_return_date_changed)
        view.connect_book_clicked(self.on_book_clicked)

    def main(self):
        self.view.show_all()
        self.view.main()

    def on_flight_type_changed(self, combobox):
        self.model.one_way = (combobox.get_active() == 0)
        self._update_view()
        
    def on_start_date_changed(self, entry):
        s = entry.get_text()
        date = self._parse_date(s)
        self.model.start_date = date
        self._update_view()
        
    def on_return_date_changed(self, entry):
        s = entry.get_text()
        date = self._parse_date(s)
        self.model.return_date = date
        self._update_view()

    def _update_view(self, **kwargs):
        self.view.update_view(**kwargs)
    
    def on_book_clicked(self, w):
        try:
            model.BookingClient().book(self.model)
            self.view.show_ok("Flight booked")
            self.model.reset()
            sdate = self.model.start_date
            rdate = self.model.return_date
            self._update_view(start_date= "" if sdate is None else sdate.isoformat(),
                              return_date= "" if rdate is None else rdate.isoformat())
        except Exception as e:
            self.view.show_error(str(e))
            
    def _parse_date(self, s):
        try:
            return datetime.datetime.fromisoformat(s)
        except ValueError:
            return None
