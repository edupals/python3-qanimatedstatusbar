#!/usr/bin/env python3
from PySide2.QtWidgets import QStatusBar,QPushButton,QLabel
from PySide2 import QtGui
from PySide2.QtCore import Qt, QPropertyAnimation,QRect,QTimer

class QAnimatedStatusBar(QStatusBar):

	def __init__(self):
		super().__init__()
		self.dbg=False
		self.height_=0
		self.anim=QPropertyAnimation(self, b"geometry")
		self.hide()
		self.timer=QTimer()
		self.timer.setSingleShot(True)
		self.btn_close=QPushButton("X")
		self.insertPermanentWidget(0,self.btn_close)
		self.btn_close.clicked.connect(self._hide_message)
		self.btn_close.setAutoDefault(False)
		self.btn_close.setDefault(False)
		self.animationInterval=1000
		self.label=QLabel("")
		self.label.setWordWrap(True)
		self.label.setStyleSheet("background-color:transparent;margin:0px;border:0px;text-decoration:none")
		self.addWidget(self.label)
		self.showInterval=3000
		self.msg=''
		self.css={}
		self.css['default']="background-color:qlineargradient(x1:0 y1:0,x2:0 y2:1,stop:0 rgba(25,25,25,1), stop:1 rgba(25,25,25,0.6));color:white;\
						text-decoration:underline;font-weight:bold;border:1px;border-color:black;border-style:solid;"
	#def __init__

	def _debug(self,msg):
		print("QAnimatedStatusBar: %s"%msg)
	#def _debug

	def setText(self,msg):
			#self.msg="%s"%msg.replace("\n","<br>")
		self.label.setText("%s"%msg.replace("\n","<br>"))
	#def setText

	def setAnimation(self,animation):
		try:
			self.anim=QPropertyAnimation(self, b"%s"%animation)
		except Exception as e:
			self._debug(e)
	#def setAnimation

	def setAnimationInterval(self,miliseconds):
		self.animationInterval=miliseconds
	#def setAnimationInterval

	def setShowInterval(self,miliseconds):
		self.showInterval=miliseconds
	#def setShowInterval

	def setStateCss(self,state,css):
		self.css[state]="QStatusBar{text-decoration:underline;font-weight:bold;border:1px;border-color:black;border-style:solid;%s}"%css
	#def setStateCss

	def setCss(self,css):
		self.css['default']="QStatusBar{text-decoration:underline;font-weight:bold;border:1px;border-color:black;border-style:solid;%s}"%css
	#def setCss

	def show(self,state=None):
		self._debug("Show state %s"%state)
		if state:
				if state in self.css.keys():
					self.setStyleSheet("""%s"""%self.css[state])
				else:
					self._debug("No css found for %s"%state)
					self.setStyleSheet("""%s"""%self.css['default'])
		else:
				self.setStyleSheet("""%s"""%self.css['default'])
		self.raise_()
		#self.showMessage("%s"%self.msg)
		self.showMessage("")
		self.anim.setDuration(self.animationInterval)
		self.anim.setLoopCount(1)
		self.btn_close.height=16
		super(QAnimatedStatusBar,self).show()
		width_=self.parentWidget().width()
		#360px should be good enough....
		width=360
		self.anim.setDuration(1)
		self.anim.setStartValue(QRect(width_-width,0,width,0))
		self.anim.setEndValue(QRect(width_-width,0,width,self.label.height()+6))
		self.anim.start()
		if state==None or state=='':
			self._debug("Hide state %s"%state)
			height=(self.height()/10)-10
			self.height_=height
			self.timer.singleShot(self.showInterval, lambda:self._hide_message())
	#def show(self,state=None):
	

	def _hide_message(self):
		self._debug("Hiding statusbar")
		width_=self.parentWidget().width()
		width=360
		self.anim.setDuration(self.animationInterval)
		self.anim.setStartValue(QRect(width_-width,0,width,self.height_))
		self.anim.setEndValue(QRect(width_-width,0,width,0))
		self.anim.start()
		self.timer.singleShot(self.animationInterval, lambda:self.hide())
