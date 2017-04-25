GUI-brut-form
===================

Brutforce web forms has never been so easy

----------

![gif](http://s8.hostingkartinok.com/uploads/images/2017/01/17d2d59991f78dc9ece63376531627b4.gif)

How to use
-------------


## Quick start
```
$ sudo pacman -S python-gobject
$ pip3 install selenium
$ python3 main.py
```



**Preferences**

1. target = 'http://mysite.com/admin/' # target page with a form-based
2. authentication. xPathLogin = "// input [@ name = 'login']" # xPath for the login field. 
3. xPathPassword = "// input [@ name = 'password']" # xPath for the field password. 
4. xPathAcceptButton = "//input [@ type = 'submit']" # xPath to enter the confirmation button.
5. xPathSuccessAuth = "// a [@ id = 'loginLink']" # xPath fo successful authorization conditions.  xPathFailAuth = "// div [@ id ='error']" # xPath authorization failure conditions. 
6. selBrowserString = '* firefox' # browser shows Selenium WebDriver which browser you want to run: * firefox, * chrome, * ie. 
7. selFFProfile = 'ff_profile'  # Profile Mozilla. This option is only used ff. This is a relative path to the directory with the profile. Parameters for brute forcer:
8. usersFile = 'dict / users.txt' # path to a file with a list of
9. usernames. passwordsFile = 'dict / pwd.txt' # path to a file with a list of passwords. 
10. resultFile = 'result.txt' # path to the file tooutput the results.
11. brutThreads = 1 # The number of threads to run brute force.


