#
# spec file for package:  GMperl510
#
#
%include Solaris.inc
# %include arch64.inc

%define src_version 5.10.1
%define gm_version  %{src_version}.2

Name:             GMperl510
Summary:          Practical Extraction and Report Language
# Last dot version is our build of this pkg
Version:          %{gm_version}
License:          Artistic
Source:           http://www.cpan.org/src/perl-%{src_version}.tar.gz
Patch1:           perl-%{src_version}-change-inc.patch
SUNW_BaseDir:     %{_basedir}
SUNW_Copyright:   %{name}.copyright
BuildRoot:        %{_tmppath}/%{name}-%{src_version}-build
IPS_legacy:       false

# The prefix matches the one that Sun/Oracle has used for deployment of Perl
# over the years, and prevents any kind of collision with existing versions

#
# The architecture dir name is define, not based on the bit-ness of the perl
# binary itself, but on the bit length of the C int (integer) type
#
%ifarch sparc
%define perl_arch_dir sun4-solaris-64int
%else
%define perl_arch_dir i86pc-solaris-64int 
%endif

%define           perl_vendor     GM
%define           perl5_dir       %{_prefix}/perl5
%define           perl_prefix     %{perl5_dir}/%{src_version}
%define           perl_lib        %{perl_prefix}/lib
%define           perl_archlib    %{perl_lib}/%{perl_arch_dir}
%define           perl_mandir     %{perl_prefix}/man
%define           perl_htmldir     %{perl_prefix}/html

%define           perl_sitedir    %{perl5_dir}/site_perl
%define           perl_sitebin    %{perl_sitedir}/%{src_version}/bin
%define           perl_sitelib    %{perl_sitedir}/%{src_version}
%define           perl_sitearch   %{perl_sitelib}/%{perl_arch_dir}
%define           perl_sitemandir    %{perl_sitedir}/%{src_version}/man
%define           perl_sitehtmldir    %{perl_sitedir}/%{src_version}/html

%define           perl_vendordir  %{perl5_dir}/vendor_perl
#%define           perl_vendorlib  %{perl_vendordir}/%{version}/%{vendor}
#%define           perl_vendorarch %{perl_vendordir}/%{version}/%{vendor}/%{perl_arch_dir}
%define           perl_vendorbin  %{perl_vendordir}/%{src_version}/bin
%define           perl_vendorlib  %{perl_vendordir}/%{src_version}
%define           perl_vendorarch %{perl_vendorlib}/%{perl_arch_dir}
%define           perl_vendormandir  %{perl_vendordir}/%{src_version}/man
%define           perl_vendorhtmldir  %{perl_vendordir}/%{src_version}/html


%include default-depend.inc

Requires:         database/berkeleydb-5

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
%patch1 -p1

%build
CPUS=$(/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' ')
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CONFIGURE_ENV=""

export INC_COMPAT="5.8.0 5.8.2 5.8.4 5.8.6 5.8.7 5.8.8 5.10.0"
# export PERL_LIBS="-lsocket -lnsl -lgdbm -ldb-4.8 -ldl -lm -lpthread -lc -lperl"
export PERL_LIBS="-lsocket -lnsl -ldb-5.1 -ldl -lm -lpthread -lc"

export CC=/opt/solarisstudio12.3/bin/cc
export CFLAGS="%optflags -I%{_prefix}/gnu/include"
export LDFLAGS="%_ldflags -L%{_prefix}/gnu/lib -R%{_prefix}/gnu/lib -L%{_libdir} -R%{_libdir}"


# Configure Perl
# $CONFIGURE_ENV ./Configure             \
./Configure                             \
  -Darchlib=%{perl_archlib}             \
  -Dcc="$CC"                            \
  -Dccflags="$CFLAGS"                   \
  -Dccversion="%{CC_VERSION}"           \
  -Dcf_email="root@gmarler.com"       \
  -Dinc_version_list="$INC_COMPAT"      \
  -Dld="$CC"                            \
  -Dldflags="$LDFLAGS"                  \
  -Dlibperl=libperl.so.%{src_version}       \
  -Dlocincpth=%{includedir}             \
  -Dloclibpth=%{_libdir}                \
  -Dman1dir=%{perl_mandir}/man1         \
  -Dman1ext=1                           \
  -Dman3dir=%{perl_mandir}/man3         \
  -Dman3ext=3perl                       \
  -Doptimize="%{optflags}"              \
  -Dperladmin="root@localhost"          \
  -Dprefix=%{perl_prefix}               \
  -Dprivlib=%{perl_lib}                 \
  -Dsitebin=%{perl_sitebin}           \
  -Dsitearch=%{perl_sitearch}           \
  -Dsitelib=%{perl_sitelib}             \
  -Dsiteman1dir=%{perl_sitemandir}/man1     \
  -Dsiteman3dir=%{perl_sitemandir}/man3     \
  -Dsitehtml1dir=%{perl_sitehtmldir}/html1     \
  -Dsitehtml3dir=%{perl_sitehtmldir}/html3     \
  -Dsiteprefix=%{perl_prefix}           \
  -Duse64bitint                         \
  -Duselargefiles                       \
  -Duseshrplib                          \
  -Dusesitecustomize                    \
  -Dusethreads                          \
  -Dccdlflags="-R %{perl_archlib}/CORE" \
  -Dvendorbin=%{perl_vendorbin}       \
  -Dvendorarch=%{perl_vendorarch}       \
  -Dvendorlib=%{perl_vendorlib}         \
  -Dvendorman1dir=%{perl_vendormandir}/man1     \
  -Dvendorman3dir=%{perl_vendormandir}/man3     \
  -Dvendorhtml1dir=%{perl_vendorhtmldir}/html1     \
  -Dvendorhtml3dir=%{perl_vendorhtmldir}/html3     \
  -Dvendorprefix=%{perl_prefix}         \
  -Dlibs="$PERL_LIBS"                   \
  -Dlibsdirs=" /usr/lib "               \
  -Dsed=%{_bindir}/gsed                 \
  -des

gmake regen_headers
gmake -j$CPUS

# This takes a while...
# gmake test

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

