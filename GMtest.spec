#
# spec file for package: gtk-gnutella
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s): NONE
#

%include Solaris.inc

Name:           GMtest
Summary:        Test package
Version:        0.0.1
License:        GPLv2
#URL:            http://gtk-gnutella.sourceforge.net/
#Source:         http://downloads.sourceforge.net/project/%{short_name}/%{short_name}/%{version}/%{short_name}-%{version}.tar.bz2
Distribution:   OpenSolaris
Vendor:		      OpenSolaris Community
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_Basedir:   %{_basedir}
#SUNW_Copyright: %{short_name}.copyright

%include default-depend.inc

#
# BuildRequires: (configuration/compile time requirements)
#
#
# Requires: (runtime requirements)
#

%description
A simple test package

%prep

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d -m 755 $RPM_BUILD_ROOT/%{_bindir}
cp /etc/group $RPM_BUILD_ROOT/%{_bindir}/testfile


%clean
rm -rf $RPM_BUILD_ROOT

#

%files
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{_bindir}
%attr(0555, root, bin) %{_bindir}/*

%changelog
* Sat Aug 28, 2011 - gmarler@gmarler.com
- update to 0.97
* Sat Apr 23, 2011 - gmarler@gmarler.com
- update to 0.96.9
* Fri Feb 04, 2011 - gmarler@gmarler.com
- Use new S11 Express naming scheme
- use of short_name
* Thu Aug 27 - gmarler@gmarler.com
Initial spec file, all %files directives
Fix Source location
* Thu Aug 28 - gmarler@gmarler.com
Add entries for %{_prefix}/share/pixmaps/
Fix several dir perms so we won't have conflicts with other packages
Fix locale dir perms
Properly compute the number of CPUs for building, and use in gmake invocation
* Tue Sep 1 - gmarler@gmarler.com
Add Requires runtime packages
Add all remaining BuildRequires statements
Substitute %{name} and %{version} where appropriate
* Wed Sep 2 - gmarler@gmarler.com
Fix line endings from DOS to Unix
* Thu Sep 3 - gmarler@gmarler.com
add changelog back in
Eliminate Group field
Fix Meta(info.classification) field
## Re-build 24/09/09
