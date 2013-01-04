#
# spec file for package:  GMperl-5.16.2
#
# NOTE: Please, please, make sure /usr/gnu/bin isn't in your path
#       when you build this/set it up.  Perl doesn't seem to like this on
#       the Solaris 11 platform that much.
# ALSO: Make sure the Studio 12.3 compiler is already in your path when you
#       run pkgtool on this.
#

%define major       5
%define minor       16
%define patch       2
%define src_version %{major}.%{minor}.%{patch}
%define my_version  %{src_version}.0

Name:             GMperl-%{major}-%{minor}-%{patch}
Summary:          Practical Extraction and Report Language
# Last dot version is our build of this pkg
Version:          %{my_version}
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

# NOTE: Since this is 64-bit perl, we can simply use the new arch dir of 64,
#       rather than the arch specific sparcv9 or amd64
%define arch_dir 64

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


# %include default-depend.inc

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
# NOTE: %optflags is currently dangerous, as it seems to assume gcc - have
#       removed it from both CFLAGS and -Doptimize
export CFLAGS="-xO3 -I%{_prefix}/gnu/include"
# TODO: This *might* cause problems later for us, as it shows up automatically
# in lddlflags:
#  -L/opt/solarisstudio12.3/prod/lib/amd64
export LDFLAGS="-L%{_prefix}/gnu/lib/%{arch_dir} -R%{_prefix}/gnu/lib/%{arch_dir} -L%{_libdir} -R%{_libdir}"
# TESTED: This may prevent the Embed.t test from failing - it doesn't - that
# test is definitely broken:
# 
# export LD_LIBRARY_PATH=%{_builddir}

#
# Configure Perl
#
./Configure                             \
  -Darchlib=%{perl_archlib}             \
  -Dcc="$CC"                            \
  -Dccflags="$CFLAGS"                   \
  -Dccversion="$($CC -V 2>&1)"          \
  -Dcf_email="root@gmarler.com"         \
  -Dinc_version_list="$INC_COMPAT"      \
  -Dld="$CC"                            \
  -Dldflags="$LDFLAGS"                  \
  -Dlibperl=libperl.so.%{src_version}   \
  -Dlocincpth=%{includedir}             \
  -Dloclibpth=%{_libdir}                \
  -Dman1dir=%{perl_mandir}/man1         \
  -Dman1ext=1                           \
  -Dman3dir=%{perl_mandir}/man3         \
  -Dman3ext=3perl                       \
  -Doptimize="-xO3"                     \
  -Dperladmin="root@localhost"          \
  -Dprefix=%{perl_prefix}                      \
  -Dprivlib=%{perl_lib}                        \
  -Dsitebin=%{perl_sitebin}                    \
  -Dsitearch=%{perl_sitearch}                  \
  -Dsitelib=%{perl_sitelib}                    \
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
  -Dccdlflags="-L%{perl_archlib}/CORE -R%{perl_archlib}/CORE"         \
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
TEST_JOBS=32 gmake test_harness # Run tests in parallel as of 5.10.0

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

%files
%defattr (-,root,bin)
%dir %attr(-,root,bin)
/usr/perl5/%{src_version}/*
%dir %attr(-,root,bin)
/usr/perl5/site_perl/*
/usr/perl5/vendor_perl/*

%changelog

