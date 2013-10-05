%define git_rev 7946e2c

%define _libdir     /opt/GM/lib
%define _includedir /opt/GM/include
#%define optflags    -xO3

Name:           linenoise
Version:        0
Release:        4.git%{git_rev}
Summary:        Minimal replacement for readline

License:        BSD
URL:            https://github.com/tadmarshall/linenoise
Source0: https://github.com/tadmarshall/linenoise/tarball/%{git_rev}/tadmarshall-%{name}-%{git_rev}.tar.gz
Patch0:         %{name}-build-shared-lib.patch
Patch1:         %{name}-symbol-visibility.patch

%description
Linenoise is a replacement for the readline line-editing library with the goal 
of being smaller.

%prep
%setup -q -n tadmarshall-%{name}-%{git_rev}
%patch0 -p0
%patch1 -p1

%build
CC=cc
CXX=CC
LIBDIR="%{_libdir}" INCLUDEDIR="%{_includedir}" CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
LIBDIR="%{_libdir}" INCLUDEDIR="%{_includedir}" CFLAGS="%{optflags}" make %{?_smp_mflags} DESTDIR="%{buildroot}" install

%files
%doc README.markdown
%{_libdir}/liblinenoise.so.*
%{_includedir}/linenoise.h
%{_libdir}/liblinenoise.so

%changelog
