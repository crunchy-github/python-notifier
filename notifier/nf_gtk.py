#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# nf_gtk.py
# 
# Author: Andreas Büsching <crunchy@tzi.de>
# 
# notifier wrapper for GTK+ 2.x
# 
# $Id$
# 
# Copyright (C) 2004, 2005 Andreas Büsching <crunchy@tzi.de>
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

"""Simple mainloop that watches sockets and timers."""

import gobject
import gtk

import popen2

IO_READ = gobject.IO_IN
IO_WRITE = gobject.IO_OUT
IO_EXCEPT = gobject.IO_ERR

# map of Sockets/Methods -> gtk_input_handler_id
_gtk_socketIDs = {}
_gtk_socketIDs[ IO_READ ] = {}
_gtk_socketIDs[ IO_WRITE ] = {}

def addSocket( socket, method, condition = IO_READ ):
    """The first argument specifies a socket, the second argument has to be a
    function that is called whenever there is data ready in the socket."""
    global _gtk_socketIDs
    source = gobject.io_add_watch( socket, condition,
                                   _socketCallback, method )
    _gtk_socketIDs[ condition ][ socket ] = source

def _socketCallback( source, condition, method ):
    global _gtk_socketIDs
    if _gtk_socketIDs[ condition ].has_key( source ):
        ret = method( source )
        if not ret:
            del _gtk_socketIDs[ condition ][ source ]
        return ret

    print 'socket not found'
    return False

def removeSocket( socket, condition = IO_READ ):
    """Removes the given socket from scheduler."""
    global _gtk_socketIDs
    if _gtk_socketIDs[ condition ].has_key( socket ):
	gobject.source_remove( _gtk_socketIDs[ condition ][ socket ] )
	del _gtk_socketIDs[ condition ][ socket ]

def addTimer( interval, method ):
    """The first argument specifies an interval in milliseconds, the
    second argument a function. This is function is called after
    interval seconds. If it returns true it's called again after
    interval seconds, otherwise it is removed from the scheduler. The
    third (optional) argument is a parameter given to the called
    function."""
    return gobject.timeout_add( interval, method )

def removeTimer( id ):
    """Removes _all_ functioncalls to the method given as argument from the
    scheduler."""
    gobject.source_remove( id )

addDispatcher = None
removeDispatcher = None

def step():
    gtk.main_iteration_do()

def loop():
    """Execute main loop forver."""
    while 1:
        step()
