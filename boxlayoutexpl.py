from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutExplGUI(BoxLayout):
	def setToLabel(self, value):
		self.ids.label_1.text = 'Button {} pressed'.format(value)
	
class BoxLayoutExplApp(App):
	def build(self):
		return BoxLayoutExplGUI()
		
if __name__ == '__main__':
	BoxLayoutExplApp().run()