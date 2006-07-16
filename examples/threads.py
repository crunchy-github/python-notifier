#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Author: Andreas Büsching <crunchy@bitkipper.net>
#
# en example demonstrating the process handler class
#
# $Id$
#
# Copyright (C) 2006
#	Andreas Büsching <crunchy@bitkipper.net>
#
# This library is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version
# 2.1 as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301 USA

import notifier
import notifier.threads as threads

import time

def my_thread( words ):
    i = 50
    while i:
	print i, words
	time.sleep( 0.1 )
	i -= 1
    return words.reverse()

def done_with_it( thread, result ):
    print "Thread '%s' is finished" % thread.name()
    print "Result:", result

def doing_something_else():
    print 'doing something else'
    return True

if __name__ == '__main__':
    notifier.init( notifier.GENERIC )

#     notifier.dispatcher_add( threads.results )
    task = threads.Thread( 'test',
			   notifier.Callback( my_thread, [ 'hello', 'world' ] ),
			   done_with_it )
    task.run()
    notifier.timer_add( 1000, doing_something_else )
    notifier.loop()