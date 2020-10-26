from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.event import EventDispatcher
from kivy.uix.screenmanager import Screen


from kivy.network.urlrequest import UrlRequest
from kivy.factory import Factory
# Python imports
import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from json import dumps
import os.path



# Load the kv files
folder = os.path.dirname(os.path.realpath(__file__))




KV = """

<SignUpScreen>:
Screen:
    NavigationLayout:

        ScreenManager:
           
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    

                    MDToolbar:
                        md_bg_color: app.theme_cls.primary_color
                        title: "Sign Up"
                        elevation: 10
                        left_action_items: [["arrow-left", lambda x: x]]

                    MDTabs:
                        id: android_tabs
                        
                                    

                                    

                        Tab:
                            text: "Patient"

                            ScrollView:

                                BoxLayout:
                                    orientation: 'vertical'
                                    height: self.minimum_height
                                    padding: dp(48)
                                    spacing: "10dp"
                                    size_hint_x: .75
                                    size_hint_max_x: dp(400)
                                    size_hint_min_x: min(dp(400), root.width)
                                    pos_hint: {'center_x': .5}
                                    
                                
                                    FloatLayout:
                                    

                                        MDTextFieldRound:
                                            icon_left: 'email'
                                            hint_text: 'Email'
                                            pos_hint: {"center_x": 1.15, "center_y": .6}
                                            normal_color: 0, 0, 0, 0
                                            color_active: 1, 1, 1, 1
                                            
                                            

                                        MDTextFieldRound:
                                            icon_left: 'lock'
                                            icon_right: 'eye-off'
                                            hint_text: 'Password'
                                            pos_hint: {"center_x": 1.15, "center_y": .5}
                                            normal_color: 0, 0, 0, 0
                                            color_active: 1, 1, 1, .5
                                            
                                        MDFillRoundFlatIconButton:
                                            text: "Continue"
                                            icon: "cursor-pointer"
                                            pos_hint: {"center_x": 1.15, "center_y": .3} 
                                            size_hint_x: .9
                                        
                                        MDRoundFlatIconButton:
                                            icon: "facebook"
                                            width: dp(280)
                                            pos_hint: {"center_x": 1.15, "center_y": .2} 
                                            size_hint_x: .9

                                            MDLabel:
                                                text: "Sign Up with Facebook"
                                                halign: 'center'
                                                theme_text_color: "Custom"
                                                text_color: 0, 0, 1, .5
                                                font_size: "12sp"
                                                width: dp(250)

                                        MDRoundFlatIconButton:
                                            icon: "google-plus"
                                            width: dp(280)
                                            pos_hint: {"center_x": 1.15, "center_y": .1} 
                                            size_hint_x: .9

                                            MDLabel:
                                                text: "Sign Up with Gmail"
                                                halign: 'center'
                                                theme_text_color: "Custom"
                                                text_color: 0, 0, 1, .5
                                                font_size: "12sp"
                                                width: dp(250)

                                        MDTextButton:
                                            text: "Already have an account?"
                                            font_size: "9sp"
                                            pos_hint: {"center_x": 1.15, "center_y": .03} 
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 1, .5
                                            on_press: 


                        Tab:
                            text: "Doctor"      

                            ScrollView:

                                BoxLayout:
                                    orientation: 'vertical'
                                    height: self.minimum_height
                                    padding: dp(48)
                                    spacing: "10dp"
                                    size_hint_x: .75
                                    size_hint_max_x: dp(400)
                                    size_hint_min_x: min(dp(400), root.width)
                                    pos_hint: {'center_x': .5}
                                    
                                
                                    FloatLayout:
                                    

                                        MDTextFieldRound:
                                            icon_left: 'email'
                                            hint_text: 'Email'
                                            pos_hint: {"center_x": 1.15, "center_y": .6}
                                            normal_color: 0, 0, 0, 0
                                            color_active: 1, 1, 1, 1
                                            
                                            

                                        MDTextFieldRound:
                                            icon_left: 'lock'
                                            icon_right: 'eye-off'
                                            hint_text: 'Password'
                                            pos_hint: {"center_x": 1.15, "center_y": .5}
                                            normal_color: 0, 0, 0, 0
                                            color_active: 1, 1, 1, .5
                                            
                                        MDFillRoundFlatIconButton:
                                            text: "Continue"
                                            icon: "cursor-pointer"
                                            pos_hint: {"center_x": 1.15, "center_y": .3} 
                                            size_hint_x: .9
                                        
                                        MDRoundFlatIconButton:
                                            icon: "facebook"
                                            width: dp(280)
                                            pos_hint: {"center_x": 1.15, "center_y": .2} 
                                            size_hint_x: .9

                                            MDLabel:
                                                text: "Sign Up with Facebook"
                                                halign: 'center'
                                                theme_text_color: "Custom"
                                                text_color: 0, 0, 1, .5
                                                font_size: "12sp"
                                                width: dp(250)

                                        MDRoundFlatIconButton:
                                            icon: "google-plus"
                                            width: dp(280)
                                            pos_hint: {"center_x": 1.15, "center_y": .1} 
                                            size_hint_x: .9

                                            MDLabel:
                                                text: "Sign Up with Gmail"
                                                halign: 'center'
                                                theme_text_color: "Custom"
                                                text_color: 0, 0, 1, .5
                                                font_size: "12sp"
                                                width: dp(250)

                                        MDTextButton:
                                            text: "Already have an account?"
                                            font_size: "9sp"
                                            pos_hint: {"center_x": 1.15, "center_y": .03} 
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 1, .5
                                            on_press:        
                
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'


        


    


"""

    
class Tab(FloatLayout, MDTabsBase):
    pass 

class SignUp(MDApp):
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_string(KV)
    
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
    
        instance_tab.ids.label.text = tab_text



SignUp().run()
