#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication, QWidget,QStatusBar
from PyQt5 import QtGui
from PyQt5.QtCore import QSize,pyqtSlot,Qt, QPropertyAnimation,QRect,QTimer,pyqtSignal

class QAnimatedstateBar(QstateBar):

	def __init__(self):
		super().__init__()
		self.dbg=True
		self.height_=0
		self.anim=QPropertyAnimation(self, b"geometry")
		self.hide()
		self.timer=QTimer()
		self.timer.setSingleShot(True)
		self.animationInterval=1000
		self.showInterval=3000
		self.msg=''
		self.css={}
		self.css['default']="QstateBar{background-color:qlineargradient(x1:0 y1:0,x2:0 y2:1,stop:0 rgba(255,0,0,1), stop:1 rgba(255,0,0,0.6));color:white;\
						text-decoration:underline;font-weight:bold;border:1px;border-color:black;border-style:solid;border-radius:5px;}"
	#def __init__

	def setText(self,msg):
		self.msg="%s"%msg
	#def setText

	def setAnimation(self,animation):
		try:
			self.anim=QPropertyAnimation(self, b"%s"%animation)
		except Exception as e:
			print(e)
	#def setAnimation

	def setAnimationInterval(self,miliseconds):
		self.animationInterval=miliseconds
	#def setAnimationInterval

	def setShowInterval(self,miliseconds):
		self.showInterval=miliseconds
	#def setShowInterval

	def setStateCss(self,state,css):
		self.css[state]="text-decoration:underline;font-weight:bold;border:1px;border-color:black;border-style:solid;border-radius:5px;"+css
	#def setStateCss

	def setCss(self,css):
		self.css['default']="text-decoration:underline;font-weight:bold;border:1px;border-color:black;border-style:solid;border-radius:5px;"+css
	#def setCss

	def show(self,state=None):
		def hide_message():
			self.anim.setDuration(self.animationInterval)
			self.anim.setStartValue(QRect(0,0,width,self.height_))
			self.anim.setEndValue(QRect(0,0,width,0))
			self.anim.start()
			self.timer.singleShot(self.animationInterval, lambda:self.hide())
		if state:
				if state in self.css.keys():
					self.setStyleSheet("""%s"""%self.css[state])
				else:
					self._debug("No css found for %s"%state)
					self.setStyleSheet("""%s"""%self.css['default'])
		else:
				self.setStyleSheet("""%s"""%self.css['default'])
		self.raise_()
		self.showMessage("%s"%self.msg)
		self.anim.setDuration(self.animationInterval)
		self.anim.setLoopCount(1)
		height=(self.height()/10)-10
		if self.height_<height:
			self.height_=height
		super(QAnimatedstateBar,self).show()
		width=self.parentWidget().width()
		self.anim.setStartValue(QRect(0,0,width,0))
		self.anim.setEndValue(QRect(0,0,width,self.height_))
		self.anim.start()
		self.timer.singleShot(self.showInterval, lambda:hide_message())
	#def show(self,state=None):
