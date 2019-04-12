# QAnimatedStatusBar

QAnimatedStatusBar is a QT widget for python3 that shows an animated status bar with a message.

## setText(string)

Sets the text to show

## setCss(css_style)

Sets the default css style for the widget

## setStateCss(state,css_style)

Sets the css for that state

## setAnimation(QAnimation)

Sets the animations for the StatusBar

## setAnimationInterval(miliseconds)

Sets the interval for the show and hide animations

## setShowInterval(miliseconds)

Sets the interval in wich the statusBar will be showed

## show(state='default')

Shows the statusbar setting the css for the state. If there's no state then loads the default css. 
