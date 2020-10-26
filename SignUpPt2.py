from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ListProperty, ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineRightIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDTimePicker, MDDatePicker
from kivymd.uix.dropdownitem import MDDropDownItem


KV =  """
<Item>:
    height: dp(56)
    text: "A button with"
    secondary_text: "a dropdown"
    font_style: "H6"

    ListButtonDropdown:
        items: root.items
        
<TextFields@BoxLayout>:
    orientation: "vertical"

    MDToolbar:
        id: toolbar
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        background_palette: "Primary"
        elevation: 10
        left_action_items: [["arrow-left", lambda x: x]]
        
        
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
                on_focus: if self.focus: app.menu.open()

            
                
                

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
                password: True
                
            
            MDTextFieldRound:
                hint_text: "Confirm Password"
                icon_right: "lock"
                normal_color: 0, 0, 0, 0
                color_active: 0, 0, 0, .6
                height: "300dp"
                password: True


           
"""


class Item(OneLineRightIconListItem):
    items = ListProperty()


class ListButtonDropdown(IRightBodyTouch, MDDropDownItem):
    pass 

class MainApp(MDApp):
    get_date = ObjectProperty()
    dropdown = ObjectProperty()
    def __init__(self, **kwargs):
        self.title = "Sign Up - Personal Information"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)
        
    def on_start(self):
        menu_items = [{"text":"England, Scotland, Wales, Northern Ireland"}]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.field,
            items=menu_items,
            position="center",
            callback = self.set_item,
            width_mult=4,
        
        )
    

    def option_callback(self, text_of_the_option):
        print(text_of_the_option)

    def build(self):
        Builder.load_string(KV)
        self.root = Factory.TextFields()
        
    def set_item(self, instance):
        def set_item(interval):
            self.menu.ids.field.text = instance.text
 

    def get_date(self, instance, the_date):
        self.get_date = the_date
        self.root.ids.date_picker_label.text = str(the_date)

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

            
    
        

        
if __name__ == "__main__":
    MainApp().run()