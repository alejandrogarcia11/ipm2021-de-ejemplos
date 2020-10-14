#!/usr/bin/env python3

from controller import Controller
from model import BookingData
from view import View

if __name__ == '__main__':

    controller = Controller()
    controller.set_model(BookingData())
    controller.set_view(View())
    controller.main()

