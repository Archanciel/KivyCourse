from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color

Builder.load_file('canvas_line_expl.kv')

class CanvasLineExpl1(GridLayout):
	def __init__(self, **kvargs):
		super().__init__(**kvargs)
		with self.canvas:
			Line(points=(0, 0, 150, 300, 150, 300, 800, 200), width=2)
	
class CanvasLineExplApp(App):
	def build(self):
		return CanvasLineExpl1()
		
if __name__ == '__main__':
	CanvasLineExplApp().run()