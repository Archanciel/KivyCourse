from kivy.app import App
from kivy.uix.widget import Widget

class CanvasExpl1(Widget):
	pass
	
class CanvasExpl2(Widget):
	pass
	
class CanvasExplApp(App):
	def build(self):
		return CanvasExpl2()
		
if __name__ == '__main__':
	CanvasExplApp().run()