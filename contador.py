#!/usr/bin/env python3


import controller
from model import Model
import view

if __name__ == '__main__':
    model = Model()
    controller.Controller(model)
    controller.Controller(model)
    controller.view_start()
