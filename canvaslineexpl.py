from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.vertex_instructions import Line, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
Builder.load_file('canvas_line_expl.kv')

class CanvasLineExpl1(GridLayout):
	def __init__(self, **kvargs):
		super().__init__(**kvargs)
		self.directedHorizonzalMoveDp = dp(40)

		pointsLst = []
		startX = 0
		startY = 0
		lineLength = 50
		dir = 2
		
		for i in range(10):
			endX = startX + lineLength + 10 * i * dir
			endY = startY + lineLength - 20 * i * dir
			pointsLst.extend([startX, startY, endX, endY])
			startX = endX
			startY = endY
			dir = - dir
			if i > 6:
				dir = dir * 1.5
		with self.canvas:
			Line(points=tuple(pointsLst), width=2)
			self.radius = dp(100)
			self.ellipse = Ellipse(pos=(self.directedHorizonzalMoveDp, dp(100)), size=(self.radius, self.radius))
	
	def buttonMovePressed(self):
		circleX, circleY = self.ellipse.pos

		directedMoveDpReduction = 0
		
		rightX = circleX + self.radius
		
		if rightX + self.directedHorizonzalMoveDp >= self.width:
			# near right side
			directedMoveDpReduction = self.width - (rightX + self.directedHorizonzalMoveDp)

		if circleX + self.directedHorizonzalMoveDp <= 0:
			# near left side
			directedMoveDpReduction = - (circleX + self.directedHorizonzalMoveDp)
		
		# moving circle
		
		circleX = circleX + self.directedHorizonzalMoveDp + directedMoveDpReduction
		self.ellipse.pos = (circleX, circleY)
		rightX = circleX + self.radius
		
		if rightX == self.width:
			# circle at right side
			self.directedHorizonzalMoveDp = - self.directedHorizonzalMoveDp
		elif circleX == 0:
			# circle at left side
			self.directedHorizonzalMoveDp = - self.directedHorizonzalMoveDp


class CanvasLineExplApp(App):
	def build(self):
		return CanvasLineExpl1()
		
if __name__ == '__main__':
	CanvasLineExplApp().run()