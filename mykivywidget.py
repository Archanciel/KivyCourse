from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class MyGridLayout(GridLayout):
	labelTxt = StringProperty('0')
	
	def __init__(self, **kvarg):
		super().__init__(**kvarg)
		
		self.clickNb = 0

	def handleClick(self):
		self.clickNb += 1
		self.labelTxt = str(self.clickNb) 	
	
class MyKivyWidgetApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	MyKivyWidgetApp().run()