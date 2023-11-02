#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.clock import Clock
# from kivy.graphics.texture import Texture
# import cv2
from plyer import filechooser
import plyer
import shutil
# from android.permissions import request_permission, check_permission, Permission
# from jnius import autoclass
import os
from kivy import platform
import shutil


if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.CAMERA,
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE
    ])



class Classifier(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        # self.capture = cv2.VideoCapture(0)
        # Clock.schedule_interval(self.load_video, 1.0 / 30.0)
        self.camera = self.ids["0"]
        self.image = self.ids["4"]
        self.result_label = self.ids["6"]

    # def load_video(self, *args):
    #     ret, frame = self.capture.read()
    #     self.image_frame = frame
    #     buffer = cv2.flip(frame, 0).tostring()
    #     texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
    #     texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
    #     self.screen.texture = texture
    #
    def take_picture(self, *args):
        image_name = "screenshot.png"
        # self.camera.export_to_png(image_name)
        # dest_path = os.path.join(plyer.storagepath.get_home_dir(), "DCIM", "Camera", image_name)
        # dest_path = "../screenshot.png"
        # self.result_label.text = dest_path

        try:
            self.camera.texture.save(os.path.join("/sdcard/DCIM/Camera", image_name))
            self.image.source = os.path.join("/sdcard/DCIM/Camera", image_name)
            self.result_label.text = "Success"
        except Exception as e:
            self.result_label.text = str(e)

        # shutil.copy(image_name, dest_path)

    def attach_image(self, *args):
        self.result_label.text = "Wow"
        filechooser.open_file(on_selection=self.selected)
        # self.image.source = selection[0]
        # path = filechooser.open_file(path=".")[0]
        # self.result_label.text = type(path)

        # try:
        #     self.image.source = path
        #     print("YES")
        #
        # except Exception as e:
        #     print("NO")

    def selected(self, selection):
        self.result_label.text = selection[0]
        shutil.copy(selection[0], "/sdcard/DCIM/Camera/asdsad.png")
        self.image.source = "/sdcard/DCIM/Camera/asdsad.png"

Builder.load_file("layout.kv")
sm = ScreenManager()
sm.add_widget(Classifier(name='mushroom_classifier'))


class StartApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    StartApp().run()





