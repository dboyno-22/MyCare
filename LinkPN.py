from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty

from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.picker import MDDatePicker

KV = '''



Screen:

    NavigationLayout:

        ScreenManager:

            Screen:
                
                
                BoxLayout:
                    orientation: 'vertical'
      
                
                    MDToolbar:
                        title: "NHS LINK"
                        left_action_items: [["arrow-left", lambda x: x]]
                        right_action_items: [["dots-vertical", lambda x: x]]
                    
                    MDTabs:
                        id: android_tabs
                        

                        

                        Tab:
                            text: "Request NHS Number"
                            
                        
                            ScrollView:    
                                BoxLayout:
                                    orientation: "vertical"
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: dp(48)
                                    spacing: "10dp"
                        
                
                                    MDTextField:
                                        hint_text: "First Name"
                                        mode: "rectangle"
                                        required: True
                                        helper_text_mode: "on_error"
                                        

                                    MDTextField:
                                        hint_text: "Last Name"
                                        mode: "rectangle"
                                        required: True
                                        helper_text_mode: "on_error"

                                    MDTextField:
                                        id: date_picker_label
                                        hint_text: "Date of Birth"
                                        mode: "rectangle"
                                        size_hint_x: .8
                                        
                                    FloatLayout:
                                        MDRaisedButton:
                                            text: "Select Date of Birth"
                                            pos_hint: {"center_x": 0.95,'center_y': 2.5}
                                            opposite_colors: True
                                            on_release: app.show_date_picker()
                                            radius: [25, 0, 0, 0]
                                            
                                

                                    MDTextField:
                                        id: field
                                        hint_text: "Country/Region"
                                        mode: "rectangle"
                                        size_hint_x: .8
                                        on_focus: if self.focus: app.dropdown.open(root)

                                    
                                        
                                        

                                    MDTextField:
                                        hint_text: "Location"
                                        mode: "rectangle"
                                    
                                    MDTextField:
                                        hint_text: "City"
                                        mode: "rectangle"

                                    MDTextField:
                                        hint_text: "Address"
                                        mode: "rectangle"

                                    MDTextField:
                                        hint_text: "Gender"
                                        mode: "rectangle"
                                    
                                    MDTextField:
                                        hint_text: "Contact Number"
                                        mode: "rectangle"
                                        max_text_length: 11


                                    MDSeparator:

                                    MDTextFieldRound:
                                        hint_text: "Password"
                                        icon_right: "lock"
                                        normal_color: 0, 0, 0, 0
                                        color_active: 0, 0, 0, .6
                                        height: "300dp"
                                        
                                    
                                    MDTextFieldRound:
                                        hint_text: "Confirm Password"
                                        icon_right: "lock"
                                        normal_color: 0, 0, 0, 0
                                        color_active: 0, 0, 0, .6
                                        height: "300dp"
                        Tab:
                            text: "Link NHS Number"
                            
                            ScrollView:
                                
                                BoxLayout:
                                    orientation: "vertical"
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: dp(48)
                                    spacing: "10dp"
                        
                
                                    MDTextField:
                                        hint_text: "First Name"
                                        mode: "rectangle"
                                        required: True
                                        helper_text_mode: "on_error"
                                        

                                    MDTextField:
                                        hint_text: "Last Name"
                                        mode: "rectangle"
                                        required: True
                                        helper_text_mode: "on_error"

                                    MDTextField:
                                        id: date_picker_label
                                        hint_text: "Date of Birth"
                                        mode: "rectangle"
                                        size_hint_x: .8
                                        
                                    FloatLayout:
                                        MDRaisedButton:
                                            text: "Select Date of Birth"
                                            pos_hint: {"center_x": 0.95,'center_y': 2.5}
                                            opposite_colors: True
                                            on_release: app.show_date_picker()
                                            radius: [25, 0, 0, 0]
                                            
                                

                                    MDTextField:
                                        id: field
                                        hint_text: "Country/Region"
                                        mode: "rectangle"
                                        size_hint_x: .8
                                        on_focus: if self.focus: app.dropdown.open(root)

                                    
                                        
                                        

                                    MDTextField:
                                        hint_text: "Location"
                                        mode: "rectangle"
                                    
                                    MDTextField:
                                        hint_text: "City"
                                        mode: "rectangle"

                                    MDTextField:
                                        hint_text: "Address"
                                        mode: "rectangle"

                                    MDTextField:
                                        hint_text: "Gender"
                                        mode: "rectangle"
                                    
                                    MDTextField:
                                        hint_text: "Contact Number"
                                        mode: "rectangle"
                                        max_text_length: 11


                                    MDSeparator:

                                    MDTextFieldRound:
                                        hint_text: "Password"
                                        icon_right: "lock"
                                        normal_color: 0, 0, 0, 0
                                        color_active: 0, 0, 0, .6
                                        height: "300dp"
                                        
                                    
                                    MDTextFieldRound:
                                        hint_text: "Confirm Password"
                                        icon_right: "lock"
                                        normal_color: 0, 0, 0, 0
                                        color_active: 0, 0, 0, .6
                                        height: "300dp"
                                
                            


                    
'''
class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class ContentNavigationDrawer(BoxLayout):
    pass


class Link(MDApp):
    text = StringProperty()
    get_date = ObjectProperty()

    def build(self):
        return Builder.load_string(KV)

    def set_item(self, instance):
        def set_item(interval):
            self.menu.ids.field.text = instance.text
 

    def get_date(self, the_date):
        self.get_date = the_date
        self.root.ids.date_picker_label.text = str(the_date)

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
    
        instance_tab.ids.label.text = tab_text

Link().run()