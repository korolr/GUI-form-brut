GUI-brut-form
===================

Brutforce web forms has never been so easy

----------

![enter image description here](http://im2.ezgif.com/tmp/ezgif.com-7253c0ed59.gif)
Documents
-------------

StackEdit stores your documents in your browser, which means all your documents are automatically saved locally and are accessible **offline!**

> **Install:**

> - sudo apt-get install python3-gi glade
> - pip3 install selenium
> - python3 main.py



**Preferences**



target = 'http://mysite.com/admin/' # target page with a form-based authentication.
xPathLogin = "// input [@ name = 'login']" # xPath for the login field.
xPathPassword = "// input [@ name = 'password']" # xPath for the field password.
xPathAcceptButton = "// input [@ type = 'submit']" # xPath to enter the confirmation button.
xPathSuccessAuth = "// a [@ id = 'loginLink']" # xPath for successful authorization conditions.
xPathFailAuth = "// div [@ id = 'error']" # xPath authorization failure conditions.
selBrowserString = '* firefox' # browser shows Selenium WebDriver which browser you want to run: * firefox, * chrome, * ie.
selFFProfile = 'ff_profile' # Profile Mozilla. This option is only used ff. This is a relative path to the directory with the profile.
Parameters for brute forcer:
usersFile = 'dict / users.txt' # path to a file with a list of usernames.
passwordsFile = 'dict / pwd.txt' # path to a file with a list of passwords.
resultFile = 'result.txt' # path to the file to output the results.
brutThreads = 1 # The number of threads to run brute force.


