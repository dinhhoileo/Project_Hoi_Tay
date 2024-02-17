import pandas as pd
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
# Basicly infortion user

class User:
    def __init__(self, user_name, password):
        self.__user_name = user_name  # private
        self.__password = password  # private

    def get_user_name(self):
        return self.__user_name

    def get_password(self):
        return self.__password

    def set_user_name(self, new_user_name):
        self.__user_name = new_user_name

    def set_passwork(self, new_password):
        self.__password = new_password
