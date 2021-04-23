from kivy.properties import ColorProperty, StringProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


class DecentraRootScreen(MDScreen):
    pass


class DecentraListItem(ThemableBehavior, RectangularRippleBehavior, MDBoxLayout):
    text = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()
    bar_color = ColorProperty((1, 0, 0, 1))


class DecentraSeeAllButton(RectangularRippleBehavior, MDBoxLayout):
    pass