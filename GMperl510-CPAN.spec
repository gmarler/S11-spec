#
# spec file for package BBperl510CPAN
# YAML
# Digest::MD5
# Digest::SHA1
# Expect
# Term::ReadKey
# Term::Size
# Test::Pod
# Test::Output
# Test::Memory::Cycle
# Tie::IxHash                                                                                   
# LWP
# CPAN::SQLite
# HTML::TreeBuilder
# HTML::Entities::Numbered
# CPAN::Mini
# IO::String
# PadWalker
# version
# IPC::Run3
# force install IPC::Run 
# IO::Socket::SSL
# Catalyst::Devel
# Catalyst::View::TT
# Catalyst::View::JSON
# Catalyst::Plugin::Unicode
# Catalyst::Model::Adaptor
# Catalyst::Controller::REST
# XML::LibXML
# XML::DOM
# XML::Twig
# XML::XPath
# Log::Dispatch
# Log::Dispatch::FileRotate
# Log::Log4perl
# Archive::Tar
# Archive::Zip
# Excel::Writer::XLSX
# Math::BigInt
# bignum
# Math::BigInt::FastCalc
# Math::BigRat
# Storable
# Date::Manip
# Date::Calc
# Net::Pcap
# Acme::LOLCAT
# Number::Bytes::Human
# Net::ISC::DHCPd
# IO::Prompt
# Text::Diff
# Perl::Tidy
# Perl::Critic
# CatalystX::REPL
#
# Crypt::Blowfish
# Crypt::CBC
# Crypt::DES
# Crypt::IDEA
# Crypt::Rijndael
#
# Crypt::X509
# Crypt::DSA
# Crypt::CAST5
# Crypt::OpenSSL::AES
#
# Catalyst::Plugin::Session::Store::Memcached::Fast
# Catalyst::Plugin::Session::Store::FastMmap
# Catalyst::Plugin::Session::Store::BerkeleyDB
# ### Catalyst::Plugin::Prototype
# Catalyst::Plugin::Log::Log4perl
# Catalyst::Plugin::LogDeep
# Catalyst::Plugin::LogWarnings
#
# DBIx::Class    
# SQL::Translator                                                                                                 
# DBIx::Class::DeploymentHandler
# DateTime::Format::Strptime
# DateTime::Format::SQLite
# DateTime::Format::MySQL
# Catalyst::Helper::Model::DBIC::Schema
# Catalyst::Helper::AuthDBIC
# DBIx::Class::TimeStamp
# Catalyst::Helper::Model::LDAP
# Catalyst::Helper::Prototype
# DBICx::TestDatabase
#
# Curses:
# look curses
#  Alter this line: 'solaris'   => [ ''                       , '-L/usr/ccs/lib -lcurses'   ],
#  to look like:    'solaris'   => [ '-I/usr/include/ncurses' , '-L/usr/gnu/lib -lncurses'   ],
#  perl Makefile.PL PANELS MENUS FORMS
#  gmake install
#  exit
#
# 
#
# force install File::Fetch
# and then... CPAN 'upgrade' command
#
# export PATH=/usr/perl5/5.10.1/bin:$PATH
#
# pkgsend generate /usr/perl5/site_perl/5.10.1 > BBperlCPAN.p5m
# pkgdepend generate -md /usr/perl5/site_perl/5.10.1 \
#           BBperlCPAN.p5m > BBperlCPAN.p5m.1
#
# Create file "pathmod" with contents:
# <transform path=(^.+$) -> edit path .+ usr/perl5/site_perl/5.10.1/%<1>>
#
# pkgmogrify BBperlCPAN.p5m.1 pathmod > BBperlCPAN.p5m.2
#
# pkgdepend resolve -m BBperlCPAN.p5m.2
#
cat > BBperlCPAN.p5m.3 <<EOF
set name=pkg.fmri value=BBperlCPAN@5.10.1.3,5.11-0.11.0
set name=pkg.summary value="CPAN modules compiled for BB Perl 5.10.1"
set name=pkg.description value="Provides multiple Perl CPAN modules in site_perl"
EOF
 
cat BBperlCPAN.p5m.2.res >> BBperlCPAN.p5m.3
# 
# Publish for SPARC:
# pkgsend -s http://njips1:18000/sysae-sparc-dev/ publish \
#         -d /usr/perl5/site_perl/5.10.1 \
#         BBperlCPAN.p5m.3
#
# Publish for x64:
# pkgsend -s http://njipst1:18000/sysae-x86-dev/ publish \
#         -d /usr/perl5/site_perl/5.10.1 \
#         BBperlCPAN.p5m.3
#
#
# Merge two platforms (on njxs11be1), from this dir, as non-root user:
# ./merge.py -r -d /tmp/merge -v sparc,http://njips1:18000/sysae-sparc-dev/ \
#                             -v i386,http://njips1:18000/sysae-x86-dev/ arch BBperlCPAN
#
# And publish result to central repo:
#
# ./pkg_publish /tmp/merge/BBperlCPAN http://njips1:18000/sysae-all-dev/
#
# Rebuild the catalog on njips1:
# TODO: Make sure we're refreshing the right repo, the one we published to!
#       The one below *ISN'T* it - yet - fix that!
# root@njips1:/root# pkgrepo -s /export/ips-repos/sysae rebuild
#
# Then sync njips1 to nyips1 (using a preloaded SSH key in ssh-agent)...
#





#
# spec file for package BBperl510-CPAN
# YAML
# Digest::MD5
# Digest::SHA1
# Expect
# Test::Pod
# Test::Output
# Tie::IxHash
# LWP
# HTML::TreeBuilder
# HTML::Entities::Numbered
# CPAN::Mini
# CPAN::SQLite
# IO::String
# PadWalker
# version
# IPC::Run3
# force install IPC::Run 
# Catalyst::Devel
# Catalyst::Helper::AuthDBIC
# XML::LibXML
# XML::DOM
# XML::Twig
# XML::XPath
# Log::Dispatch
# Log::Log4perl
# Archive::Tar
# Archive::Zip
# Excel::Writer::XLSX
# Math::BigInt
# bignum
# Math::BigInt::FastCalc
# Math::BigRat
# Storable
# Date::Manip
# Date::Calc
# Net::Pcap
# Test::Memory::Cycle
# Sub::Identify
# DateTime::Format:Strptime
#
# TODO:
# Catalyst::View::TT
# Catalyst::View::JSON
# Catalyst::Plugin::Unicode
# Catalyst::Model::Adaptor
#
# and then... CPAN 'upgrade' command
# force install File::Fetch
#
# pkgsend generate /usr/perl5/site_perl/5.10.1 > BBperlCPAN.p5m
# pkgdepend generate -md /usr/perl5/site_perl/5.10.1 \
#           BBperlCPAN.p5m > BBperlCPAN.p5m.1
#
# Create file "pathmod" with contents:
# <transform path=(^.+$) -> edit path .+ usr/perl5/site_perl/5.10.1/%<1>>
#
# pkgmogrify BBperlCPAN.p5m.1 pathmod > BBperlCPAN.p5m.2
#
# pkgdepend resolve -m BBperlCPAN.p5m.2 
# 
# Publish for x64:
# pkgsend -s http://njxs11be1:10000/ publish \
#         -d /usr/perl5/site_perl/5.10.1 \
#         BBperlCPAN@5.10.1.1 BBperlCPAN.p5m.2.res
#
# Publish for SPARC:
# pkgsend -s http://njxs11be1:20000/ publish \
#         -d /usr/perl5/site_perl/5.10.1 \
#         BBperlCPAN@5.10.1.1 BBperlCPAN.p5m.2.res
#
# includes module(s):
#
%include Solaris.inc
 
Name:                    BBperl510-CPAN
Summary:                 CPAN modules compiled for BB Perl 5.10.1
Version:                 5.10.1.1
# Source:                  http://
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

# libxml2, libexpat, libpcap
Requires:                BBperl510
Requires:                library/libxml2
Requires:                library/libexpat
Requires:                system/library/libpcap
Requires:                library/gd
Requires:                database/sqlite-3

BuildRequires:           BBperl510
BuildRequires:           SUNWgmake
BuildRequires:           library/libxml2
BuildRequires:           library/libexpat
BuildRequires:           system/library/libpcap
BuildRequires:           library/gd
BuildRequires:           database/sqlite-3

%description
Provides multiple Perl CPAN modules in site_perl

%include default-depend.inc

%prep


%build

cd %{module_name}-%{module_version_download}
%{perl} Makefile.PL \
    UNINST=0 \
    PREFIX=$RPM_BUILD_ROOT%{_prefix} \
    INSTALLSITELIB=$RPM_BUILD_ROOT%{perl_sitelib} \
    INSTALLSITEARCH=$RPM_BUILD_ROOT%{perl_sitearch} \
    INSTALLSITEMAN1DIR=$RPM_BUILD_ROOT%{perl_mandir}/man1 \
    INSTALLSITEMAN3DIR=$RPM_BUILD_ROOT%{perl_mandir}/man3 \
    INSTALLMAN1DIR=$RPM_BUILD_ROOT%{perl_mandir}/man1 \
    INSTALLMAN3DIR=$RPM_BUILD_ROOT%{perl_mandir}/man3

 
 gmake CC=$CC CCCDLFLAGS="%picflags" OPTIMIZE="%optflags" LD=$CC
  
%install
rm -rf $RPM_BUILD_ROOT
cd %{module_name}-%{module_version_download}
gmake test
gmake install
   
#remove:       /usr/lib/i86pc-solaris-64int/perllocal.pod
 rm -rf $RPM_BUILD_ROOT%{_prefix}/lib
    
     
%clean
rm -rf $RPM_BUILD_ROOT
      
%files
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{_prefix}/perl5
%dir %attr(0755, root, bin) %{perl_sitedir}
%dir %attr(0755, root, bin) %{perl_sitelib}
%{perl_sitelib}/*
%dir %attr(0755, root, bin) %{perl_mandir}
%dir %attr(0755, root, bin) %{perl_mandir}/man3
%{perl_mandir}/man3/*
       
        
%changelog
