dnl Autoconf script for the m17n-contrib.
dnl Process this file with autoconf to produce a configure script.
dnl
dnl Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2012
dnl   National Institute of Advanced Industrial Science and Technology (AIST)
dnl   Registration Number H15PRO112
dnl
dnl This file is part of the m17n-contrib; a sub-part of the m17n
dnl library.
dnl
dnl The m17n library is free software; you can redistribute it and/or
dnl modify it under the terms of the GNU Lesser General Public License
dnl as published by the Free Software Foundation; either version 2.1 of
dnl the License, or (at your option) any later version.
dnl
dnl The m17n library is distributed in the hope that it will be useful,
dnl but WITHOUT ANY WARRANTY; without even the implied warranty of
dnl MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
dnl Lesser General Public License for more details.
dnl
dnl You should have received a copy of the GNU Lesser General Public
dnl License along with the m17n library; if not, write to the Free
dnl Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
dnl Boston, MA 02110-1301, USA.

AC_INIT(m17n-contrib, 1.1.14, bugs-m17n-lib@m17n.org)
AM_INIT_AUTOMAKE
AM_GNU_GETTEXT([external])

# Checks for programs.
AC_PROG_AWK

AC_CHECK_PROG(HAVE_M17N_DB, m17n-db, yes)
if test "x$HAVE_M17N_DB" != "xyes"; then
  AC_MSG_ERROR([Please install m17n-db at first.
It is available at <http://www.m17n.org/m17n-lib>.])
fi

if test "x$prefix" = "xNONE"; then
  M17NDIR=`m17n-db`
else
  M17NDIR='${datadir}/m17n'
fi
AC_SUBST(M17NDIR)

INPUT_METHOD=`echo im/*.mim`
AC_SUBST(INPUT_METHOD)
ICONS=`echo im/*.png`
AC_SUBST(ICONS)

AC_CONFIG_FILES([Makefile po/Makefile.in])
AC_OUTPUT
