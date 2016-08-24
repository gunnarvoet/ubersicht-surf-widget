# This is a simple example Widget, written in CoffeeScript, to get you started
# with Übersicht. For the full documentation please visit:
#
# https://github.com/felixhageloh/uebersicht
#
# You can modify this widget as you see fit, or simply delete this file to
# remove it.

# this is the shell command that gets executed every time this widget refreshes
command: "/opt/local/bin/python surf.widget/surf_plot.py"

# the refresh frequency in milliseconds
refreshFrequency: 1800000 # refresh every half hour

# render gets called after the shell command has executed. The command's output
# is passed in as a string. Whatever it returns will get rendered as HTML.
render: (output) -> """
  <p>
  <IMG SRC="surf.widget/surf.png" ALT="surf">
  </p>
"""

# the CSS style for this widget, written using Stylus
# (http://learnboost.github.io/stylus/)
style: """
  font-family: Helvetica Neue
  font-weight: 300
  left: 20%
  top: 30%

  h1
    font-size: 20px
    font-weight: 300
    margin: 16px 0 8px

  strong
    background: #ad7a7c
    color: #fff
    display: block
    font-size: 16px
    font-style: italic
    font-weight: 200
    margin: 12px -20px
    padding: 8px 20px

  em
    font-weight: 400
    font-style: normal
"""
