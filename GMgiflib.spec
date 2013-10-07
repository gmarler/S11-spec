
Summary:  Library for manipulating GIF format image files
Name:   GMgiflib
Version:  4.1.6
Release:  9%{?dist}
License:  MIT
Group:    System Environment/Libraries
URL:    http://www.sourceforge.net/projects/%{name}/
Source:   http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  libX11-devel, libice, libsm, libxt
#Provides: libungif = %{version}-%{release}
#Obsoletes:  libungif <= %{version}-%{release}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The giflib package contains a shared library of functions for loading and
saving GIF format image files. It is API and ABI compatible with libungif,
the library which supported uncompressed GIFs while the Unisys LZW patent
was in effect.

%prep
%setup -q

%build
%configure
gmake %{?_smp_mflags} all

# Handling of libungif compatibility
MAJOR=`echo '%{version}' | sed -e 's/\([0-9]\+\)\..*/\1/'`
%{__cc} -G -KPIC -o libungif.so.$MAJOR -Llib/.libs -lgif -o libungif.so.%{version}

%install
rm -rf $RPM_BUILD_ROOT
gmake DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install

# Handling of libungif compatibility
ginstall -p -m 755 libungif.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -sf libungif.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libungif.so.4
ln -sf libungif.so.4 $RPM_BUILD_ROOT%{_libdir}/libungif.so

# Don't install any static .a and libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

# Remove makefile relics from documentation
rm -f doc/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc doc/* util/giffiltr.c util/gifspnge.c
%{_libdir}/lib*.so.*
%{_libdir}/lib*.so
%{_includedir}/*.h
%{_bindir}/*


%changelog
