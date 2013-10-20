%include optGM.inc

%define git_rev    7946e2c
%define short_name linenoise

Name:           GM%{short_name}
Version:        0
Release:        4.git%{git_rev}
Summary:        Minimal replacement for readline

License:        BSD
URL:            https://github.com/tadmarshall/linenoise
Source0: https://github.com/tadmarshall/linenoise/tarball/%{git_rev}/tadmarshall-%{short_name}-%{git_rev}.tar.gz
Patch0:         %{short_name}-build-shared-lib.patch
Patch1:         %{short_name}-symbol-visibility.patch

%description
Linenoise is a replacement for the readline line-editing library with the goal 
of being smaller.

%prep
%setup -q -n tadmarshall-%{short_name}-%{git_rev}
%patch0 -p1
%patch1 -p1

%build
export CC=cc CXX=CC
LIBDIR="%{_libdir}" INCLUDEDIR="%{_includedir}" CFLAGS="%{optflags}" gmake %{?_smp_mflags}

%install
export CC=cc CXX=CC
LIBDIR="%{_libdir}" INCLUDEDIR="%{_includedir}" CFLAGS="%{optflags}" gmake %{?_smp_mflags} DESTDIR="%{buildroot}" install

%files
%doc README.markdown
%{_libdir}/liblinenoise.so.*
%{_includedir}/linenoise.h
%{_libdir}/liblinenoise.so

%changelog
