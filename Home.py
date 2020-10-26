from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty

from kivymd.theming import ThemeManager
from kivymd.uix.menu import MDDropdownMenu

from kivymd.uix.list import OneLineAvatarIconListItem, MDList,\
OneLineIconListItem, TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.theming import ThemableBehavior
from kivy.animation import Animation
from kivy.core.window import Window
from kivymd.uix.behaviors.elevation import RectangularElevationBehavior
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton,\
    MDRaisedButton
from kivymd.uix.behaviors.backgroundcolorbehavior import BackgroundColorBehavior
from kivy.event import EventDispatcher
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.dialog import MDDialog
from kivy.app import App
from kivy.clock import Clock
from kivy.garden.mapview import MapView, MapMarker

from kivy.uix.button import Button
from kivy.garden.mapview import MapMarkerPopup
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivy.animation import Animation
from kivy.core.window import Window
from kivymd.icon_definitions import md_icons
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout


import pprint
import requests
import json
from kivymd.uix.expansionpanel import MDExpansionPanel,\
    MDExpansionPanelThreeLine

Builder.load_string("""
<Search>: 

    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": .5, "center_y": .4}
        padding: 0, dp(16), 0, 0
        size_hint_x: .75
        
       


        BoxLayout:
            size_hint_y: None
            height: self.minimum_height

            MDIconButton:
                icon: 'magnify'
                

            MDTextField:
                id: search_field
                hint_text: 'Search'
                on_text: root.set_list(self.text, True)
                size_hint_x: 5.
                
            AnchorLayout:
                anchor_x: 'right'
                anchor_y: 'top'

                MDFloatingActionButton:
                    icon: "microphone"
                    md_bg_color: app.theme_cls.primary_color


        RecycleView:
            id: search_results_list
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'



    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'

        MDToolbar:
            title: "Search"
            left_action_items: [["arrow-left", lambda x: app.callback12()]]
            right_action_items: [["dots-vertical", lambda x: x],["clock", lambda x: x]]
                    


<ProfileScreen>:
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
                        title: "Home"
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        right_action_items: [["magnify", lambda x: app.callback6()],["bell", lambda x: app.callback7()]]

                        
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

<MessageScreen>:

    NavigationLayout:
        ScreenManager:
            id : screen_manager
            Screen:
                name: 'home screen'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Messages'
                        pos_hint: {'top': True}
                        left_action_items: [["menu", lambda x: print(x)]]
                        right_action_items : [['magnify', lambda x: print(x)], ['dots-vertical', lambda x : print(x)]]
                    MDTabs:	
                        Tab:			
                            # INDIVIDUAL TABS CONTENT GOES HERE !!
                            text: 'CHATS'
                            ScrollView:
                                MDList:
                                    TwoLineAvatarListItem:
                                        text: 'sentdex'
                                        secondary_text: 'Some random msg !!.'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'Andrew'
                                        secondary_text: 'LOL !'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'starmer'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'alfredo'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarIconListItem:
                                        text: 'Chartbusters'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        IconLeftWidget:
                                            icon: "account-group-outline"
                                    TwoLineAvatarListItem:
                                        text: 'Ng'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'krish'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarIconListItem:
                                        text: 'Swaggers'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        IconLeftWidget:
                                            icon : "account-group-outline"
                                    TwoLineAvatarListItem:
                                        text: 'joshua'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'naik'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'thakur'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: '3blue1brown'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'Abhishek'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'Nick'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'white'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'Errichto'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                                    TwoLineAvatarListItem:
                                        text: 'Aryan'
                                        secondary_text: 'Some random msg !!'
                                        on_press:
                                            root.change_screen('chat screen', title = self.text)
                                        ImageLeftWidget:
                                            source: "data/logo/kivy-icon-256.png"
                            FloatLayout:
                                MDFloatingActionButton:
                                    md_bg_color :  app.theme_cls.primary_color
                                    text_color : (1, 1, 1, 1)
                                    icon : 'message-reply-text'
                                    size : 45, 45
                                    pos : root.width - 1.5*self.width,  root.y + self.height//2
                                    on_press:
                                        root.change_screen('select contact')
                        
                        Tab:
                            # INDIVIDUAL TABS CONTENT GOES HERE !!
                            text: 'CALLS'
                            ScrollView:
                                MDList:
                                    TwoLineAvatarIconListItem:
                                        text : 'kevin'
                                        secondary_text : '30 March,8:53 PM'
                                        IconLeftWidget:
                                            icon : 'emoticon-cool-outline'
                                        IconRightWidget:
                                            icon : 'phone'
                                            theme_text_color : 'Custom'
                                            text_color :  app.theme_cls.primary_color
                                    TwoLineAvatarIconListItem:
                                        text : 'Jeff'
                                        secondary_text : '30 March,8:53 PM'
                                        IconLeftWidget:
                                            icon : 'emoticon-excited-outline'
                                        IconRightWidget:
                                            icon : 'phone'
                                            theme_text_color : 'Custom'
                                            text_color :  app.theme_cls.primary_color
                                    TwoLineAvatarIconListItem:
                                        text : 'Markham'
                                        secondary_text : '30 March,8:53 PM'
                                        IconLeftWidget:
                                            icon : 'emoticon-cool-outline'
                                        IconRightWidget:
                                            icon : 'phone'
                                            theme_text_color : 'Custom'
                                            text_color :  app.theme_cls.primary_color
                                    TwoLineAvatarIconListItem:
                                        text : 'heaton'
                                        secondary_text : '30 March,8:53 PM'
                                        IconLeftWidget:
                                            icon : 'emoticon-excited-outline'
                                        IconRightWidget:
                                            icon : 'phone'
                                            theme_text_color : 'Custom'
                                            text_color :  app.theme_cls.primary_color
                                    TwoLineAvatarIconListItem:
                                        text : 'Corey'
                                        secondary_text : '30 March,8:53 PM'
                                        IconLeftWidget:
                                            icon : 'emoticon-neutral-outline'
                                        IconRightWidget:
                                            icon : 'phone'
                                            theme_text_color : 'Custom'
                                            text_color :  app.theme_cls.primary_color
                                    TwoLineAvatarIconListItem:
                                        text : 'Daniel'
                                        secondary_text : '30 March,8:53 PM'
                                        IconLeftWidget:
                                            icon : 'emoticon-happy-outline'
                                        IconRightWidget:
                                            icon : 'phone'
                                            theme_text_color : 'Custom'
                                            text_color :  app.theme_cls.primary_color
                                    TwoLineAvatarIconListItem:
                                        text : 'Dojo'
                                        secondary_text : '30 March,8:53 PM'
                                        IconLeftWidget:
                                            icon : 'emoticon-neutral-outline'
                                        IconRightWidget:
                                            icon : 'phone'
                                            theme_text_color : 'Custom'
                                            text_color : app.theme_cls.primary_color
                                    TwoLineAvatarIconListItem:
                                        text : 'Bourke'
                                        secondary_text : '30 March,8:53 PM'
                                        IconLeftWidget:
                                            icon : 'emoticon-happy-outline'
                                        IconRightWidget:
                                            icon : 'phone'
                                            theme_text_color : 'Custom'
                                            text_color :  app.theme_cls.primary_color
                                    TwoLineAvatarIconListItem:
                                        text : 'Jackson'
                                        secondary_text : '30 March,8:53 PM'
                                        IconLeftWidget:
                                            icon : 'emoticon-neutral-outline'
                                        IconRightWidget:
                                            icon : 'phone'
                                            theme_text_color : 'Custom'
                                            text_color : app.theme_cls.primary_color
                                    TwoLineAvatarIconListItem:
                                        text : ''
                            FloatLayout:
                                MDFloatingActionButton:
                                    md_bg_color :  app.theme_cls.primary_color
                                    text_color : (1, 1, 1, 1)
                                    icon : 'call-made'
                                    size : 45, 45
                                    pos : root.width - 1.5*self.width, root.y + self.height//2
                                    on_press:
                                        app.change_screen('select contact2')

            Screen:
                name : 'update status'
                FloatLayout:
                    canvas:
                        Color:
                            rgb: (0.4, 0.2, 0.5)
                        Rectangle:
                            size : self.size
                            pos : self.pos
                    MDIconButton:
                        icon : 'keyboard-backspace'
                        md_bg_color : (0.4, 0.2, 0.5, 1)
                        theme_text_color : 'Custom'
                        text_color : (1, 1, 1, 1)
                        size_hint: (None, None)
                        pos_hint : {'top' : True}
                        on_press:
                            app.change_screen('home screen', 'back')
                    MDLabel:
                        text : 'Type a status'
                        halign: 'center'
                        theme_text_color : 'Custom'
                        text_color : (1, 1, 1, 1)
                        font_size: '25sp'
                    MDList:
                        OneLineIconListItem:
                            md_bg_color : (0.5, 0.5, 0.8, 1)
                            text : 'Status (Custom)'
                            theme_text_color : 'Custom'
                            text_color : (1, 1, 1, 1)
                            pos_hint: {'bottom': True}
                            IconLeftWidget:	
                                icon : 'chevron-right'
                                theme_text_color : 'Custom'
                                text_color : (1, 1, 1, 1)
                    MDIconButton:
                        icon : 'emoticon-excited'
                        md_bg_color : (0.4, 0.2, 0.5, 1)
                        theme_text_color : 'Custom'
                        text_color : (1, 1, 1, 1)
                        #size_hint: (None, None)
                        pos : root.x + self.width, root.y + 0.8*self.height
                    MDIconButton:
                        icon : 'format-text'
                        md_bg_color : (0.4, 0.2, 0.5, 1)
                        theme_text_color : 'Custom'
                        text_color : (1, 1, 1, 1)
                        #size_hint: (None, None)
                        pos : root.x + 2*self.width, root.y + 0.8*self.height
                    MDIconButton:
                        icon : 'palette'
                        md_bg_color : (0.4, 0.2, 0.5, 1)
                        theme_text_color : 'Custom'
                        text_color : (1, 1, 1, 1)
                        #size_hint: (None, None)
                        pos : root.x + 3*self.width, root.y + 0.8*self.height

            Screen:
                name : 'select contact2'	
                BoxLayout:
                    orientation : 'vertical'
                    MDToolbar:
                        id : toolbar2
                        pos_hint : {'top' : True}
                        title : 'Select contact'
                        left_action_items : [['keyboard-backspace', lambda x : app.change_screen('home screen', 'back')]]
                        right_action_items : [['magnify', lambda x : print('search')], ['dots-vertical', lambda x : print('vertical-dots')]]
                    ScrollView:
                        MDList:
                            OneLineAvatarIconListItem:
                                text : 'New group call' # account-multiple
                                IconLeftWidget:
                                    icon : 'account-multiple'
                            OneLineAvatarIconListItem:
                                text : 'New contact' # account-plus
                                IconLeftWidget:
                                    icon : 'account-plus'

            Screen:
                name : 'select contact'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        id : toolbar
                        pos_hint: {'top': True}
                        title: 'Select contact'
                        right_action_items : [['magnify', lambda x : print('search')], ['dots-vertical', lambda x : print(x)]]
                        left_action_items : [['keyboard-backspace', lambda x : app.change_screen('home screen', 'back')]]
                    ScrollView:
                        MDList:
                            OneLineAvatarIconListItem:
                                text : 'New group'
                                IconLeftWidget:
                                    icon : 'account-multiple'
                                    md_bg_color : (0.145, 0.827, 0.4, 1)
                                    size_hint: (1, 1)
                            OneLineAvatarIconListItem:
                                text : 'New contact'
                                IconLeftWidget:
                                    icon : 'account-plus'
                                    md_bg_color : (0.145, 0.827, 0.4, 1)
                                    size_hint: (1, 1)								
                            TwoLineAvatarIconListItem:
                                text : 'Andrew'
                                secondary_text : 'Hey there! I am using WhatsApp.'
                                on_press:
                                    app.change_screen('chat screen', title = self.text)
                                IconLeftWidget:
                                    icon : 'face-woman'						
                            TwoLineAvatarIconListItem:
                                text : 'Gabbard'
                                secondary_text : 'Hey there! I am using WhatsApp.'
                                on_press:
                                    app.change_screen('chat screen', title = self.text)
                                IconLeftWidget:
                                    icon : 'face-woman-outline'						
                            TwoLineAvatarIconListItem:
                                text : 'Kevin'
                                secondary_text : 'Hey there! I am using WhatsApp.'	
                                on_press:
                                    app.change_screen('chat screen', title = self.text)
                                IconLeftWidget:
                                    icon : 'face-woman'					
                            TwoLineAvatarIconListItem:
                                text : 'Dojo'
                                secondary_text : 'Hey there! I am using WhatsApp.'
                                on_press:
                                    app.change_screen('chat screen', title = self.text)
                                IconLeftWidget:
                                    icon : 'face-woman-outline'						
                            TwoLineAvatarIconListItem:
                                text : 'Markham'
                                secondary_text : 'Hey there! I am using WhatsApp.'
                                on_press:
                                    app.change_screen('chat screen', title = self.text)
                                IconLeftWidget:
                                    icon : 'face-woman'						
                            TwoLineAvatarIconListItem:
                                text : 'Daniel'
                                secondary_text : 'Hey there! I am using WhatsApp.'	
                                on_press:
                                    app.change_screen('chat screen', title = self.text)
                                IconLeftWidget:
                                    icon : 'face-woman-outline'					
                            TwoLineAvatarIconListItem:
                                text : 'Krish'
                                secondary_text : 'Hey there! I am using WhatsApp.'
                                on_press:
                                    app.change_screen('chat screen', title = self.text)
                                IconLeftWidget:
                                    icon : 'face-woman-outline'						
                            TwoLineAvatarIconListItem:
                                text : 'Erik'
                                secondary_text : 'Hey there! I am using WhatsApp.'
                                on_press:
                                    app.change_screen('chat screen', title = self.text)
                                IconLeftWidget:
                                    icon : 'face-woman'						
                            TwoLineAvatarIconListItem:
                                text : 'Julian'
                                secondary_text : 'Hey there! I am using WhatsApp.'	
                                on_press:
                                    app.change_screen('chat screen', title = self.text)
                                IconLeftWidget:
                                    icon : 'face-woman'					
                            TwoLineAvatarIconListItem:
                                text : 'Jeff'
                                secondary_text : 'Hey there! I am using WhatsApp.'
                                on_press:
                                    app.change_screen('chat screen', title = self.text)
                                IconLeftWidget:
                                    icon : 'face-woman-outline'
            Screen:
                name : 'chat screen'	
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        id : toolbar_chat_screen
                        pos_hint: {'top': True}
                        right_action_items : [['video', lambda x : print('video call')], ['phone', lambda x : print('calling..')], ['dots-vertical', lambda x : print('OPTIONS NOT ACCESSIBLE...')]]
                        left_action_items : [['keyboard-backspace', lambda x : app.change_screen('home screen', curr = 'back')]]
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                            OneLineListItem:
                                text : 'Chat content (scrollable)'
                FloatLayout:
                    MDTextFieldRound:
                        hint_text : 'Type a message'
                        icon_left : 'emoticon-outline'
                        normal_color : 1, 1, 1, 1
                        color_active : 1, 1, 1, 1
                        icon_right : 'paperclip'
                        size_hint: (0.59, 0.08)
                        pos : root.x + self.height/1.5, root.y + self.height//5
                    MDFloatingActionButton:
                        md_bg_color : (0.145, 0.827, 0.4, 1)
                        text_color : (1, 1, 1, 1)
                        icon : 'microphone'
                        size : 45, 45
                        pos : root.width - 1.25*self.width, 0.2*self.width
                        size : 47, 47
<NotificationsScreen>:
    
    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'
                    pos_hint: {"center_x": .5, "center_y": .4}
                    padding: 0, dp(16), 0, 0
                    
                    
                    ScrollView:
                        GridLayout:
                            id: box
                            cols: 1
                            adaptive_height: True


                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'top'

                    MDToolbar:
                        title: "Notifications"
                        left_action_items: [["arrow-left", lambda x: app.callback12()]]
                        right_action_items: [["magnify", lambda x: Search.callback()],["clock", lambda x: app.callback_2()]]

<Content1>
    adaptive_height: True

    TwoLineIconListItem:
        text: "(050)-123-45-67"
        secondary_text: "Mobile"

        IconLeftWidget:
            icon: 'phone'
                    
<LifestyleScreen>:
<AppointmentScreen>:
    MDBackdrop:
        id: backdrop
        on_open: print("on_open")
        on_close: print("on_close")
        left_action_items: [["menu", lambda x: self.open()]]
        header_text: "Menu:"
        right_action_items: [["arrow-left", lambda x: app.callback12()]]

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                backlayer: backlayer
<MapScreen>:
    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    
                    MDBottomNavigation:
                        panel_color: .2, .2, .2, 1
                        halign: "center"
                        
                    

                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Directions'
                            icon: "directions"

                            canvas:
                                Color:
                                    rgba: 0, .7, 1, 1
                                RoundedRectangle:
                                    size : self.size
                                    pos : self.pos
                                Color:
                                    rgba : (1, 1, 1, 1)
                                RoundedRectangle:
                                    size : self.size[0], self.size[1] - 0.45*self.size[1]
                            
                            
                            
                            MDTextFieldRound:
                                hint_text : 'search'
                                icon_left : 'magnify'
                                size_hint: (0.7, 0.06)
                                pos_hint: {'x': 0.15, 'center_y' : 0.725}
                                color_mode : 'custom'
                                normal_color : (1, 1, 1, 1)
                                active_color : (1, 1, 1, 1)

                           

                        MDBottomNavigationItem:
                            name: 'screen 2'
                            text: 'Nearby GP'
                            icon: "hospital-marker"

                            FloatLayout: 
                                pos_hint: {"center_x": .5, "center_y": .4}

                                BoxLayout: 
                                    pos_hint_y: 0.5
                                    size_hint_y: 0.8

                                
                                    ScrollView:
                                        
                                        GridLayout:
                                            rows: 1
                                            spacing: dp(10)
                                            width: self.minimum_width
                                            size_hint_x: None
                                            size_hint_y: 0.3
                                            


                                            GPScreenElevationButton:
                                                FitImage:
                                                    source: "Gp1.jpg"
                                                    size_hint: 1., 1.
                                                    on_press:
                                                        

                                                FloatLayout:
                                                    
                                                    MDFloatingActionButton:
                                                        icon: "map-marker"
                                                        md_bg_color: app.theme_cls.primary_color
                                                        pos_hint: {"center_x": .95, "center_y": .3}

                                                FloatLayout:
                                                    pos_hint: {"center_x": .4, "center_y": .1}

                                                    MDLabel:
                                                        text: "0.1km"
                                                        font_size: "12sp"
                                                        halign: "right"
                                                
                                                    
                                                        



                                            GPScreenElevationButton:
                                                FitImage:
                                                    source: "Gp2.jpg"
                                                    size_hint: 1, 0.75
                                                    on_press:
                                                        


                                                FloatLayout:
                                                    
                                                    MDFloatingActionButton:
                                                        icon: "map-marker"
                                                        md_bg_color: app.theme_cls.primary_color
                                                        pos_hint: {"center_x": .95, "center_y": .3}

                                                MDLabel:


                                            GPScreenElevationButton:
                                                FitImage:
                                                    source: "Gp3.jpg"
                                                    size_hint: 1, 0.75
                                                    on_press:
                                                        


                                                FloatLayout:
                                                    
                                                    MDFloatingActionButton:
                                                        icon: "map-marker"
                                                        md_bg_color: app.theme_cls.primary_color
                                                        pos_hint: {"center_x": .95, "center_y": .3}
                                                MDLabel:


                                            GPScreenElevationButton:
                                                FitImage:
                                                    source: "Gp4.png"
                                                    size_hint: 1, 0.75

                                                FloatLayout:
                                                    
                                                    MDFloatingActionButton:
                                                        icon: "map-marker"
                                                        md_bg_color: app.theme_cls.primary_color
                                                        pos_hint: {"center_x": .95, "center_y": .3}

                                                MDLabel:


                                            GPScreenElevationButton:
                                                FitImage:
                                                    source: "Gp5.jpg"
                                                    size_hint: 1, 0.75
                                                
                                                FloatLayout:
                                                    
                                                    MDFloatingActionButton:
                                                        icon: "map-marker"
                                                        md_bg_color: app.theme_cls.primary_color
                                                        pos_hint: {"center_x": .95, "center_y": .3}

                                                MDLabel:


                            GridLayout:
                                rows: 1
                                spacing: dp(10)
                                size_hint_y: 0.9


                                

                                MDFillRoundFlatButton: 
                                    text: "Nearby"
                                    width: dp(250)
                                    elevation: 5


                                MDFillRoundFlatButton: 
                                    text: "Recommended"
                                    width: dp(250)
                                    elevation: 5

                                MDFillRoundFlatButton: 
                                    text: "Popular"
                                    width: dp(250)
                                    elevation: 5

                                MDFillRoundFlatButton: 
                                    text: "Open"
                                    width: dp(250)
                                    elevation: 5

                                MDFillRoundFlatButton: 
                                    text: "Distance"
                                    width: dp(250)
                                    elevation: 5

                                
                            AnchorLayout:
                                anchor_x: 'center'
                                anchor_y: 'top'

                                MDToolbar:
                                    title: 'Nearby GPs'
                                    pos_hint: {'top': True}
                                    left_action_items: [["menu", lambda x: print(x)]]
                                    right_action_items: [['magnify', lambda x: print(x)], ['dots-vertical', lambda x : print(x)]]

                        

                           

                        MDBottomNavigationItem:
                            name: 'screen 3'
                            text: 'My GP'
                            icon: "hospital-building"

                            canvas:
                                Color:
                                    rgba: 0, .7, 1, 1
                                RoundedRectangle:
                                    size : self.size
                                    pos : self.pos
                                Color:
                                    rgba : (1, 1, 1, 1)
                                RoundedRectangle:
                                    size : self.size[0], self.size[1] - 0.45*self.size[1]

                            BoxLayout: 

                                FloatLayout: 
                                    MDCard: 
                                        size_hint: None, None
                                        size: "400dp", "200dp"
                                        pos_hint: {"center_x": .5, "center_y": .7}
                                        focus_behavior: True
                                        ripple_behavior: True
                                        elevation: 5

                                        FitImage:
                                            source: "Gp4.png"
                                            size_hint: 1, 1

                            BoxLayout: 
                                FloatLayout: 
                                    
                                    MDCard: 
                                        size_hint: None, None
                                        size: "320dp", "280dp"
                                        pos_hint: {"center_x": .5, "center_y": .3}
                                        focus_behavior: True
                                        ripple_behavior: True
                                        elevation: 5

                                        ScrollView:

                                            MDList:

                                                ThreeLineListItem:
                                                    text: "City Health Centre"
                                                    secondary_text: "Family practice physician in Manchester, England"
                                                    tertiary_text: "General Practice"

                                                OneLineAvatarIconListItem:
                                                    halign: "left"
                                                    spacing: "10dp"
                                                    text: "[size=15]4.2 - Google reviews [/size]"
                                                

                                                    IconLeftWidget:
                                                        icon: "star"
                                                        user_font_size: "18sp"

                                                OneLineAvatarIconListItem:
                                                    halign: "left"
                                                    spacing: "10dp"
                                                    text: "[size=15]Address: 32 Market St, Manchester M1 1PL[/size]"


                                                    IconLeftWidget:
                                                        icon: "map-marker"
                                                        user_font_size: "18sp"

                                                
                                                OneLineAvatarIconListItem:
                                                    halign: "left"
                                                    spacing: "10dp"
                                                    text: "[size=15]Hours: Opens 8AM - Closes 6PM[/size]"


                                                    IconLeftWidget:
                                                        icon: "clock"
                                                        user_font_size: "18sp"

                                                
                                                OneLineAvatarIconListItem:
                                                    halign: "left"
                                                    spacing: "10dp"
                                                    text: "[size=15]Phone: 0161 839 6227[/size]"


                                                    IconLeftWidget:
                                                        icon: "phone"
                                                        user_font_size: "18sp"

                                                    
                                        

                                                    

                                                

                                            



                        MDBottomNavigationItem:
                            name: 'screen 4'
                            text: 'Map'
                            icon: "map-marker"

                            Screen:
   
                                BoxLayout:
                                    orientation: 'vertical'
                                    MDToolbar:
                                        title: "Directions"
                                        right_action_items: [['magnify', lambda x: app.show_confirmation_dialog()]]
                                        md_bg_color: app.theme_cls.primary_color

                                    FarmersMapView:
                                        id: mapview

                            
                                        

                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'top'

                    MDToolbar:
                        title: "Map"
                        left_action_items: [["arrow-left", lambda x: app.callback12()]]
<NewsScreen>:
<SettingsScreen>:
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
                        left_action_items: [["arrow-left", lambda x: app.callback12()]]

<WidgetsScreen>:
<LinkScreen>:


<StarButton@MDIconButton>
    icon: "star"


<FarmersMapView>:
    
    

    MapMarkerPopup:
        lon: 11
        lat: 11


<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        hint_text: "City"

    MDTextField:
        hint_text: "Street"
    
<GPScreenElevationButton>:
	#size_hint : (0.4, 0.25)
	width: dp(300)
	height: dp(500)
	elevation: 10
	md_bg_color: (1, 1, 1, 1)
	text_color: rgba('#FFC7B8F5')



<RectangularElevationButton>:
	size_hint: (0.44, 0.09)
	elevation : 8
	md_bg_color : (1, 1, 1, 1)
	text_color : rgba('#9370DB')

<LifestyleScreenElevationButton>:
	#size_hint : (0.4, 0.25)
	width: dp(200)
	height : dp(100)
	elevation : 10
	md_bg_color : (1, 1, 1, 1)
	text_color : rgba('#FFC7B8F5')

<RectangularElevationListItem>:
	md_bg_color : (1, 1, 1, 1)
	size_hint: (0.9, None)
	elevation : 8


<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)


    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color



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
                
                OneLineIconListItem:
                    text: "Discovery"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.callback11()

                    IconLeftWidget:
                        icon: "compass"

                OneLineIconListItem:
                    text: "Profile"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.callback()

                    IconLeftWidget:
                        icon:  "account"

                OneLineIconListItem:
                    text: "Messages"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.callback1()
                   
                    IconLeftWidget:
                        icon: "mail"
                        
                
                OneLineIconListItem:
                    text: "Notifications"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.callback7()

                    IconLeftWidget:
                        icon: "bell"

                OneLineIconListItem:
                    text: "Lifestyle"
                    on_press: 
                        root.nav_drawer.set_state("close")
                        root.callback4()

                    IconLeftWidget:
                        icon: "heart"

                OneLineIconListItem:
                    text: "Appointment"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.callback5()
                    
                    IconLeftWidget:
                        icon: "calendar"


                OneLineIconListItem:
                    text: "Map"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.callback2()

                    IconLeftWidget:
                        icon: "map-marker"

                OneLineIconListItem:
                    text: "NewsFeed"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.callback10()

                    IconLeftWidget:
                        icon: "newspaper"

                OneLineIconListItem:
                    text: "Settings"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.callback4()

                    IconLeftWidget:
                        icon: "settings"

                OneLineIconListItem:
                    text: "Add widgets"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.callback8()
                    
                    IconLeftWidget:
                        icon: "plus"
                
                OneLineIconListItem:
                    text: "Link NHS Patient No."
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.callback9()
                    
                    IconLeftWidget:
                        icon: "sync"
                




<ItemBackdropFrontLayer@TwoLineAvatarListItem>:
    icon: "android"

    IconLeftWidget:
        icon: root.icon


<ItemBackdropBackLayer>
    size_hint_y: None
    height: self.minimum_height
    spacing: "10dp"

    canvas:
        Color:
            rgba:
                root.theme_cls.primary_dark if root.selected_item \
                else root.theme_cls.primary_color
        RoundedRectangle:
            pos: self.pos
            size: self.size

    MDIconButton:
        icon: root.icon
        theme_text_color: "Custom"
        text_color: 1, 1, 1, .5 if not root.selected_item else 1, 1, 1, 1

    MDLabel:
        text: root.text
        color: 1, 1, 1, .5 if not root.selected_item else 1, 1, 1, 1


<ItemBackdropBackLayerOfSecondScreen@BoxLayout>:
    size_hint_y: None
    height: "40dp"
    spacing: "25dp"
    text: ""

    MDCheckbox:
        size_hint: None, None
        size: "30dp", "30dp"
        active: False or self.active
        pos_hint: {"center_y": .5}
        selected_color: 1, 1, 1, 1

    MDLabel:
        text: root.text
        color: 1, 1, 1, .7

   



<ItemRoundBackdropBackLayerOfSecondScreen@BoxLayout>:
    size_hint_y: None
    height: "40dp"
    spacing: "25dp"
    text: ""

    MDCheckbox:
        group: "size"
        size_hint: None, None
        size: "30dp", "30dp"
        pos_hint: {"center_y": .5}
        selected_color: 1, 1, 1, 1

    MDLabel:
        text: root.text
        color: 1, 1, 1, .7


<MyBackdropFrontLayer@ScrollView>
    backdrop: None
    backlayer: None

    GridLayout:
        size_hint_y: None
        height: self.minimum_height
        cols: 1
        padding: "5dp"

        ItemBackdropFrontLayer:
            text: "Press to Choose Location"
            secondary_text: "Appointment Location"
            icon: "map-marker"
            on_press:
                root.backlayer.current = "second screen"
                root.backdrop.open()

        ItemBackdropFrontLayer:
            text: "Press to Select a Date"
            secondary_text: "Appointment Date"
            icon: "calendar-month"
            on_press:
                app.show_date_picker()

        ItemBackdropFrontLayer:
            text: "Press to Choose a Time"
            secondary_text: "Appointment Time"
            icon: "clock"
            on_press:
                app.show_time_picker()
                
        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: self.minimum_height
            spacing: 10
            padding: dp(48)

            MDTextField:
                hint_text: "Location"
                mode: "rectangle"

            MDTextField:
                id: date_picker_label
                hint_text: "Date"
                mode: "rectangle"

            MDTextField:
                id: time_picker_label
                hint_text: "Time"
                mode: "rectangle"
                
            MDTextField:
                hint_text: "Reason for Appointment"
                mode: "rectangle"

            MDTextField:
                hint_text: "Notes"
                mode: "rectangle"

            MDTextField:
                hint_text: "Any prescribed medication"
                mode: "rectangle"
                icon_right: "arrow-down-drop-circle-outline"
                icon_right_color: app.theme_cls.primary_color

            MDTextField:
                hint_text: "First name"
                mode: "rectangle"

            MDTextField:
                hint_text: "Last name"
                mode: "rectangle"

            MDTextField:
                hint_text: "Email"
                mode: "rectangle"



            MDSeparator:
            StackLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                

                MDRectangleFlatButton:
                    text: "Confirm"
                    size_hint: None, None
                    orientation: "vertical"
                    pos_hint: {"right": 1} 
                   
            
                MDRectangleFlatButton:
                    text: "Cancel"
                    size_hint: None, None
                    orientation: "vertical"
                    pos_hint: {"right": 1} 
                    on_press:  root.manager.backdrop.current = 'home'




<MyBackdropBackLayer@ScreenManager>:
    

    
   
    Screen:
        name: "second screen"

        ScrollView

            GridLayout:
                size_hint_y: None
                height: self.minimum_height
                cols: 1
                padding: "15dp"
                spacing: "10dp"

                MDLabel:
                    text: "Choose a local GP"
                    color: 1, 1, 1, 1
                    

                

                Widget:
                    size_hint_y: None
                    height: "10dp"

                MDTextField:
                    hint_text: "Location"
                    text_color: 1, 1, 1, 1
                    color_mode: 'custom'
                    helper_text_mode: "on_focus" 
                    line_color_focus: 1, 1, 1, 1
                    icon_right: "map-marker"
                    icon_right_color: 1, 1, 1, 1
                                    

               

                MDLabel:
                    text: "Search Filters" 
                    color: 1, 1, 1, 1
                    spacing: "40dp"

                
                MDSlider:
                    min: 0
                    max: 25
                    step: 5
                    hint: False
                    thumb_color: 0, 0, 0, 0
                    thumb_color_down: 1, 1, 1, 1

                BoxLayout:
                    size_hint_x: 0.6
                   

                    MDLabel:
                        text: "0m" 
                        color: 1, 1, 1, 1
                        

                    MDLabel:
                        text: "5m" 
                        color: 1, 1, 1, 1

                    MDLabel:
                        text: "10m" 
                        color: 1, 1, 1, 1

                    MDLabel:
                        text: "15m" 
                        color: 1, 1, 1, 1

                    MDLabel:
                        text: "20m" 
                        color: 1, 1, 1, 1

                    MDLabel:
                        text: "25m+" 
                        color: 1, 1, 1, 1
                        pos_hint: {"center_x": .5, "center_y": .4}

                ItemBackdropBackLayerOfSecondScreen:
                    text: "Distance"

            

                
                        
                


                ItemBackdropBackLayerOfSecondScreen:
                    text: "Open now"
                ItemBackdropBackLayerOfSecondScreen:
                    text: "Top Rated"
                ItemBackdropBackLayerOfSecondScreen:
                    text: "Visited"
                ItemBackdropBackLayerOfSecondScreen:
                    text: "Not Visited"

                MDSeparator:

                Widget:
                    size_hint_y: None
                    height: "15dp"

                MDLabel:
                    text: "Nearest GPs"
                    color: 1, 1, 1, 1

                ItemBackdropBackLayer:
                    icon: "hospital-marker"
                    text: "Gratelake Walk In"
                ItemBackdropBackLayer:
                    icon: "hospital-marker"
                    text: "Choaktale GP Clinic"
                ItemBackdropBackLayer:
                    icon: "hospital-marker"
                    text: "Cornbrook Medical Practice"
                ItemBackdropBackLayer:
                    icon: "hospital-marker"
                    text: "The Whitsworth Practice"




               
                    


           
<HomeScreen>:

    NavigationLayout:

        ScreenManager:
            id: screen_manager
            Screen:
                name: "home"
                FloatLayout:
                    canvas:
                        Color:
                            rgba: 0, .7, 1, 1
                        RoundedRectangle:
                            size : self.size
                            pos : self.pos
                        Color:
                            rgba : (1, 1, 1, 1)
                        RoundedRectangle:
                            size : self.size[0], self.size[1] - 0.45*self.size[1]
                    Image:
                        source: 'MyCare1.png'
                        size_hint: (0.9, 0.8)
                        pos_hint : {'center_x' : 0.25, 'center_y' : 0.72}
                    MDLabel:
                        text : 'Welcome Daniel'
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1, 1)
                        font_style : 'H6'
                        pos_hint : {'x' : 0.6, 'center_y' : 0.855}
                        size_hint: (0.55, None)
                    

                        
                    
                    # first button
                    
                    LifestyleScreenElevationButton:
                        pos_hint : {'center_x' : 0.25, 'center_y' : 0.515}
                        on_press: root.callback()
                    Image:
                        source: 'user.png'
                        size_hint: (0.18, 0.18)
                        pos_hint: {'center_x' : 0.25, 'center_y' : 0.54}
                    MDLabel:
                        text : 'Profile'
                        font_size: '8sp'
                        size_hint: (0.22, None)
                        pos_hint: {'x' : 0.172, 'center_y' : 0.46}
                    
                    # Second button
                    
                    LifestyleScreenElevationButton:
                        pos_hint : {'center_x' : 0.75, 'center_y' : 0.515}
                        on_press: root.callback1()
                    Image:
                        source: 'email.png'
                        size_hint: (0.2, 0.2)
                        pos_hint: {'center_x' : 0.75, 'center_y' : 0.54}
                    MDLabel:
                        text : 'Messages'
                        font_size: '8sp'
                        size_hint: (0.22, None)
                        pos_hint: {'x' : 0.69, 'center_y' : 0.46}
                    
                    # Third button
                    
                    LifestyleScreenElevationButton:
                        pos_hint : {'center_x' : 0.25, 'center_y' : 0.24}
                        on_press: root.callback2()
                        
                    Image:
                        source: 'location.png'
                        size_hint: (0.2, 0.2)
                        pos_hint: {'center_x' : 0.25, 'center_y' : 0.28}
                    MDLabel:
                        text : 'Map'
                        font_size: '8sp'
                        size_hint: (0.22, None)
                        pos_hint: {'x' : 0.18, 'center_y' : 0.20}
                    
                    # Fourth button
                    
                    LifestyleScreenElevationButton:
                        pos_hint : {'center_x' : 0.75, 'center_y' : 0.24}
                        on_press: root.callback3()
                    Image:
                        source: 'settings.png'
                        size_hint: (0.2, 0.2)
                        pos_hint: {'center_x' : 0.75, 'center_y' : 0.272}
                    MDLabel:
                        text : 'Settings'
                        font_size: '8sp'
                        size_hint: (0.26, None)
                        pos_hint: {'x' : 0.72, 'center_y' : 0.20}


                    LifestyleScreenElevationButton:
                        pos_hint : {'center_x' : 0.5, 'center_y' : 0.08}
                        on_press: root.callback4()
                        
                          
                    Image:
                        source: 'exit.png'
                        size_hint: (0.2, 0.2)
                        pos_hint: {'center_x' : 0.52, 'center_y' : 0.11}
                    MDLabel:
                        text : 'Sign out'
                        font_size: '8sp'
                        size_hint: (0.26, None)
                        pos_hint: {'x' : 0.72, 'center_y' : 0.20}
                        
            
                FloatLayout:

                    MDFloatingActionButtonSpeedDial:
                        data: app.data
                        rotation_root_button: True
                        callback: app.callback                          

                          
 

                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'top'

                    MDToolbar:
                        title: "Home"
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        right_action_items: [["magnify", lambda x: app.callback6()],["calendar", lambda x: app.callback5()]]

           
 

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

       

""")    
                      

class ProfileScreen(Screen):
    pass 

class MessageScreen(Screen):


    def demo(self):
        print(self.screen.ids.toolbar.right_action_items[1])
    
    def change_screen(self, screen_name, curr = None, title = None):
        self.root.ids.screen_manager.current = screen_name
        if curr is not None:
            self.root.ids.screen_manager.transition.direction = 'right'
        else:
            self.root.ids.screen_manager.transition.direction = 'left'
        if title is not None:
            self.set_title(title)

    def set_title(self, title):
        self.root.ids.toolbar_chat_screen.title = title



class NotificationsScreen(Screen):

    def __init__(self, **kwargs):
        super(NotificationsScreen, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        if key is 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if self.manager.current != 'profile':
            self.manager.transition.direction = 'left'
            self.manager.current = self.sm.previous()

    def on_start(self):
        for i in range(10):
            self.root.ids.box.add_widget(
                MDExpansionPanel(
                    icon=f"{images_path}kivymd_logo.png",
                    content=Content1(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Doctor Singh",
                        secondary_text="Subject:",
                        tertiary_text="Message",
                    )
                )
            )
    

class LifestyleScreen(Screen):
    pass 

class AppointmentScreen(Screen):

    def __init__(self, **kwargs):
        super(AppointmentScreen, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key is 27:
            self.set_previous_screen()
            return True
    def set_previous_screen(self):
        if self.manager.current != 'home':
            self.manager.transition.direction = 'left'
            self.manager.current = self.sm.previous()

class MapScreen(Screen):
    pass 

class NewsScreen(Screen):
    pass 

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)


    def _key_handler(self, instance, key, *args):
        if key is 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if self.manager.current != 'home':
            self.manager.transition.direction = 'left'
            self.manager.current = self.manager.previous()


class WidgetsScreen(Screen):
    pass 

class LinkScreen(Screen):
    pass 

class Tab(FloatLayout, MDTabsBase):
	pass


class ItemBackdropBackLayer(ThemableBehavior, BoxLayout):
    icon = StringProperty("android")
    text = StringProperty()
    selected_item = BooleanProperty(False)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            for item in self.parent.children:
                if item.selected_item:
                    item.selected_item = False
            self.selected_item = True
        return super().on_touch_down(touch)


class RectangularElevationButton(RectangularElevationBehavior,
                                MDFillRoundFlatIconButton):
    md_bg_color = [0, 0, 1, 1]

class LifestyleScreenElevationButton(RectangularElevationBehavior,
                                MDFillRoundFlatButton):
    pass

class RectangularElevationListItem(RectangularElevationBehavior,
                                    BackgroundColorBehavior,
                                    TwoLineAvatarIconListItem):
    md_bg_color = [1, 1, 1, 1]     


class ContentNavigationDrawer(BoxLayout, EventDispatcher):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    



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

    
        
class Search(Screen):

    def set_list(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''
        
        def add_item(self):
            self.ids.search_results_list.data = []
            len(result['items'])
            for item in result['items']:
                print(item['title'], item['link'])

    def search_engine(self):
        search_template = "https://www.nhs.uk/" 
        search_url = search_template.format(self.add_item)
        request = UrlRequest(search_url, self.set_list)

        
    def found_search(self, request, data): 
        data = json.loads(data.decode()) if not isinstance(data, dict) else data 
        search = ["{] ({})".format(d['name'], d['sys']['nhs'])
            for d in data['list']] 
        self.search_results.item_strings = search
        self.srarch_results.adapter.data.clear()
        self.search_results.adapter.data.extend(search)
        self.search_results._trigger_reset_populate()


class SearchPopupMenu(MDDialog):
    title = 'Search by Address'
    text_button_ok = 'Search'

    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback


    def open(self):
        super().open()
        Clock.schedule_once(self.set_field_focus, 0.5)

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        with open('app_id.txt', 'r') as f:
            app_id = f.read()
        with open('app_code.txt', 'r') as f:
            app_code = f.read()
        address = parse.quote(address)
        url = "https://geocoder.api.here.com/6.2/geocode.json?searchtext=%s&app_id=%s&app_code=%s"%(address, app_id, app_code)
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where())

    def success(self, urlrequest, result):
        print("Success")
        latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude)

    def error(self, urlrequest, result):
        print("error")
        print(result)

    def failure(self, urlrequest, result):
        print("failure")
        print(result)
    

class LocationPopupMenu(MDDialog):
    def __init__(self, market_data):
        super().__init__()

        # Set all of the fields of market data
        headers = "FMID,MarketName,Website,Facebook,Twitter,Youtube,OtherMedia,street,city,County,State,zip,Season1Date,Season1Time,Season2Date,Season2Time,Season3Date,Season3Time,Season4Date,Season4Time,x,y,Location,Credit,WIC,WICcash,SFMNP,SNAP,Organic,Bakedgoods,Cheese,Crafts,Flowers,Eggs,Seafood,Herbs,Vegetables,Honey,Jams,Maple,Meat,Nursery,Nuts,Plants,Poultry,Prepared,Soap,Trees,Wine,Coffee,Beans,Fruits,Grains,Juices,Mushrooms,PetFood,Tofu,WildHarvested,updateTime"
        headers = headers.split(',')

        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = market_data[i]
            setattr(self, attribute_name, attribute_value)


class MarketMarker(MapMarkerPopup):
    source = "marker.png"
    market_data = ["gp.db"]
 
    def on_release(self):
        # Open up the LocationPopupMenu
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [.8, .9]
        menu.open()


class FarmersMapView(MapView):
    getting_markets_timer = None
    market_names = []

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.getting_markets_timer.cancel()
        except:
            pass

        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self, *args):
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * FROM markets WHERE x > %s AND x < %s AND y > %s AND y < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()
        print(markets)
        for market in markets:
            name = market[1]
            if name in self.market_names:
                continue
            else:
                self.add_market(market)

    def add_market(self, market):
        # Create the MarketMarker
        lat, lon = market[21], market[20]
        marker = MarketMarker(lat=lat, lon=lon)
        marker.market_data = market
        # Add the MarketMarker to the map
        self.add_widget(marker)

        # Keep track of the marker's name
        name = market[1]
        self.market_names.append(name)




class Content(BoxLayout):
    pass



class Content1(BoxLayout):
    '''Custom content.'''

class RootWidget(AnchorLayout):
    lat = NumericProperty(51.509865)
    lon = NumericProperty(-0.118092)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.anchor_x = 'right'
        self.anchor_y = 'top'
        mapview = MapView(zoom=11, lat=self.lat, lon=self.lon)
        self.add_widget(mapview)
        toolbar = MDToolbar(
            title="Map",
            background_palette="Primary",
            background_hue="500",
            elevation=10,
        )
        toolbar.left_action_items = [["arrow-left", lambda x: x]]
        toolbar.right_action_items = [["magnify", lambda x: self.show_confirmation_dialog()]]
        self.add_widget(toolbar)


    def show_confirmation_dialog(self):  
        search_menu = MDDialog(
            title="Address:",
            type="custom",
            content_cls=Content1(),
            buttons=[
                MDRaisedButton(
                    text="CANCEL"
                ),
                MDRaisedButton(
                    text="OK"
                ),
            ],
        )
        self.add_widget(search_menu)

    def centerOnUser(self):
        pass

class GPScreenElevationButton(RectangularElevationBehavior,
                                MDFillRoundFlatButton):
    pass
        


class ListItem(OneLineAvatarIconListItem):
    icon = StringProperty("android")
    text = StringProperty()
    selected_item = BooleanProperty(False)
   
    

class HomeScreen(Screen, MDApp):
    set_date = ObjectProperty()
    get_time = ObjectProperty()
    data = {
        "calendar": "Appointment",
        "robot": "Chatbot",
        "heart-pulse": "Lifestyle",
    }

    def callback(self):
        self.manager.current = 'profile'

    def callback1(self):
        self.manager.current = 'messages'

    def callback2(self):
        self.manager.current = 'map'

    def callback3(self):
        self.manager.current = 'settings'

    def callback4(self):
        self.manager.current = 'logout'

    def callback5(self):
        self.manager.current = 'appointment'

    def callback6(self):
        self.manager.current = 'search'
    
    def callback7(self):
        self.manager.current = 'notifications'

    
    def callback8(self):
        self.manager.current = 'widgets'

    def callback9(self):
        self.manager.current = 'link'
    
    def callback10(self):
        self.manager.current = 'news'

    def callback11(self):
        self.manager.current = 'discovery'

    def callback12(self):
        self.manager.current = 'home'
   
    
    def on_start(self):
        for i in range(10):
            self.root.ids.box.add_widget(
                MDExpansionPanel(
                    icon=f"{images_path}kivymd_logo.png",
                    content=Content1(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Doctor Singh",
                        secondary_text="Subject:",
                        tertiary_text="Message",
                    )
                )
            )
    
   

    def build(self):
        self.root = AppointmentScreen()

    
    

    def option_callback(self, text_of_the_option):
        print(text_of_the_option)
    
        
    def set_date(self, date):
        def set_date(interval):
            self.root.ids.date_picker_label.field.text = str(date)
        


    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.set_date)
        date_dialog.open()
        
    def get_time(self, the_time):
        self.get_time = the_time
        self.root.ids.time_picker_label.text = str(the_time)


    def show_time_picker(self):

        time_dialog = MDTimePicker()
        time_dialog.open()

 

    

            
# Names of standard color themes.
        
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(ProfileScreen(name='discovery'))
sm.add_widget(MessageScreen(name='messages'))
sm.add_widget(NotificationsScreen(name='notifications'))
sm.add_widget(LifestyleScreen(name='lifestyle'))
sm.add_widget(AppointmentScreen(name='appointment'))
sm.add_widget(MapScreen(name='map'))
sm.add_widget(NewsScreen(name='news'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(WidgetsScreen(name='widgets'))
sm.add_widget(LinkScreen(name='link'))
sm.add_widget(Search(name='search'))

class TestApp(MDApp):

    

    def build(self):
        return sm

    


if __name__ == '__main__':
    TestApp().run()