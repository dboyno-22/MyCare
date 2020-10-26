import os
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout 
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty


from kivymd.uix.list import OneLineAvatarIconListItem, MDList
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout

KV = '''
<OneLineAvatarIconListItem>:

    IconLeftWidget:
        icon: root.icon


Screen:

    NavigationLayout:

        ScreenManager:

            Screen:
                BoxLayout:
                    id: bl
                    orientation: 'vertical'
                    padding: 10, 10
                    pos_hint: {"center_x": .5, "center_y": .4}
                    size_hint_y: .82
                    size_hint_max_x: dp(500)
                    size_hint_min_x: min(dp(400), root.width)
                    

                    ScrollView:
                        
                        
        
            
        
                        GridLayout:
                            cols: 2
                            spacing: 10

                            MDCard:
                                canvas:
                                    Color:
                                        rgba: 0, .8, .6, .1
                                    Rectangle:
                                        size: self.size
                                        pos: self.pos
                                FloatLayout:
                                    size_hint_x: 18.
                                    spacing: "10dp"

                                    MDIconButton:
                                        icon: "pencil"
                                        user_font_size: "60sp"
                                        caption: "Personal info"
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5, "center_x": .2}

                                    MDTextButton:
                                        text: "Personal info"
                                        pos_hint: {"center_y": 0.5, "center_x": 0.6}
                                        theme_text_color: "Primary"
                                        font_style: "H5"
                                        bold: True
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        

                            MDCard:
                                canvas:
                                    Color:
                                        rgba: 0, .8, .6, .1
                                    Rectangle:
                                        size: self.size
                                        pos: self.pos 
                               
                                FloatLayout:
                                    size_hint_x: 18.
                                    spacing: "10dp"

                                    MDIconButton:
                                        icon: "bell"
                                        user_font_size: "60sp"
                                        caption: 'Notifications'
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5, "center_x": .2}

                                    MDTextButton:
                                        text: "Notifications"
                                        pos_hint: {"center_y": 0.5, "center_x": 0.6}
                                        theme_text_color: "Primary"
                                        font_style: "H5"
                                        bold: True
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        
                            
                            MDCard:
                                
                                canvas:
                                    Color:
                                        rgba: 0, .8, .6, .1
                                    Rectangle:
                                        size: self.size
                                        pos: self.pos
                                        
                                FloatLayout:
                                    size_hint_x: 18.
                                    spacing: "10dp"

                                    MDIconButton:
                                        icon: "settings"
                                        user_font_size: "60sp"
                                        caption: 'General'
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5, "center_x": .2}

                                    MDTextButton:
                                        text: "General"
                                        pos_hint: {"center_y": 0.5, "center_x": 0.6}
                                        theme_text_color: "Primary"
                                        font_style: "H5"
                                        bold: True
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        

                            MDCard:
                                canvas:
                                    Color:
                                        rgba: 0, .8, .6, .1
                                    Rectangle:
                                        size: self.size
                                        pos: self.pos
                                
                                FloatLayout:
                                    size_hint_x: 18.
                                    spacing: "10dp"

                                    MDIconButton:
                                        icon: "account"
                                        user_font_size: "60sp"
                                        caption: 'Account'
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5, "center_x": .2}
                                    
                                    MDTextButton:
                                        text: "Account"
                                        pos_hint: {"center_y": 0.5, "center_x": 0.6}
                                        theme_text_color: "Primary"
                                        font_style: "H5"
                                        bold: True
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        

                            MDCard:
                                canvas:
                                    Color:
                                        rgba: 0, .8, .6, .1
                                    Rectangle:
                                        size: self.size
                                        pos: self.pos

                                FloatLayout:
                                    size_hint_x: 18.
                                    spacing: "10dp"

                                    MDIconButton:
                                        icon: "lock"
                                        user_font_size: "60sp"
                                        caption: 'Privacy'
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5, "center_x": .2}
                                    
                                    MDTextButton:
                                        text: "Privacy"
                                        pos_hint: {"center_y": 0.5, "center_x": 0.6}
                                        theme_text_color: "Primary"
                                        font_style: "H5"
                                        bold: True
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        


                            MDCard:
                                canvas:
                                    Color:
                                        rgba: 0, .8, .6, .1
                                    Rectangle:
                                        size: self.size
                                        pos: self.pos

                                FloatLayout:
                                    size_hint_x: 18.
                                    spacing: "10dp"

                                    MDIconButton:
                                        icon: "devices"
                                        user_font_size: "60sp"
                                        caption: 'Devices'
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5, "center_x": .2}
                                    
                                    MDTextButton:
                                        text: "Devices"
                                        pos_hint: {"center_y": 0.5, "center_x": 0.6}
                                        theme_text_color: "Primary"
                                        font_style: "H5"
                                        bold: True
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        


                            

                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'top'
       
                    MDToolbar:
                        title: "Settings"
                        left_action_items: [["arrow-left", lambda x: x]]


                
                      

      


'''


class ContentNavigationDrawer(BoxLayout):
    pass

class FloatingButton(MDApp):
    def build(self):
        return Builder.load_string(KV)
        
class NavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)


class ListItem(OneLineAvatarIconListItem):
    icon = StringProperty("android")
    text = StringProperty()
    selected_item = BooleanProperty(False)
   
    

class Settings(MDApp):
    def build(self):
        return Builder.load_string(KV)



# Names of standard color themes.
        

Settings().run()
