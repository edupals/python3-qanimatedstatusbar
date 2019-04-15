# QAnimatedStatusBar

QAnimatedStatusBar is a QT widget for python3 that shows an animated status bar with a message.

### API  

###### setText(string)

Sets the text to show

###### setCss(css_style)

Sets the default css style for the widget

###### setStateCss(state,css_style)

Sets the css for that state

###### setAnimation(QAnimation)

Sets the animations for the StatusBar

###### setAnimationInterval(miliseconds)

Sets the interval for the show and hide animations

###### setShowInterval(miliseconds)

Sets the interval in wich the statusBar will be showed

###### show(state='default')

Shows the statusbar setting the css for the state. If there's no state then loads the default css. 


### Examples  
```python  

#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from edupals.ui import QAnimatedStatusBar

class animatedStatusExample(QWidget):

    def __init__(self):
        super().__init__()
        box=QGridLayout()
        btn=QPushButton("click me!!")
        self.statusBar=QAnimatedStatusBar.QAnimatedStatusBar()
        self.statusBar.setText("Example")
        box.addWidget(self.statusBar,0,0,1,1)
        box.addWidget(btn,0,0,1,1)
        btn.clicked.connect(self._begin_animation)
        self.setLayout(box)
        self.show()
    #def init

    def _begin_animation(self):
        self.statusBar.show()
    #def _begin_animation

app=QApplication([])                                                                                                                                                                         
animatedExample=animatedStatusExample()
app.exec_()
