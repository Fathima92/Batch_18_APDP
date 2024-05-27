class IButton(object):
   html = ""
   def get_html(self):
      return self.html

class Image(IButton):
   html = "<img></img>"

class Input(IButton):
   html = "<input></input>"

class Flash(IButton):
   html = "<obj></obj>"

class ButtonFactory():
   def create_button(self, typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]()

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
   print (button_obj.create_button(b).get_html())
