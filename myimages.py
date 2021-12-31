from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyImages(GridLayout):
	pass

class MyImagesApp(App):
	def build(self):
		return MyImages()
		
if __name__ == '__main__':
	MyImagesApp().run()