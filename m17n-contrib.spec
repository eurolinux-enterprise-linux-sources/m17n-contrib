Name:     m17n-contrib
Summary:  Contributed multilingualization datafiles for m17n-lib
Version:  1.1.14
Release:  3%{?dist}
Group:    System Environment/Libraries
License:  LGPLv2+
URL:      http://www.nongnu.org/m17n
Source0:  http://download-mirror.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz
Source1:  mai-inscript.mim
Source2:  ks-inscript.mim
Source3:  kn-typewriter.mim
## Till the Inscript2 gets upstreamed in m17n-lib, use this source
Source4:  https://fedorahosted.org/releases/i/n/inscript2/inscript2-20120320.tar.gz
Patch0:   bug433416-bn-probhat.patch
Patch1:   as-inscript-keysummary-440201.patch
Patch2:   ml-inscript-keysummary-435259.patch
Patch3:   kn-inscript-ZWNJ-440007.patch
Patch4:   or-inscript-ZWJ-ZWNJ-466748.patch
Patch6:   te-inscript-ZWJ-451203.patch
Patch7:   te-inscript-642134.patch

BuildArch: noarch
BuildRequires: m17n-db-devel 
Requires: m17n-db

Obsoletes: m17n-contrib-assamese < 1.1.11
Obsoletes: m17n-contrib-bengali < 1.1.11
Obsoletes: m17n-contrib-czech < 1.1.11
Obsoletes: m17n-contrib-esperanto < 1.1.11
Obsoletes: m17n-contrib-gujarati < 1.1.11
Obsoletes: m17n-contrib-hindi < 1.1.11
Obsoletes: m17n-contrib-kannada < 1.1.11
Obsoletes: m17n-contrib-kashmiri < 1.1.11
Obsoletes: m17n-contrib-maithili < 1.1.11
Obsoletes: m17n-contrib-malayalam < 1.1.11
Obsoletes: m17n-contrib-marathi < 1.1.11
Obsoletes: m17n-contrib-nepali < 1.1.11
Obsoletes: m17n-contrib-oriya < 1.1.11
Obsoletes: m17n-contrib-pashto < 1.1.11
Obsoletes: m17n-contrib-punjabi < 1.1.11
Obsoletes: m17n-contrib-russian < 1.1.11
Obsoletes: m17n-contrib-sindhi < 1.1.11
Obsoletes: m17n-contrib-sinhala < 1.1.11
Obsoletes: m17n-contrib-tai < 1.1.11
Obsoletes: m17n-contrib-tamil < 1.1.11
Obsoletes: m17n-contrib-telugu < 1.1.11
Obsoletes: m17n-contrib-urdu < 1.1.11
Obsoletes: m17n-contrib-vietnamese < 1.1.11

Provides: m17n-contrib-assamese = %{version}-%{release}
Provides: m17n-contrib-bengali = %{version}-%{release}
Provides: m17n-contrib-czech = %{version}-%{release}
Provides: m17n-contrib-esperanto = %{version}-%{release}
Provides: m17n-contrib-gujarati = %{version}-%{release}
Provides: m17n-contrib-hindi = %{version}-%{release}
Provides: m17n-contrib-kannada = %{version}-%{release}
Provides: m17n-contrib-kashmiri = %{version}-%{release}
Provides: m17n-contrib-maithili = %{version}-%{release}
Provides: m17n-contrib-malayalam = %{version}-%{release}
Provides: m17n-contrib-marathi = %{version}-%{release}
Provides: m17n-contrib-nepali = %{version}-%{release}
Provides: m17n-contrib-oriya = %{version}-%{release}
Provides: m17n-contrib-pashto = %{version}-%{release}
Provides: m17n-contrib-punjabi = %{version}-%{release}
Provides: m17n-contrib-russian = %{version}-%{release}
Provides: m17n-contrib-sindhi = %{version}-%{release}
Provides: m17n-contrib-sinhala = %{version}-%{release}
Provides: m17n-contrib-tai = %{version}-%{release}
Provides: m17n-contrib-tamil = %{version}-%{release}
Provides: m17n-contrib-telugu = %{version}-%{release}
Provides: m17n-contrib-urdu = %{version}-%{release}
Provides: m17n-contrib-vietnamese = %{version}-%{release}

%description
This package contains contributed multilingualization (m17n) datafiles
for the m17n-lib project.

%package extras
Summary:  Extra m17n-contrib files
Group:    System Environment/Libraries
Requires: %{name} = %{version}-%{release}

Obsoletes: m17n-contrib-chinese < 1.1.11
Provides: m17n-contrib-chinese = %{version}-%{release}

%description extras
m17n-db extra files for input maps that are less used.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p0
%patch7 -p0

##extract inscript2 maps
tar xzf %{SOURCE4} 

%build
%configure
make


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/m17n/
cp -p inscript2/IM/* $RPM_BUILD_ROOT%{_datadir}/m17n/
cp -p inscript2/icons/* $RPM_BUILD_ROOT%{_datadir}/m17n/icons/
rm -rf $RPM_BUILD_ROOT/%{_bindir}

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_datadir}/m17n/scripts
%{_datadir}/m17n/a*.mim
%{_datadir}/m17n/b*.mim
%{_datadir}/m17n/c*.mim
%{_datadir}/m17n/d*.mim
%{_datadir}/m17n/e*.mim
%{_datadir}/m17n/g*.mim
%{_datadir}/m17n/h*.mim
%{_datadir}/m17n/i*.mim
%{_datadir}/m17n/k*.mim
%{_datadir}/m17n/m*.mim
%{_datadir}/m17n/n*.mim
%{_datadir}/m17n/o*.mim
%{_datadir}/m17n/p*.mim
%{_datadir}/m17n/r*.mim
%{_datadir}/m17n/s*.mim
%{_datadir}/m17n/t*.mim
%{_datadir}/m17n/u*.mim
%{_datadir}/m17n/v*.mim
%{_datadir}/m17n/y*.mim
%{_datadir}/m17n/icons/a*.png
%{_datadir}/m17n/icons/b*.png
%{_datadir}/m17n/icons/c*.png
%{_datadir}/m17n/icons/d*.png
%{_datadir}/m17n/icons/e*.png
%{_datadir}/m17n/icons/g*.png
%{_datadir}/m17n/icons/h*.png
%{_datadir}/m17n/icons/i*.png
%{_datadir}/m17n/icons/k*.png
%{_datadir}/m17n/icons/m*.png
%{_datadir}/m17n/icons/n*.png
%{_datadir}/m17n/icons/o*.png
%{_datadir}/m17n/icons/p*.png
%{_datadir}/m17n/icons/s*.png
%{_datadir}/m17n/icons/t*.png
%{_datadir}/m17n/icons/u*.png
%{_datadir}/m17n/icons/v*.png
%{_datadir}/m17n/icons/y*.png


%files extras 
%{_datadir}/m17n/zh-*.mim
%{_datadir}/m17n/icons/zh*.png

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.14-3
- Mass rebuild 2013-12-27

* Fri Jul 12 2013 Parag Nemade <pnemade AT redhat DOT com> - 1.1.14-2.1
- Resolves:rh#983613: Bring back Obsoletes for upgrade from rhel6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 18 2012 Parag Nemade <pnemade AT redhat DOT com> - 1.1.14-1
- update to 1.1.14
- upload fixed tarball

* Tue Jul 24 2012 Parag Nemade <pnemade AT redhat DOT com> - 1.1.13-5
- Resolves:rh#803571-[Punjabi-Jhelum] Addition to keyboard layout
- Resolves:rh#815385-[kn_IN] Add Kannada typewriter keyboard layout
- Resolves:rh#803652-Inscript2 for Bengali contains a wrong key mapping
- Resolves:rh#804898-[bn_IN] Add missing 'z' key mapping in inscript2 keymap
- Resolves:rh#803207-(as_IN)Instead of Assamese ra (u09f0) Bengali ra (u09b0) is mapped
- Resolves:rh#803236-(as_IN)Letter 'ma' (ম) and 'wa' (ৱ) not mapped for Assamese

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Parag Nemade <pnemade AT redhat DOT com> - 1.1.13-2
- Resolves:rh#746562 - Add draft version of Inscript2 keymaps

* Tue Oct 11 2011 Parag Nemade <pnemade AT redhat DOT com> - 1.1.13-1
- update to 1.1.13

* Fri Apr 01 2011 Parag Nemade <pnemade AT redhat DOT com> - 1.1.12-5
- Resolves:rh#692351 - [indic] Add Rupee Sign support in Inscript maps

* Tue Mar 22 2011 Parag Nemade <pnemade AT redhat DOT com> - 1.1.12-4
- Resolves: rh#679289 - please include kashmiri inscript keyboard
- Removed Obsoletes and Provides added in f14

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 28 2010 Parag Nemade <pnemade AT redhat.com> - 1.1.12-2
- Resolves:rh#642134-[te_IN] [inscript] U0C60, U0C44 and U0C01 need key mapping in inscript keymap.

* Wed Oct 06 2010 Parag Nemade <pnemade AT redhat.com> - 1.1.12-1
- update to new upstream release 1.1.12

* Wed Jul 07 2010 Parag Nemade <pnemade AT redhat.com> -1.1.11-4
- Add patches ta-tamil99-enhancement.patch ml-inscript-semicolon-577171.patch

* Mon May 17 2010 Parag Nemade <pnemade AT redhat.com> -1.1.11-3
- Add patch hi-remington-enhancements-591810.patch
- Fix upgrade path from F-13 

* Wed Apr 07 2010 Parag Nemade <pnemade AT redhat.com> - 1.1.11-2
- bump release; spec cleanup

* Wed Apr 07 2010 Parag Nemade <pnemade AT redhat.com> - 1.1.11-1
- update to new upstream release 1.1.11

* Tue Jan 19 2010 Parag Nemade <pnemade AT redhat.com> -1.1.10-3
- Add patch te-inscript-ZWJ-451203.patch

* Mon Aug 17 2009 Parag Nemade <pnemade@redhat.com> -1.1.10-2
- Add patch kn-kgp-halantha-ayogavaaha.patch

* Wed Jul 29 2009 Parag Nemade <pnemade@redhat.com> -1.1.10-1
- update to new upstream release 1.1.10 
- Resolves: rh#513920: [pa_IN]Jhelum layout conflict with shortcut key in lokalize
- revert pa-jhelum-numeric-503478.patch to its original version.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-7
- update patch pa-jhelum-numeric-503478.patch

* Tue Jun 02 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-6
- Resolves: rh#503478-[pa_IN][Jhelum] layout need update for Gurmukhi Numeric

* Wed May 06 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-5
- Resolves: rh#485152- Kashmiri (Arabic-persian) language keyboard layout 

* Wed Apr 08 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-4
- Resolves: rh#494810-[indic][m17n-db][m17n-contrib] ibus .engine files no longer needed for new ibus

* Mon Apr 06 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-3
- Fix broken deps for maithili subpackage.

* Fri Apr 03 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-2
- Resolves: rh#491794 [mai_IN] Removing @maithili-support removes m17n-db-hindi package
- Resolves: rh#493793 [mai_IN] No default keymap for language

* Tue Mar 03 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-1
- Update to new upstream release 1.1.9

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 05 2008 Parag Nemade <pnemade@redhat.com> -1.1.8-2.fc10
- Resolves: Bug 466748-[or_IN] Needed ZWJ & ZWNJ for Oriya Inscript keymap

* Tue Oct 21 2008 Parag Nemade <pnemade@redhat.com> -1.1.8-1.fc10
- Update to new upstream release 1.1.8

* Mon Oct 20 2008 Jens Petersen <petersen@redhat.com> - 1.1.7-5.fc10
- add obsoletes for ibus-m17n subpackages

* Wed Oct 15 2008 Parag Nemade <pnemade@redhat.com> - 1.5.2-4
- create .engine files for ibus-m17n with m17n-gen-ibus-engine (#466410)

* Thu Sep 04 2008 Parag Nemade <pnemade@redhat.com> -1.1.7-3
- Resolves: rh# Bug 458264-Required Inscript map for Sindhi language

* Fri Jul 04 2008 Parag Nemade <pnemade@redhat.com> -1.1.7-2
- Resolves: rh#453910: [kn_IN]Include latest kn- kgp.mim againist the latest build

* Thu Jul 03 2008 Parag Nemade <pnemade@redhat.com> -1.1.7-1
- Update to new upstream release 1.1.7

* Wed May 21 2008 Parag Nemade <pnemade@redhat.com> -1.1.6-4
- Resolves: rh#447682,rh#447683

* Wed Apr 02 2008 Parag Nemade <pnemade@redhat.com> -1.1.6-3.fc9
- Resolves: rh#440201,rh#435259,rh#440007

* Thu Feb 28 2008 Parag Nemade <pnemade@redhat.com> -1.1.6-2.fc9
- Resolves: rh#433416

* Thu Feb 07 2008 Parag Nemade <pnemade@redhat.com> -1.1.6-1.fc9
- Update to new upstream release 1.1.6
- Resolves: rh#431169

* Thu Jan 24 2008 Parag Nemade <pnemade@redhat.com> -1.1.5-2
- Resolves:rh#430054

* Mon Dec 31 2007 Parag Nemade <pnemade@redhat.com> -1.1.5-1.fc9
- Update to new upstream release 1.1.5

* Fri Dec 28 2007 Parag Nemade <pnemade@redhat.com> -1.1.4-1.fc9
- Update to new upstream release 1.1.4

* Tue Dec 18 2007 Parag Nemade <pnemade@redhat.com> -1.1.3-4.fc9
- Resolves: rh#404081, rh#419691

* Mon Aug 13 2007 Parag Nemade <pnemade@redhat.com>
- update License tag

* Wed Jul 25 2007 Parag Nemade <pnemade@redhat.com> - 1.1.3-3
- Added m17n-contrib as Requires for mk_pkg() macro generating packages.
- Added m17b-contrib and m17n-db-lang as Requires
  for mk_pkg_uses_db() macro generating packages.

* Wed Jul 25 2007 Parag Nemade <pnemade@redhat.com> - 1.1.3-2
- Import to cvs
- bump release

* Tue Jul 24 2007 Parag Nemade <pnemade@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Tue Jul 24 2007 Parag Nemade <pnemade@redhat.com>
- Bump release

* Mon Jul 23 2007 Parag Nemade <pnemade@redhat.com>
- SPEC cleanup
- make tbl2mim.awk executable
- bump release

* Mon Jul 23 2007 Parag Nemade <pnemade@redhat.com>
- updated SPEC according to suggestions from Jens Petersen in #249006

* Fri Jul 20 2007 Parag Nemade <pnemade@redhat.com> - 1.1.2-1
- Initial package for Fedora Review.
