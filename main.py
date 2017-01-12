import gi
from pwd_brut import *
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def user_file(self, button):
    	text_a =  target_in.get_text()
    	print(text_a)
    	# Main()

builder = Gtk.Builder()
builder.add_from_file("/home/korolr/Desktop/python/gui_test/gui.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()