
from easygui import *
while 1:
  image   = "signlang.png"
  msg="HEARING IMPAIRMENT ASSISTANT\nDesigned for the wellfare of deaf community."
  choices = ["Give Voice Input","Exit"]
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()