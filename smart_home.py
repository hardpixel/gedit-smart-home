import gi

gi.require_version('Gedit', '3.0')

from gi.repository import GObject, Gedit

class SmartHomeViewActivatable(GObject.Object, Gedit.ViewActivatable):

	view = GObject.property(type=Gedit.View)

	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		self.view.set_smart_home_end(True)

	def do_deactivate(self):
		self.view.set_smart_home_end(False)
