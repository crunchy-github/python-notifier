#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# log.py
# 
# Author: Andreas Büsching <crunchy@tzi.de>
# 
# log - a logging facility for the generic notifier module
# 
# $Id$
# 
# Copyright (C) 2004 Andreas Büsching <crunchy@tzi.de>
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
 
import logging

instance = logging.getLogger( 'notifier' )

debug = instance.debug
info = instance.info
warn = instance.warn
error = instance.error
critical = instance.critical
exception = instance.exception
