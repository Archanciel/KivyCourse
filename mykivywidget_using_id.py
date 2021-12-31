from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty

class MyGridLayout(GridLayout):
	labelTxt = StringProperty('0')
	clickDisabled = BooleanProperty(True)
	#switchActive = BooleanProperty(False)
	#sliderLabelTxt = StringProperty('0')
	#sliderDisabled = BooleanProperty(True)
	
	def __init__(self, **kvarg):
		super().__init__(**kvarg)
		
		self.clickNb = 0
		self.clickNumberActive = False

	def handleClick(self):
		self.clickNb += 1
		self.labelTxt = str(self.clickNb) 
		
	def handleToggle(self, widget):
		if widget.state == 'normal':
			widget.text = 'Off'
			self.clickDisabled = True
		else:	
			widget.text = 'On'
			self.clickDisabled = False

#	def handleSwitch(self, widget):
#		self.sliderDisabled = not widget.active
			
#	def handleSlider(self, widget):
#		self.sliderLabelTxt = str(int(widget.value))
	
class MyKivyWidget_using_idApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	MyKivyWidget_using_idApp().run()