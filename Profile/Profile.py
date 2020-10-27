
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.font_definitions import theme_font_styles
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemableBehavior
from kivy.core.window import Window
from kivy.animation import Animation

KV = '''
<Example@FloatLayout>

    BoxLayout:
        orientation: "vertical"


        MDScrollViewRefreshLayout:
            id: refresh_layout
            refresh_callback: app.refresh_callback
            root_layout: root

            GridLayout:
                id: box
                size_hint_y: None
                height: self.minimum_height
                cols: 1

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

            Screen:
                id: screen_manager
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
                                size: "380dp", "280dp"
                                pos_hint: {"center_x": .5, "center_y": .6}
                                padding: "8dp"
                                

                                

                                AnchorLayout:
                                    anchor_x: 'left'
                                    anchor_y: 'top'
                    
                                    Image:
                                        id: avatar
                                        size_hint: None, None
                                        size: "66dp", "66dp"
                                        source: "data/logo/kivy-icon-256.png"
                                        height: avatar.height
                                        pos_hint: {"right": 1}

                                    
                                MDFloatingActionButton:
                                    icon: "plus"
                                    size: "46dp", "46dp"
                                    elevation_normal: 8
                                    md_bg_color: app.theme_cls.primary_color
                                    text_color: 1, 1, 1, 1

                            MDCard:
                                size_hint: None, None
                                size: "380dp", "140dp"
                                pos_hint: {"center_x": .5, "center_y": .3}
                                padding: "8dp"
                                
                                AnchorLayout:
                                    anchor_x: 'left'
                                    anchor_y: 'top'

                                    

                                
                                    
                                BoxLayout:
                                    size_hint_x: 19.
                                    spacing: "10dp"
                                    

                                    MDFloatingActionButton:
                                        icon: ""
                                        size: "46dp", "46dp"
                                        pos_hint: {"center_y": .4, "center_x": .6}
                                        elevation_normal: 8
                                        md_bg_color: 1, 0, 0, 0
                                        
                                    MDFloatingActionButton:
                                        icon: ""
                                        size: "46dp", "46dp"
                                        pos_hint: {"center_y": .4, "center_x": .5}
                                        elevation_normal: 8
                                        md_bg_color: 1, 0, 0, 0

                                    MDFloatingActionButton:
                                        icon: ""
                                        size: "46dp", "46dp"
                                        pos_hint: {"center_y": .4, "center_x": .5}
                                        elevation_normal: 8
                                        md_bg_color: 1, 0, 0, 0
                                
                                    MDFloatingActionButton:
                                        icon: ""
                                        size: "46dp", "46dp"
                                        pos_hint: {"center_y": .4, "center_x": .4}
                                        elevation_normal: 8
                                        md_bg_color: 1, 0, 0, 0

                                    MDFloatingActionButton:
                                        icon: ""
                                        size: "46dp", "46dp"
                                        pos_hint: {"center_y": .4}
                                        elevation_normal: 8
                                        md_bg_color: 1, 0, 0, 0

                                    MDIconButton:
                                        icon: "calendar"
                                        user_font_size: "54sp"
                                        pos_hint: {"center_y": .4}
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color

                            MDCard:
                                size_hint: None, None
                                size: "380dp", "200dp"
                                pos_hint: {"center_x": .5, "center_y": .1}
                                padding: "8dp"


                                BoxLayout:
                                    size_hint_x: 18.
                                    spacing: "10dp"
                                    

                                    MDIconButton:
                                        icon: "information"
                                        user_font_size: "60sp"
                                        text: "About"
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5,}

                                    MDIconButton:
                                        icon: "update"
                                        user_font_size: "60sp"
                                        text: "Update Profile"
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5,}

                                    MDIconButton:
                                        icon: "help-circle"
                                        user_font_size: "60sp"
                                        text: "Help & Support"
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5,}

                                    MDIconButton:
                                        icon: "sync"
                                        user_font_size: "60sp"
                                        pos_hint: {"center_y": .5}
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color

                            MDCard:
                                size_hint: None, None
                                size: "380dp", "100dp"
                                pos_hint: {"center_x": .5, "center_y": .1}
                                padding: "8dp"

                                FloatLayout:
                                    size_hint_x: 18.
                                    spacing: "10dp"

                                    MDIconButton:
                                        icon: "key-variant"
                                        user_font_size: "60sp"
                                        text: "Change Password"
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5, "center_x": .2}

                                    MDIconButton:
                                        icon: "settings"
                                        user_font_size: "60sp"
                                        text: "Settings"
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5, "center_x": .5}

                                    MDIconButton:
                                        icon: "exit-to-app"
                                        user_font_size: "60sp"
                                        text: "Sign out"
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        pos_hint: {"center_y": .5,"center_x": .8}
         
       
                                
                                    
    
    
    


                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'top'

                    MDToolbar:
                        title: "Profile"
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        right_action_items: [["magnify", lambda x: Search.callback()],["bell", lambda x: x]]
                    

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
        
class Profile(MDApp):
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



Profile().run()
