from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty

from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
from kivymd.uix.list import OneLineAvatarIconListItem, MDList
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import Screen

KV = '''
<Content>
    adaptive_height: True

    TwoLineIconListItem:
        text: "(050)-123-45-67"
        secondary_text: "Mobile"

        IconLeftWidget:
            icon: 'phone'



Screen:

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
                        left_action_items: [["arrow-left", lambda x: nav_drawer.toggle_nav_drawer()]]
                        right_action_items: [["magnify", lambda x: Search.callback()],["clock", lambda x: app.callback_2()]]
                    

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
'''

class Content(BoxLayout):
    '''Custom content.'''

class ContentNavigationDrawer(BoxLayout):
    pass

class NavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

class Notification(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(10):
            self.root.ids.box.add_widget(
                MDExpansionPanel(
                    icon=f"{images_path}kivymd_logo.png",
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Doctor Singh",
                        secondary_text="Subject:",
                        tertiary_text="Message",
                    )
                )
            )



Notification().run()
