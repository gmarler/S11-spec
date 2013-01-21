#
# spec file for package GMexctags
#
#
# %include Solaris.inc

# %include usr-gnu.inc

Name:                    GMexctags
Summary:                 Exuberant ctags
Version:                 5.8
Source:                  http://prdownloads.sourceforge.net/ctags/ctags-%{version}.tar.gz
URL:                     http://ctags.sourceforge.net/
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

# %include default-depend.inc

%prep
%setup -q -n ctags-%{version}

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CC=cc
export CXX=CC
# export CFLAGS="%optflags"
export CFLAGS="-xO3"
# export LDFLAGS="%{_ldflags}"
./configure                                 \
        --prefix=%{_prefix}                 \
        --libexecdir=%{_libexecdir}         \
        --libdir=%{_libdir}                 \
        --mandir=%{_mandir}                 \
        --datadir=%{_datadir}               \
        --infodir=%{_datadir}/info

gmake -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
# Unfortunately, DESTDIR doesn't work for this release
# gmake install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/db*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libdb*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/*

%changelog
