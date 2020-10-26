from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.image import Image 
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.event import EventDispatcher
import json
import requests
from firebase import Firebase

from kivy.factory import Factory
import os.path
from kivy.network.urlrequest import UrlRequest
import certifi
from json import dumps
from kivymd.uix.dialog import MDDialog
from kivymd.uix.spinner import MDSpinner



# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<SignUpScreen>:

    NavigationLayout:

        ScreenManager:
           
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    

                    MDToolbar:
                        md_bg_color: app.theme_cls.primary_color
                        title: "Sign Up"
                        elevation: 10
                        left_action_items: [["arrow-left", lambda x: root.callback()]]

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
                                        pos_hint: {'center_x': 1.45}
    
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
                                            password: True
                                            pos_hint: {"center_x": 1.15, "center_y": .5}
                                            normal_color: 0, 0, 0, 0
                                            color_active: 1, 1, 1, .5
                                            
                                        MDFillRoundFlatIconButton:
                                            text: "Continue"
                                            icon: "cursor-pointer"
                                            pos_hint: {"center_x": 1.15, "center_y": .3} 
                                            size_hint_x: .9
                                            on_release:
                                                
                                    
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
                                            on_press: root.callback2()


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
                                        pos_hint: {'center_x': 1.45}

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
                                            password: True
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
                                            on_press: root.callback2()   
                
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'


<LoginScreen>:
    web_api_key: "AIzaSyDfIu0zKYNLkQqovFdkQDcRj095w4IBR6w"
    debug: True 
    on_login_success:
        app.user_localId = self.localId
        app.user_idToken = self.idToken

    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"

        ScrollView:

            BoxLayout:
                orientation: 'vertical'
                height: self.minimum_height
                padding: dp(48)
                spacing: dp(15)
                size_hint_x: .75
                size_hint_max_x: dp(400)
                size_hint_min_x: min(dp(400), root.width)
                pos_hint: {'center_x': .5}
                 
               
                FloatLayout:
                    pos_hint: {'center_x': 1.45}
                 

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
                        password: True
                        pos_hint: {"center_x": 1.15, "center_y": .5}
                        normal_color: 0, 0, 0, 0
                        color_active: 1, 1, 1, .5
                        
                    MDFillRoundFlatIconButton:
                        text: "Continue"
                        icon: "cursor-pointer"
                        pos_hint: {"center_x": 1.15, "center_y": .3} 
                        size_hint_x: .9
                        on_release: 
                           
                       
                    
                    
                    MDRoundFlatIconButton:
                        icon: "facebook"
                        width: dp(280)
                        pos_hint: {"center_x": 1.15, "center_y": .2} 
                        size_hint_x: .9

                        MDLabel:
                            text: "Login with Facebook"
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
                            text: "Login with Gmail"
                            halign: 'center'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 1, .5
                            font_size: "12sp"
                            width: dp(250)

                    MDTextButton:
                        text: "Don't have an account?"
                        font_size: "9sp"
                        pos_hint: {"center_x": 1.15, "center_y": .03} 
                        theme_text_color: "Custom"
                        text_color: 0, 0, 1, .5
                        on_release: root.callback1()


                        
    FloatLayout:
            
                    
        Image:
            id: avatar
            size_hint: None, None
            size: "66dp", "66dp"
            source: "data/logo/kivy-icon-256.png"
            height: avatar.height
            pos_hint: {"center_x": .5, "center_y": .8}

        
    
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'


        MDToolbar:
            md_bg_color: app.theme_cls.primary_color
            title: "Log In"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: root.callback()]]


<LoadingScreen>:
    BoxLayout:
        Image:
            source: 'MyCare.png'
            size_hint: 0.5, 0.5
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    
    FloatLayout:

        MDFillRoundFlatIconButton:
            text: "Continue"
            icon: "cursor-pointer"
            pos_hint: {"center_x": .5, "center_y": .2} 
            size_hint_x: .4
            on_press: root.manager.current = 'login'

    
        

""")
   
class LoadingPopup(Screen):
    pass

class Tab(FloatLayout, MDTabsBase):
    pass 

# Declare both screens
class SignUpScreen(Screen, MDApp, EventDispatcher):
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def callback1(self):
        self.manager.current = 'signup'

    def callback(self):
        self.manager.current = 'loading'

    def callback2(self):
        self.manager.current = 'login'
    
    
   
    
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
    
        instance_tab.ids.label.text = tab_text


 
    
    



class LogInScreen(Screen, MDApp, EventDispatcher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def callback(self):
        self.manager.current = 'loading'

    def callback1(self):
        self.manager.current = 'signup'

    account_id = 1 
    def on_start(self):
        result = requests.get("https://mycare-134d0.firebaseio.com/" + str(self.account_id) + "1.json")
        print("Welcome", result.ok)

    url = 'https://mycare-134d0.firebaseio.com/.json'

    web_api_key = StringProperty()  # From Settings tab in Firebase project

    # Firebase Authentication Credentials - what developers want to retrieve
    refresh_token = ""
    localId = ""
    idToken = ""

    # Properties used to send events to update some parts of the UI
    login_success = BooleanProperty(False)  # Called upon successful sign in
    sign_up_msg = StringProperty()
    sign_in_msg = StringProperty()
    email_exists = BooleanProperty(False)
    email_not_found = BooleanProperty(False)

    debug = False
    

    def patch(self, JSON):
        to_database = json.loads(JSON)
        requests.patch(url = self.url, json = to_database)
    
    def on_web_api_key(self, *args):
        """When the web api key is set, look for an existing account in local
        memory.
        """
        # Try to load the users info if they've already created an account
        self.refresh_token_file = MDApp.get_running_app().user_data_dir + "/refresh_token.txt"
        if self.debug:
            print("Looking for a refresh token in:", self.refresh_token_file)
        if os.path.exists(self.refresh_token_file):
            self.load_saved_account()

    def patch1(self, firstname, lastname, phonenumber, username, password):
        fname_data = {"fname": firstname}
        lname_data = {"lname": lastname} # Make a python dictionary
        pnumber_data = {"phonenumber": phonenumber}
        username_data = {"username": username}
        password_data = {"password": password}
        requests.patch(url=self.database_url, json=fname_data)

    def on_login_success(self, *args):
        pass
        
        print("Logged in successfully", args)

    

class LoadingScreen(Screen, MDApp):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoadingScreen(name='loading'))
sm.add_widget(LogInScreen(name='login'))
sm.add_widget(SignUpScreen(name='signup'))


class TestApp(MDApp):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()


