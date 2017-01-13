import gi
from pwd_brut import *
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def __init__(self):
    	pass

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def user_file(self, button):
    	
    	Main()

    def target_in(self, widget, event):
    	text_a =  self.get_text()
    	print(text_a)
    	# Main()

builder = Gtk.Builder()
builder.add_from_file("/home/korolr/Desktop/python/gui_test/gui.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()
target = builder.get_object("target_in").get_text()

xPathLogin = builder.get_object("login_in_1").get_text()

xPathPassword = builder.get_object("pass_in").get_text()

xPathAcceptButton = builder.get_object("login_in").get_text()

xPathSuccessAuth = builder.get_object("auth_in").get_text()

xPathFailAuth = builder.get_object("login_in").get_text()

selBrowserString = '*chrome'

selFFProfile = 'ff_profile'


usersFile = 'dict/users.txt'

passwordsFile = 'dict/pwd.txt'

resultFile = 'result.txt'

brutThreads = 1

rumpUpPeriod = brutThreads * 5

timeout = 1

randomCredentials = False


randomGeneratorParameter = [100, 8, 1, 1, 1, 0, 0, 0]


Gtk.main()