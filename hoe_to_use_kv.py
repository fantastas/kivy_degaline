
# code how to use .kv file in kivy
 
# import kivy module
import kivy
import requests
import json
import re
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ObjectProperty

Builder.load_file('kvfile.kv')

class MyLayout(Widget):


    def circle(self):
        response_API = requests.get('https://www.circlek.lt/privatiems/degalu-kainos')
		# print(response_API.status_code)
        data = response_API.text

        kaina = re.findall(r"[-+]?\d*\.\d+", data)
        circle_95_miles = kaina[2]

        kainos_kitos = re.findall(r"[-+]?\d*\,\d+", data)
        circle_95_miles_plus = kainos_kitos[0]
        circle_98_miles_plus = kainos_kitos[1]
        circle_d_miles = kainos_kitos[2]
        circle_d_miles_plus = kainos_kitos[3]
        circle_dz = kainos_kitos[4]
        circle_lng = kainos_kitos[5]
        message = '95 Miles = ' + circle_95_miles + '\n' + '95 Miles Plus = ' + circle_95_miles_plus
        self.ids.lbl.text = message
        print(circle_95_miles,circle_95_miles_plus,circle_98_miles_plus,circle_d_miles, circle_d_miles_plus, circle_dz, circle_lng)



 

class kvfileApp(App):
    def build(self):
        return MyLayout()




if __name__ == '__main__': 
    kv = kvfileApp()
    kv.run()