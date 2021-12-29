from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from anchorlayoutexpl import AnchorLayoutExplGUI

class GridLayoutExplGUI(GridLayout):
	pass
	
class BoxLayoutExplGUI(BoxLayout):
	def setToLabel(self, value):
		self.ids.label_1.text = 'Button {} pressed'.format(value)
	
class GridLayoutExplApp(App):
	def build(self):
		return GridLayoutExplGUI()
		
if __name__ == '__main__':
	GridLayoutExplApp().run()