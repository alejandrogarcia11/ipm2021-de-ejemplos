#!/usr/bin/env python3

from controller import Controller
from model import Model

if __name__ == '__main__':
    model = Model()
    controler = Controller(model)
    controler.start()
