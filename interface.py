from kivy.uix.screenmanager import Screen, ScreenManager
from helper import *
from kivy.lang import Builder
from kivymd.uix.snackbar import Snackbar
from easygui import fileopenbox
from cryptography.fernet import Fernet
from kivy.core.window import Window
from cheker import add_extension
from cheker import WatchDog
from kivymd.app import MDApp
from os import startfile
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

Window.size = (750, 550)

class Content(BoxLayout):
    def chkec(self):
        print(self.ids.key.text)
        if self.ids.key.text != "":
            with open("id.txt", "w") as file:
                file.write(self.ids.key.text)
            Snackbar(text="add id").open()


    def education(self):
        startfile("education.pdf")


class MenuScreen(Screen):
    pass


class ransomwareScreen(Screen):
    def run_WatchDog(self):
        print("WatchDog is run")
        ss = WatchDog("/")

    def education(self):
        pass

    def add_Safe_extension(self):
        try:
            extension = self.ids.extension.text
            with open("SafeExtension.txt", "r") as file:
                data_file = file.read()
            list_extension = data_file.split("\\")
            if extension != "TMP":
                if extension in list_extension:
                    pass
                else:
                    add_extension(extension , "SafeExtension.txt")
            print(extension)
            snak = Snackbar(text="Extension added successfully").open()
        except:
            snak = Snackbar(text="Failed to add extension").open()
    def add_Unsecured_extension(self):
        try:
            extension = self.ids.extension.text
            with open("UnsecuredExtension.txt", "r") as file:
                data_file = file.read()
            list_extension = data_file.split("\\")
            if extension != "TMP":
                if extension in list_extension:
                    pass
                else:
                    add_extension(extension , "UnsecuredExtension.txt")
            print(extension)
            snak = Snackbar(text="Extension added successfully").open()
        except:
            snak = Snackbar(text="Failed to add extension").open()


class keyScreen(Screen):

    def file_manager_decrypt_file(self):
        try:
            self.path_file = None
            self.path_file = fileopenbox()
            if self.path_file == None:
                self.path_file = "Press the icon to select the file: "
            else:
                print(self.path_file)
                self.ids.file_name_decrypt_file.text = self.path_file
                fileName = self.path_file.split("\\")
                self.path_name =fileName[-1:]
                print(self.path_name)
                self.path_file_end = ""
                number_of_items_in_fileName= len(fileName)
                for i in range(number_of_items_in_fileName - 1):
                    self.path_file_end = self.path_file_end + fileName[i]
                    self.path_file_end = self.path_file_end + "\\"

                print(self.path_file_end)
        except:
            snak = Snackbar(text="Something is wrong").open()

    def file_manager_Encrypt_file(self):
        try:
            self.path_file = None
            self.path_file = fileopenbox()
            if self.path_file == None:
                self.path_file = "Press the icon to select the file: "
            else:
                print(self.path_file)
                self.ids.file_name_Encrypt_file.text = self.path_file
                fileName = self.path_file.split("\\")
                self.path_name = fileName[-1:]
                print(self.path_name)
                self.path_file_end = ""
                number_of_items_in_fileName = len(fileName)
                for i in range(number_of_items_in_fileName - 1):
                    self.path_file_end = self.path_file_end + fileName[i]
                    self.path_file_end = self.path_file_end + "\\"

                print(self.path_file_end)


        except:
            snak = Snackbar(text="Something is wrong").open()


    def decrypt_file (self):
        try:
            if (self.path_file != "Press the icon to select the file: ") and (self.path_file != None):
                try:
                    path = self.path_file
                    file = open(path, "rb")
                    deta = file.read()
                    key = self.ids.key.text
                    print(key)
                    Encrypt = Fernet(key)
                    dnc_data = Encrypt.decrypt(deta)
                    new_file = open( self.path_file_end + self.path_name[0], "wb")
                    new_file.write(dnc_data)
                    file.close()
                    new_file.close()
                    snak = Snackbar (text = "The decryption was successful").open()

                except:
                    snak = Snackbar(text="Decryption was not successful").open()

        except:
            snak = Snackbar(text="Please select a file").open()

    def Encrypt_file(self):
        try:
            if (self.path_file != "Press the icon to select the file: ") and (self.path_file != None):
                try:
                    path = self.path_file
                    file = open(path, "rb")
                    deta = file.read()
                    key = Fernet.generate_key()
                    print(key)
                    Encrypt = Fernet(key)
                    enc_data = Encrypt.encrypt(deta)
                    new_file = open(self.path_file_end + "Encrypt" + self.path_name[0], "wb")
                    print("2")
                    key_file = open(self.path_file_end +"key.txt", "wb")
                    new_file.write(enc_data)
                    key_file.write(key)
                    file.close()
                    new_file.close()
                    key_file.close()
                    print("The encrypt was successful")
                    snak = Snackbar(text="The encrypt was successful").open()
                except:
                    snak = Snackbar(text="encrypt was not successful").open()

        except:
            snak = Snackbar(text="Please select a file").open()


class upload_file_Screen(Screen):

    def file_manager(self):

        self.path_file = None
        self.path_file = fileopenbox()



    def account_plus(self):
        self.dilog = MDDialog(
            title="Address:",
            type="custom",
            content_cls=Content(),
        )
        self.dilog.open()

    def refresh(self):
        self.data = ""
        with open("id.txt", "r") as file:
            self.data = file.read()

        if self.data != "0" and self.data != None:
            self.ids.id_name.text = f"id : {self.data}"
            self.id_number = self.data

    def upload_file(self):
        try:
            gauth = GoogleAuth()
            drive = GoogleDrive(gauth)
            upload_file = self.path_file
            gfile = drive.CreateFile({'parents': [{'id': self.id_number}]})
            gfile.SetContentFile(upload_file)
            gfile.Upload()
            snak = Snackbar(text="Upload was successful").open()
        except:
            snak = Snackbar(text="Something is wrong").open()
    def education(self):
        startfile("education.pdf")
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ransomwareScreen(name='ransomware'))
sm.add_widget(keyScreen(name='key_file'))
sm.add_widget(upload_file_Screen(name='upload_file'))

class caracalApp(MDApp):


    def build(self):
        self.theme_cls.theme_style = "Dark" # ['Light', 'Dark']
        self.theme_cls.primary_palette = 'LightBlue'
        self.theme_cls.primary_hue = "A700"

        screen = Builder.load_string(screen_helper)
        return screen
    def on_start(self):
        pass


caracalApp().run()
