from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty

from kivymd.uix.list import OneLineAvatarIconListItem, MDList
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    RectangularElevationBehavior,
)
from kivymd.uix.button import MDFillRoundFlatButton, MDRaisedButton
from util import DATA
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDToolbar
from kivy.garden.mapview import MapView, MapMarker
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.garden.mapview import MapMarkerPopup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from urllib import parse
from kivy.network.urlrequest import UrlRequest
import certifi

  

from urllib import parse

import sqlite3
from kivy.clock import Clock
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd import app


KV = '''
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


Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                   
                    MDBottomNavigation:
                        panel_color: .2, .2, .2, 1

                    

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
                        left_action_items: [["arrow-left", lambda x: x]]
         
'''

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
            content_cls=Content(),
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

class Map(MDApp):
    data = DATA
    dialog = None
    connection = None
    cursor = None
    search_menu = SearchPopupMenu

   
    def change_screen(self, curr, ext = '.jpg'):
        pass

    def change_icon(self, name, reverse = False, rootOrigin = False):
        pass 

    def build(self):
        return Builder.load_string(KV)
         
        
    

    
    

Map().run()
