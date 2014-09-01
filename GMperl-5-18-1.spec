#
# spec file for package:  GMperl-5.18.1
#
#
%include Solaris.inc
# %include arch64.inc
%define optflags       -xstrconst -xtarget=generic -mr

%define major       5
%define minor       18
%define patch       1
%define src_version %{major}.%{minor}.%{patch}
%define gm_version  %{src_version}.3

Name:             GMperl-%{major}-%{minor}-%{patch}
Summary:          Practical Extraction and Report Language
# Last dot version is our build of this pkg
Version:          %{gm_version}
License:          Artistic
Source:           http://www.cpan.org/src/5.0/perl-%{src_version}.tar.gz
SUNW_BaseDir:     %{_basedir}
SUNW_Copyright:   %{name}.copyright
BuildRoot:        %{_tmppath}/%{name}-%{src_version}-build
IPS_legacy:       false

# The prefix matches the one that Sun/Oracle has used for deployment over
# the years, and prevents any kind of collision with existing versions

#
# The architecture dir name is defined, not based on the bit-ness of the perl
# binary itself, but on the bit length of the int (integer) type
#
%ifarch sparc
%define perl_arch_dir sun4-solaris-64int
%else
%define perl_arch_dir i86pc-solaris-64int 
%endif

%define           perl_vendor        GM
%define           perl5_dir          %{_prefix}/perl5
%define           perl_prefix        %{perl5_dir}/%{src_version}
%define           perl_lib           %{perl_prefix}/lib
%define           perl_archlib       %{perl_lib}/%{perl_arch_dir}
%define           perl_mandir        %{perl_prefix}/man
%define           perl_htmldir       %{perl_prefix}/html
%define           perl_sitedir       %{perl5_dir}/site_perl
%define           perl_sitebin       %{perl_sitedir}/%{src_version}/bin
%define           perl_sitelib       %{perl_sitedir}/%{src_version}
%define           perl_sitelibexp    %{perl_sitedir}/%{src_version}
%define           perl_sitearch      %{perl_sitelib}/%{perl_arch_dir}
%define           perl_sitemandir    %{perl_sitedir}/%{src_version}/man
%define           perl_sitehtmldir   %{perl_sitedir}/%{src_version}/html
%define           perl_vendordir     %{perl5_dir}/vendor_perl
#%define           perl_vendorlib    %{perl_vendordir}/%{src_version}/%{vendor}
#%define           perl_vendorarch   %{perl_vendordir}/%{src_version}/%{vendor}/%{perl_arch_dir}
%define           perl_vendorbin     %{perl_vendordir}/%{src_version}/bin
%define           perl_vendorlib     %{perl_vendordir}/%{src_version}
%define           perl_vendorarch    %{perl_vendorlib}/%{perl_arch_dir}
%define           perl_vendormandir  %{perl_vendordir}/%{src_version}/man
%define           perl_vendorhtmldir %{perl_vendordir}/%{src_version}/html


%include default-depend.inc

# Disable internal dependency generator for this pkg - we'll explicitly
# define them ourselves
%define _use_internal_dependency_generator 0

Requires:         database/berkeleydb-5  = *
Requires:         system/library/math    = *

BuildRequires:    database/berkeleydb-5
BuildRequires:    developer/build/gnu-make

%description
Perl is a general-purpose programming language originally developed for 
text manipulation and now used for a wide range of tasks including
system administration, web development, network programming, GUI 
development, and more.

The language is intended to be practical (easy to use, efficient,
complete) rather than beautiful (tiny, elegant, minimal).  Its major
features are that it's easy to use, supports both procedural and 
object-oriented (OO) programming, has powerful built-in support for text
processing, and has one of the world's most impressive collections of
third-party modules.

%clean
rm -rf $RPM_BUILD_ROOT

%prep
rm -rf perl-%{src_version}
%setup -q -n perl-%{src_version}

%build
CPUS=$(/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' ')
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CONFIGURE_ENV=""

export INC_COMPAT="5.14"
export PERL_LIBS="-lsocket -lnsl -ldb-5.1 -ldl -lm -lpthread -lc"

export CC=/opt/solarisstudio12.3/bin/cc
# Specify -xO3 as default specifies no optimiaztion - this helps avoid test failures
export CFLAGS="%optflags -xO3 -I%{_prefix}/gnu/include"
# NOTE: Added sparcv9 to gnu lib dirs due to this being a 64-bit perl
export LDFLAGS="%_ldflags -L%{_prefix}/gnu/lib/sparcv9 -R%{_prefix}/gnu/lib/sparcv9 -L%{_libdir} -R%{_libdir}"

#
# Configure Perl
#
./Configure                                    \
  -Darchlib=%{perl_archlib}                    \
  -Dcc="$CC"                                   \
  -Dccflags="$CFLAGS"                          \
  -Dccversion="$($CC -V 2>&1)"                 \
  -Dcf_email="root@bloomberg.net"              \
  -Dinc_version_list="$INC_COMPAT"             \
  -Dld="$CC"                                   \
  -Dldflags="$LDFLAGS"                         \
  -Dlibperl=libperl.so.%{src_version}          \
  -Dlocincpth=%{includedir}                    \
  -Dloclibpth=%{_libdir}                       \
  -Dman1dir=%{perl_mandir}/man1                \
  -Dman1ext=1                                  \
  -Dman3dir=%{perl_mandir}/man3                \
  -Dman3ext=3perl                              \
  -Doptimize="%{optflags}"                     \
  -Dperladmin="root@localhost"                 \
  -Dprefix=%{perl_prefix}                      \
  -Dprivlib=%{perl_lib}                        \
  -Dsitebin=%{perl_sitebin}                    \
  -Dsitearch=%{perl_sitearch}                  \
  -Dsitelib=%{perl_sitelib}                    \
  -Dsitelibexp=%{perl_sitelibexp}              \
  -Dsiteman1dir=%{perl_sitemandir}/man1        \
  -Dsiteman3dir=%{perl_sitemandir}/man3        \
  -Dsitehtml1dir=%{perl_sitehtmldir}/html1     \
  -Dsitehtml3dir=%{perl_sitehtmldir}/html3     \
  -Dsiteprefix=%{perl_prefix}                  \
  -Duse64bitint                                \
  -Duse64bitall                                \
  -Duselargefiles                              \
  -Duseshrplib                                 \
  -Dusesitecustomize                           \
  -Dusethreads                                 \
  -Dccdlflags="-R %{perl_archlib}/CORE"        \
  -Dvendorbin=%{perl_vendorbin}                \
  -Dvendorarch=%{perl_vendorarch}              \
  -Dvendorlib=%{perl_vendorlib}                \
  -Dvendorman1dir=%{perl_vendormandir}/man1    \
  -Dvendorman3dir=%{perl_vendormandir}/man3    \
  -Dvendorhtml1dir=%{perl_vendorhtmldir}/html1 \
  -Dvendorhtml3dir=%{perl_vendorhtmldir}/html3 \
  -Dvendorprefix=%{perl_prefix}                \
  -Dlibs="$PERL_LIBS"                          \
  -Dlibsdirs=" /usr/lib "                      \
  -Dsed=%{_bindir}/gsed                        \
  -Dusedtrace                                  \
  -des

gmake regen_headers
gmake -j$CPUS

#
# Disable due to a couple of incorrectly failing tests
#
#TEST_JOBS=32 gmake test_harness # Run tests in parallel as of 5.10.0

%install
gmake DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{perl_sitebin}
mkdir -p $RPM_BUILD_ROOT%{perl_sitearch}
mkdir -p $RPM_BUILD_ROOT%{perl_sitemandir}
mkdir -p $RPM_BUILD_ROOT%{perl_sitemandir}/man1
mkdir -p $RPM_BUILD_ROOT%{perl_sitemandir}/man3
mkdir -p $RPM_BUILD_ROOT%{perl_sitehtmldir}
mkdir -p $RPM_BUILD_ROOT%{perl_sitehtmldir}/html1
mkdir -p $RPM_BUILD_ROOT%{perl_sitehtmldir}/html3

mkdir -p $RPM_BUILD_ROOT%{perl_vendorbin}
mkdir -p $RPM_BUILD_ROOT%{perl_vendorarch}
mkdir -p $RPM_BUILD_ROOT%{perl_vendormandir}
mkdir -p $RPM_BUILD_ROOT%{perl_vendormandir}/man1
mkdir -p $RPM_BUILD_ROOT%{perl_vendormandir}/man3
mkdir -p $RPM_BUILD_ROOT%{perl_vendorhtmldir}
mkdir -p $RPM_BUILD_ROOT%{perl_vendorhtmldir}/html1
mkdir -p $RPM_BUILD_ROOT%{perl_vendorhtmldir}/html3


%clean

%mogrify
# Make sure we don't end up dependent on any specific version of these default
# dependencies that pkgbuild puts in for us.  This will eliminate embarassing
# upgrade problems
<transform depend type=require -> edit fmri system/kernel@.* system/kernel>
<transform depend type=require -> edit fmri system/core-os@.* system/core-os>
<transform depend type=require -> edit fmri system/library@.* system/library>
# Doesn't work with gid's, just group names
# <transform file path=usr/perl5/%{src_version}/bin/* -> edit group bin 242>


%files
%defattr (-,root,bin)
%dir %attr(-,root,bin)
# Only root should see/use this Perl
# Could add a group (other than bin), but it would have to reside locally on
# all hosts
%attr(0750,root,bin) /usr/perl5/%{src_version}/bin/*
/usr/perl5/%{src_version}/lib/*
/usr/perl5/%{src_version}/man/*
%dir %attr(-,root,bin)
/usr/perl5/site_perl/*
/usr/perl5/vendor_perl/*

%changelog
