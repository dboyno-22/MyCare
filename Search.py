from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout


import pprint
import requests
import json

api_key = "AIzaSyDUQA-jlRsGYRfYRgDDX5htX31anRglppg"

from apiclient.discovery import build

resource = build("customsearch", 'v1', developerKey=api_key).cse()
result = resource.list(q='python', cx='000650397041980504370:ebzcc2p4fv8').execute()
result['items'][6]

len(result['items'])
for item in result['items']:
    print(item['title'], item['link'])


Builder.load_string(
    '''
#:import images_path kivymd.images_path


<CustomOneLineListItem>:




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
            left_action_items: [["arrow-left", lambda x: x]]
            right_action_items: [["dots-vertical", lambda x: x],["clock", lambda x: x]]
                    

            

  

'''
)





class ContentNavigationDrawer(BoxLayout):
    pass

class CustomOneLineListItem(OneLineListItem):
    item = StringProperty()
    search_results = ObjectProperty()

class Search(Screen,BoxLayout):
   

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




    



class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Search()
        
   

    


    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list()


MainApp().run()