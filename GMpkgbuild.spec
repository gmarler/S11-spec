#
# spec file for package GMpkgbuild
#
#
%include Solaris.inc

%define  pversion 1.3.104

Summary:      pkgbuild - rpmbuild-like tool for building Solaris packages
Name:         GMpkgbuild
Version:      %{pversion}.4
License:      GPLv2
URL:          http://pkgbuild.sourceforge.net/
Source:       %{sf_download}/pkgbuild/pkgbuild-%{pversion}.tar.bz2
Source1:      pkgbuild-env.sh
# Patches
Patch0:       pkgbuild-%{pversion}.patch
BuildRoot: 	  %{_tmppath}/%{name}-%{version}-build
SUNW_BaseDir:	/
IPS_legacy:   false

Meta(info.maintainer):          gmarler@gmarler.com
Meta(info.maintainer_url):      gmarler@gmarler.com
Meta(info.upstream_url):        http://www.gmarler.com/

%include default-depend.inc

# Disable internal dependency generator for this pkg - we'll explicitly
# define them ourselves
%define _use_internal_dependency_generator 0

# Dependencies
BuildRequires:    developer/build/cmake
# BuildRequires:  system/xopen/xcu4
# BuildRequires:  ss-dev
# # BuildRequires:  gcc-dev
# BuildRequires:  text/gnu-patch
# BuildRequires:  web/wget
# BuildRequires:  archiver/gnu-tar 
# #BuildRequires:  x11/header/header-xorg
# BuildRequires:  package/svr4
# BuildRequires:  library/perl-5/xml-parser
# BuildRequires:  developer/build/gnu-make
# BuildRequires:  developer/build/automake-110
# BuildRequires:  developer/gnome/gnome-doc-utils
# BuildRequires:  text/gnu-sed
# BuildRequires:  text/gawk
# BuildRequires:  text/gnu-diffutils
# BuildRequires:  file/gnu-coreutils
# BuildRequires:  library/gnome/base-libs
# BuildRequires:  developer/gnome/gettext
# BuildRequires:  text/gnu-gettext
# BuildRequires:  text/gnu-gettext
# BuildRequires:  file/gnu-findutils
# BuildRequires:  developer/macro/gnu-m4
# BuildRequires:  system/xopen/xcu6
# BuildRequires:  data/docbook
# BuildRequires:  runtime/python-24
# BuildRequires:  runtime/tcl-8
# BuildRequires:  image/library/libtiff
# BuildRequires:  runtime/tk-8
# BuildRequires:  system/management/sysidtool
# BuildRequires:  system/library/sysidtool
# BuildRequires:  service/management/sysidtool
# BuildRequires:  developer/library/lint
# BuildRequires:  system/file-system/autofs
# BuildRequires:  shell/bash
# BuildRequires:  network/ftp
# BuildRequires:  compress/bzip2
# BuildRequires:  library/java/demo
# BuildRequires:  library/java/demo64
# BuildRequires:  library/java/host-config
# BuildRequires:  runtime/java
# BuildRequires:  runtime/java/runtime64
# BuildRequires:  library/java/manual
# BuildRequires:  developer/java/jdk
# BuildRequires:  developer/java/jdk64
# BuildRequires:  developer/object-file
# BuildRequires:  developer/versioning/subversion
# #BuildRequires:  x11/header
# BuildRequires:  developer/solarisstudio123

Requires:       system/xopen/xcu4 = *
Requires:       system/kernel     >= 0.5.11-0.175.0.3.0.4.1
Requires:       system/library    = *
Requires:       system/core-os    = *
Requires:       runtime/perl-512  = *
Requires:       shell/bash        = *

%description
This package delivers the pkgbuild product to Solaris systems.
It is a rpmbuild-like tool for generating Solaris packages,
primarily IPS packages.


%prep
%setup -q -n pkgbuild-%{pversion}
echo "pkgbuild %{_pkgbuild_version}"

%build

PATH=/usr/bin:/usr/gnu/bin:$PATH ./configure
# Can only patch pkgbuild.pl after it has been created by the configure script
%patch0 -p5

%install

gmake    install DESTDIR=$RPM_BUILD_ROOT
ginstall %{SOURCE1} ${RPM_BUILD_ROOT}/opt/pkgbuild/bin/env.sh

%files
%defattr      (-, root, root)
#
%dir %attr (0755, root, sys)  /opt
%dir %attr (0755, root, bin)  /opt/pkgbuild
/opt/pkgbuild/*

