from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
	def __init__(self, **kvarg):
		super().__init__(**kvarg)

	
class MyKivyWidgetApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	MyKivyWidgetApp().run()