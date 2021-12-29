from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

class AnchorLayoutExplGUI(GridLayout):
	label1 = ObjectProperty()
	label2 = ObjectProperty()
	label3 = ObjectProperty()

	label4 = ObjectProperty()
	label5 = ObjectProperty()
	label6 = ObjectProperty()

	label7 = ObjectProperty()
	label8 = ObjectProperty()
	label9 = ObjectProperty()
	
	def setToLabel(self, value, labelId):
		if '1' in labelId:
			self.label1.text = 'Button {}-1'.format(value)
		elif '2' in labelId:
			self.label2.text = 'Button {}-2'.format(value)
		elif '3' in labelId:
			self.label3.text = 'Button {}-3'.format(value)
		elif '4' in labelId:
			self.label4.text = 'Button {}-4'.format(value)
		elif '5' in labelId:
			self.label5.text = 'Button {}-5'.format(value)
		elif '6' in labelId:
			self.label6.text = 'Button {}-6'.format(value)
		elif '7' in labelId:
			self.label7.text = 'Button {}-7'.format(value)
		elif '8' in labelId:
			self.label8.text = 'Button {}-8'.format(value)
		elif '9' in labelId:
			self.label9.text = 'Button {}-9'.format(value)
	
class AnchorLayoutExplApp(App):
	def build(self):
		return AnchorLayoutExplGUI()
		
if __name__ == '__main__':
	AnchorLayoutExplApp().run()