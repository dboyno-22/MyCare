from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty,ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem, MDList,\
    OneLineAvatarIconListItem
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivy.animation import Animation
from kivy.core.window import Window



# Your layouts.
Builder.load_string("""
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget






<ItemBackdropFrontLayer@TwoLineAvatarListItem>
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


<ItemBackdropBackLayerOfSecondScreen@BoxLayout>
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

   



<ItemRoundBackdropBackLayerOfSecondScreen@BoxLayout>
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




<MyBackdropBackLayer@ScreenManager>
    transition: NoTransition()

    
   
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



<ExampleBackdrop>

    MDBackdrop:
        id: backdrop
        on_open: print("on_open")
        on_close: print("on_close")
        left_action_items: [["menu", lambda x: self.open()]]
        header_text: "Menu:"
        right_action_items: [["arrow-left", lambda x: root.callback1()]]

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                backlayer: backlayer
               


"""
)




    

class ExampleBackdrop(Screen):
    
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

        


class MainApp(MDApp):
    set_date = ObjectProperty()
    get_time = ObjectProperty()
    def __init__(self, **kwargs):
        self.title = "Appointment"
        super().__init__(**kwargs)

    def build(self):
        self.root = ExampleBackdrop()

    
    

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

if __name__ == "__main__":
    MainApp().run()
