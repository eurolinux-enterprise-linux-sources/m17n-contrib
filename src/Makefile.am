# Makefile.am -- Makefile for the m17n-contrib
# Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2012
#   National Institute of Advanced Industrial Science and Technology (AIST)
#   Registration Number H15PRO112

# This file is part of the m17n-contrib; a sub-part of the m17n
# library.

# The m17n library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1 of
# the License, or (at your option) any later version.

# The m17n library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with the m17n library; if not, write to the Free
# Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301, USA.

m17ndir = @M17NDIR@
m17n_icondir = ${m17ndir}/icons
m17n_DATA = @INPUT_METHOD@
m17n_icon_DATA= @ICONS@
m17n_scriptdir =  ${m17ndir}/scripts
m17n_script_SCRIPTS = tbl2mim.awk

EXTRA_DIST = config.rpath m4/ChangeLog  ${m17n_DATA} ${m17n_icon_DATA} \
	${m17n_script_SCRIPTS} bootstrap.sh

SUBDIRS = po

ACLOCAL_AMFLAGS = -I m4
