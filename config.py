#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Gilmullin T.M.

# This is configuration file for Password Bruter with default parameters. Please, do not change variable's names.


# ---------- Form-based Auth page parameters ---------------------------------------------------------------------------
# Start URL for Password Bruter.
target = 'http://10.111.113.83/dvwa/vulnerabilities/brute/'

# xPath for Login field.
xPathLogin = "//input[@name='username']"

# xPath for Password field.
xPathPassword = "//input[@name='password']"

# xPath for oK button.
xPathAcceptButton = "//input[@name='Login']"

# xPath for Success auth.
xPathSuccessAuth = "//img[@src='http://10.111.113.83/dvwa/hackable/users/admin.jpg']"

# xPath for Fail auth.
xPathFailAuth = "//pre[contains(text(), 'Username and/or password incorrect.']"

# Selenium Browser string. This param shows Selenium WebDriver which browser to run: *firefox, *chrome, *ie
selBrowserString = '*chrome'

# Mozilla profile. This param used only for ff. This is relative path to dir with mozilla profile config.
selFFProfile = 'ff_profile'


# ---------- Bruter parameters -----------------------------------------------------------------------------------------
# Path to user's list.
usersFile = 'dict/users.txt'

# Path to password's list.
passwordsFile = 'dict/pwd.txt'

# Path to result file.
resultFile = 'result.txt'

# How many threads do you need?
brutThreads = 1

# Rump up period when all browsers will open and all threads will in progress.
rumpUpPeriod = brutThreads * 5

# Operation's timeout in seconds.
timeout = 1

# If this key is True then Bruter uses random item from user's list and password's list in every iteration.
randomCredentials = False


# ---------- Random Generator parameters -------------------------------------------------------------------------------
# Random Generator parameter. 1 number - number of strings, 2 - string's length, 3 - use or not Numbers,
# 4 - use or not English Upper Case Chars, 5 - use or not English Lower Case Chars,
# 6 - use or not Russian Upper case chars, 7 - use or not Russian Lower Case Chars, 8 - use or not Special Simbols.
# Output file: dict/rnd_<date_time>.txt
randomGeneratorParameter = [100, 8, 1, 1, 1, 0, 0, 0]
