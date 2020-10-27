from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty

from kivymd.uix.list import OneLineAvatarIconListItem, MDList, IRightBodyTouch,\
    OneLineIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivymd.uix.expansionpanel import MDExpansionPanelOneLine, MDExpansionPanel
from kivymd import images_path
from kivy.factory import Factory
from kivymd.theming import ThemableBehavior
from kivy.core.window import Window


KV = '''
#:import get_hex_from_color kivy.utils.get_hex_from_color

<StarButton@MDIconButton>
    icon: "star"
    on_release: self.icon = "star-outline" if self.icon == "star" else "star"
    

<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)


    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"



<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    
    


    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "MyCare library"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]


    MDLabel:
        text: "kivydevelopment@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    BoxLayout:
        orientation: "vertical"

        ScrollView:
            pos_hint: {"top": 1}

            DrawerList:
                id: md_list



Screen:

    NavigationLayout:

        ScreenManager:
            id: screen_manager
            Screen:

                BoxLayout:
                    orientation: 'vertical'
                    pos_hint: {"center_x": .5, "center_y": .4}
                    padding: 0, dp(16), 0, 0
                    size_hint_x: .75
                    size_hint_max_x: dp(400)
                    size_hint_min_x: min(dp(400), root.width)
                    
                    

                    ScrollView:
                        MDList:
                            id: scroll
                            pos_hint: {"center_x": .5}
                            bar_width: 0
                            orientation: "vertical"
                            spacing: "10dp"
                            
                            

                            MDCard:
                                size_hint: None, None
                                size: "380dp", "250dp"
                                pos_hint: {"center_x": .5, "center_y": .1}
                                padding: "8dp"

                                GridLayout:
                                    cols: 1
                                    adaptive_height: True
                                    padding: dp(4), dp(4)
                                    spacing: dp(15)
                                    
                                   
                                    
                                    
                                    

                                    SmartTileWithLabel:
                                        source: "Morninghabits.jpg"
                                        text: "[size=25]COVID-19 Update[/size]"
                                
                                    TwoLineAvatarIconListItem:
                                        halign: "left"
                                        spacing: "10dp"
                                        text: "[size=15]COVID-19 Storms the UK [/size]"
                                        secondary_text: "[size=10]The Times - Michelle Adams[/size]"
                                        on_size:
                                            self.ids._right_container.x = container.width
                                            self.ids._right_container.x = container.width
                                        
                                        IconLeftWidget:
                                            icon: "heart"
                                            user_font_size: "18sp"

                                        Container:
                                            id: container
                                            pos_hint: {"center_x": .6}
                                            

                                            MDIconButton:
                                                icon: "facebook"
                                                pos_hint: {"center_x": .6}
                                                user_font_size: "18sp"
                                                
                                                

                                            MDIconButton:
                                                icon: "twitter"
                                                pos_hint: {"center_x": 1}
                                                user_font_size: "18sp"

                                       
                            
                                
                                    
                            MDCard:
                                orientation: "vertical"
                                size_hint: None, None
                                size: "380dp", "100dp"
                                focus_behavior: True
                                ripple_behavior: True
                                pos_hint: {"center_x": .5, "center_y": .5}

                                BoxLayout:
                                    id: box_top
                                    
                                    adaptive_height: True
                                    pos_hint: {"center_x": .5, "center_y": .5}

                                    

                                    SmartTileWithLabel:
                                        source: "chemist.jpg"
                                        size_hint: None, .8

                                    
                                    
                                   

                                    ThreeLineAvatarIconListItem:
                                        text: "COVID-19"
                                        secondary_text: "[size=12]Will there be a second wave of Coronavirus - and How bad could it be? Here's what Doctors say[/size]"
                                        tertiary_text: "[size=10]Claire Chillwell[/size]"
                                        on_size:
                                            self.ids._right_container.x = container.width
                                            

                                        IconLeftWidget:
                                            icon: "newspaper"


                                        Container:
                                            id: container
                                            pos_hint: {"center_x": .5}
            

                                            

                                            MDIconButton:
                                                icon: "share"
                                                pos_hint: {"center_x": .6}
                                                user_font_size: "18sp"
                                                
                                                

                                            

                                
                                

                                        


               

                                
        
                                

                            MDCard:
                                orientation: "vertical"
                                size_hint: None, None
                                size: "380dp", "100dp"
                                focus_behavior: True
                                ripple_behavior: True
                                pos_hint: {"center_x": .5, "center_y": .5}

                                BoxLayout:
                                    id: box_top
                                    
                                    adaptive_height: True
                                    pos_hint: {"center_x": .5, "center_y": .5}

                                    

                                    SmartTileWithLabel:
                                        source: "bowldiet.jpg"
                                        size_hint: None, .8

                                    
                                    
                                   

                                    ThreeLineAvatarIconListItem:
                                        text: "COVID-19"
                                        secondary_text: "[size=12]What to buy when going shopping for groceries? - here is a personal diet guide whilst in Quarantine[/size]"
                                        tertiary_text: "[size=10]Claire Chillwell[/size]"
                                        on_size:
                                            self.ids._right_container.x = container.width
                                            

                                        IconLeftWidget:
                                            icon: "newspaper"


                                        Container:
                                            id: container
                                            pos_hint: {"center_x": .5}
            

                                            

                                            MDIconButton:
                                                icon: "share"
                                                pos_hint: {"center_x": .6}
                                                user_font_size: "18sp"


                            MDCard:
                                orientation: "vertical"
                                size_hint: None, None
                                size: "380dp", "100dp"
                                focus_behavior: True
                                ripple_behavior: True
                                pos_hint: {"center_x": .5, "center_y": .5}

                                BoxLayout:
                                    id: box_top
                                    
                                    adaptive_height: True
                                    pos_hint: {"center_x": .5, "center_y": .5}

                                    

                                    SmartTileWithLabel:
                                        source: "jogger.jpg"
                                        size_hint: None, .8

                                    
                                    
                                   

                                    ThreeLineAvatarIconListItem:
                                        text: "COVID-19"
                                        secondary_text: "[size=12]Yes were in Quarantine [/size]"
                                        tertiary_text: "[size=10]Claire Chillwell[/size]"
                                        on_size:
                                            self.ids._right_container.x = container.width
                                            

                                        IconLeftWidget:
                                            icon: "newspaper"


                                        Container:
                                            id: container
                                            pos_hint: {"center_x": .5}
            

                                            

                                            MDIconButton:
                                                icon: "share"
                                                pos_hint: {"center_x": .6}
                                                user_font_size: "18sp"

                            MDCard:
                                orientation: "vertical"
                                size_hint: None, None
                                size: "380dp", "100dp"
                                focus_behavior: True
                                ripple_behavior: True
                                pos_hint: {"center_x": .5, "center_y": .5}

                                BoxLayout:
                                    id: box_top
                                    
                                    adaptive_height: True
                                    pos_hint: {"center_x": .5, "center_y": .5}

                                    

                                    SmartTileWithLabel:
                                        source: "stethoscope.jpg"
                                        size_hint: None, .8

                                    
                                    
                                   

                                    ThreeLineAvatarIconListItem:
                                        text: "COVID-19"
                                        secondary_text: "[size=12]How has the NHS responded since COVID-19 hit the UK?[/size]"
                                        tertiary_text: "[size=10]Claire Chillwell[/size]"
                                        on_size:
                                            self.ids._right_container.x = container.width
                                            

                                        IconLeftWidget:
                                            icon: "newspaper"


                                        Container:
                                            id: container
                                            pos_hint: {"center_x": .5}
            

                                            

                                            MDIconButton:
                                                icon: "share"
                                                pos_hint: {"center_x": .6}
                                                user_font_size: "18sp"

        
                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'top'

                    MDToolbar:
                        title: "NewsFeed"
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        right_action_items: [["magnify", lambda x: Search.callback()],["clock", lambda x: app.callback_2()]]
                    

                    Widget:


        
        MDNavigationDrawer:
            id: nav_drawer
             
           
            ContentNavigationDrawer:
                id: content_drawer
                screen_manager: screen_manager
                nav_drawer: nav_drawer

    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
        callback: app.callback
        label_text_color: 1,1,1,1
        color_icon_root_button: 1,1,1,1
        color_icon_stack_button: 1,1,1,1
'''
class Container(IRightBodyTouch, BoxLayout):
    adaptive_width = True

class Content(BoxLayout):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def hide_content_drawer(self):
        Animation(x=Window.width, d=0.2).start(self.ids.content_drawer)

    def show_content_drawer(self):
        Animation(x=Window.width - self.ids.content_drawer.width, d=0.2).start(
            self.ids.content_drawer
        )

    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color: 
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color
        

class News(MDApp):
    data = {
        "calendar": "Appointment",
        "robot": "Chatbot",
        "heart-pulse": "Lifestyle",
    }

    def callback(self, instance):
        print(instance.icon)

    def build(self):
        return Builder.load_string(KV)


    def on_start(self):
        icons_item = {
            "compass": "Discovery",
            "account":"Profile",
            "mail":"Messages",
            "bell":"Notifications",
            "heart":"Lifestyle",
            "calendar":"Appointment",
            "map-marker":"Map",
            "newspaper":"NewsFeed",
            "settings":"Settings",
            "plus":"Add widgets",
            "sync":"Link NHS number",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )     
    
News().run()
