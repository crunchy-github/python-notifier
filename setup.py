#!/usr/bin/env python

from distutils.core import setup

setup( name	= 'pyNotifier',
       version	= '0.1.2',
       license  = 'GPL',       
       description = 'a generic notifier, which can be used with a lot a different widget sets',       
       author	= 'Andreas B�sching',
       author_email = 'crunchy@tzi.de',
       url	= '',
       packages = [ 'notifier', 'notifier.gtk', 'notifier.qt', 'notifier.wx' ],
     )