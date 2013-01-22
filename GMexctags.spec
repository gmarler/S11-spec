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
# SUNW_BaseDir:            %{_basedir}
SUNW_BaseDir:            /
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

# %include default-depend.inc

BuildRequires:           file/gnu-coreutils

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
mkdir  $RPM_BUILD_ROOT
# Unfortunately, DESTDIR doesn't work for this release
# gmake install DESTDIR=$RPM_BUILD_ROOT
#
# Create intermediate dirs under ${RPM_BUILD_ROOT}, which we created above
ginstall -D -v -m 755 ctags   ${RPM_BUILD_ROOT}/usr/bin/exctags
ginstall -D -v -m 644 ctags.1 ${RPM_BUILD_ROOT}/usr/share/man/man1/exctags.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%attr(0555, root, bin) %{_bindir}/exctags
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%attr(0444, root, bin) %{_mandir}/man1/exctags.1

%changelog
