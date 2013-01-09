#
# spec file for package GMperl-5.16.2-CPAN
#
# Necessary config for root user to properly use CPAN - this file is
# kept at: /root/.cpan/CPAN/MyConfig.pm
#
# TODO: We're using CPANPLUS for this, so the below CPAN config won't be needed.
#
# Specify path to this config file via cpan's -j <filename> option on installs
# 
# NOTE: We use 2 variants of this file:
# - The first doesn't use a SQLite DB - have to have DBI module installed before
#   that will work
# - The second can use the SQLite DB, this usually speeds up the process
#
# $CPAN::Config = {
#   'applypatch' => q[],
#   'auto_commit' => q[0],
#   'build_cache' => q[100],
#   'build_dir' => q[/root/.cpan/build],
#   'build_dir_reuse' => q[0],
#   'build_requires_install_policy' => q[yes],
#   'bzip2' => q[/bin/bzip2],
#   'cache_metadata' => q[1],
#   'check_sigs' => q[0],
#   'colorize_output' => q[0],
#   'commandnumber_in_prompt' => q[1],
#   'connect_to_internet_ok' => q[1],
#   'cpan_home' => q[/root/.cpan],
#   'curl' => q[/bin/curl],
#   'ftp' => q[/bin/ftp],
#   'ftp_passive' => q[1],
#   'ftp_proxy' => q[http://myproxy.gmarler.com:80/],
#   'getcwd' => q[cwd],
#   'gpg' => q[],
#   'gzip' => q[/bin/gzip],
#   'halt_on_failure' => q[0],
#   'histfile' => q[/root/.cpan/histfile],
#   'histsize' => q[100],
#   'http_proxy' => q[http://myproxy.gmarler.com:80/],
#   'inactivity_timeout' => q[0],
#   'index_expire' => q[1],
#   'inhibit_startup_message' => q[0],
#   'keep_source_where' => q[/root/.cpan/sources],
#   'load_module_verbosity' => q[v],
#   'lynx' => q[],
#   'make' => q[/usr/bin/gmake],
#   'make_arg' => q[],
#   'make_install_arg' => q[INSTALLDIRS=site],
#   'make_install_make_command' => q[/usr/bin/gmake],
#   'makepl_arg' => q[],
#   'mbuild_arg' => q[],
#   'mbuild_install_arg' => q[--installdirs=site],
#   'mbuild_install_build_command' => q[./Build],
#   'mbuildpl_arg' => q[],
#   'ncftp' => q[],
#   'ncftpget' => q[],
#   'no_proxy' => q[],
#   'pager' => q[less],
#   'patch' => q[/usr/bin/gpatch],
#   'perl5lib_verbosity' => q[v],
#   'prefer_installer' => q[MB],
#   'prefs_dir' => q[/root/.cpan/prefs],
#   'prerequisites_policy' => q[follow],
#   'proxy_user' => q[],
#   'scan_cache' => q[atstart],
#   'shell' => q[/bin/ksh],
#   'show_unparsable_versions' => q[0],
#   'show_upload_date' => q[0],
#   'show_zero_versions' => q[0],
#   'tar' => q[/usr/bin/gtar],
#   'tar_verbosity' => q[v],
#   'term_is_latin' => q[1],
#   'term_ornaments' => q[1],
#   'test_report' => q[0],
#   'trust_test_report_history' => q[0],
#   'unzip' => q[/bin/unzip],
#   'urllist' => [q[file:///var/tmp/CPAN-20120204/], q[http://cpan.belfry.net/], q[http://cpan.binkerton.com/], q[http://cpan.mirror.facebook.com/]],
#   'use_sqlite' => q[0],
#   'wget' => q[/bin/wget],
#   'yaml_load_code' => q[0],
#   'yaml_module' => q[YAML],
# };
# 1;
# __END__

# 
# List of Modules to Install, in order:
# Modern::Perl
# CPAN::SQLite
# Pod::HTML
# Term::ReadKey
# YAML
# Digest::MD5
# Digest::SHA1
# Math::Pari - Manually, with libpari 2.3.5 (libpari 2.5.1 doesn't work as yet)
# Module::Signature (force install due to being unable to reach keyserver)
# Log::Dispatch::FileRotate
# Archive::Tar::Wrapper
# Perl::Tidy
# Perl::Critic
# Moo
# Dist::Zilla
# Dist::Zilla::Plugin::Git
# Dist::Zilla::Plugin::VersionFromScript
# Dist::Zilla::Plugin::VersionFromModule
# Dist::Zilla::Plugin::Version::Git::Flowish
# Dist::Zilla::Plugin::UploadToSFTP
# Dist::Zilla::Plugin::Test::ReportPrereqs
# Dist::Zilla::Plugin::Test::Portability
# Dist::Zilla::Plugin::Test::PodSpelling
# Dist::Zilla::Plugin::Test::Pod::LinkCheck
# Dist::Zilla::Plugin::Test::Perl::Critic
# Dist::Zilla::Plugin::Test::MinimumVersion
# Dist::Zilla::Plugin::Test::LocalBrew
# TODO:    Dist::Zilla::Plugin::Test::Kwalitee
# Dist::Zilla::Plugin::Test::Compile
# Dist::Zilla::Plugin::Test::CheckManifest
# Dist::Zilla::Plugin::Test::CheckDeps
# Dist::Zilla::Plugin::Test::CheckChanges
# Dist::Zilla::Plugin::Test::ChangesHasContent
# Dist::Zilla::Plugin::SurgicalPodWeaver
# Dist::Zilla::Plugin::Signature
# Dist::Zilla::Plugin::Rsync
# Dist::Zilla::Plugin::ReadmeFromPod
# Dist::Zilla::Plugin::PurePerlTests
# Dist::Zilla::Plugin::PerlTidy
# Dist::Zilla::Plugin::ModuleInstall
# Dist::Zilla::Plugin::MinimumPerl
# Dist::Zilla::Plugin::Inject
# Dist::Zilla::Plugin::GitObtain
# Dist::Zilla::Plugin::GitFlow::NextVersion
# Dist::Zilla::Plugin::GitFmtChanges
# FAILED: Dist::Zilla::Plugin::Git::ExcludeUntracked
#     Due to: Can't locate object method "list_files" via package"Archive::Tar::Wrapper"
# Dist::Zilla::Plugin::Git::DescribeVersion
# Dist::Zilla::Plugin::Git::Describe
# Dist::Zilla::Plugin::Catalyst
# Module::Starter
# Expect
# Number::Range
# Term::ReadLine::Perl
# Term::Size
# Test::Memory::Cycle
# Test::Class
# Test::Effects
# HTML::TreeBuilder
# HTML::Entities::Numbered
# CPAN::Mini
# force install IPC::Run
# IO::Socket::SSL
# NOTE: Test::WWW::Mechanize fails tests unless http_proxy is unset
# Catalyst::Devel
# Catalyst::View::TT
# Catalyst::View::JSON
# Catalyst::Plugin::Unicode
# XML::LibXML
# XML::DOM
# XML::Twig
# XML::XPath
# Archive::Tar
# Archive::Zip
# Date::Calc
# Excel::Writer::XLSX
# Storable
# force Net::Pcap
# IO::Prompt
# Text::Diff
# ExtUtils::ModuleMaker
# Readonly::XS
# CPANPLUS
# CatalystX::REPL
# Crypt::X509
# Crypt::CAST5
# Crypt::OpenSSL::AES
# Catalyst::Plugin::Session::Store::Memcached::Fast
# Catalyst::Plugin::Session::Store::FastMmap
# TODO:  Catalyst::Plugin::Session::Store::BerkeleyDB
# Catalyst::Plugin::Log::Log4perl
# Catalyst::Plugin::LogDeep
# Catalyst::Plugin::LogWarnings
# Object::Remote
# JSON::Diffable
# Web::Simple ????
# System::Introspector
#
# Graph::Directed
# SQL::Translator
# DateTime::Format::Strptime
# DateTime::Format::SQLite
# DateTime::Format::MySQL
# DateTime::Format::RFC3501
# DateTime::Format::RFC3339
# DateTime::Format::Natural
# DateTime::Format::ISO8601
# DateTime::Span
# DateTime::SpanSet
# DateTime::Set
# DateTime::Event::Recurrence
# NOTE: Following due to a bogus test failure
# force DBIx::Class
# DBIx::Class::DeploymentHandler
# Catalyst::Helper::Model::DBIC::Schema
# DBIx::Class::TimeStamp
# MLDBM
# AnyEvent
#
# To be done...
# Curses
# look curses
#  Alter this line: 'solaris'   => [ ''                       , '-L/usr/ccs/lib -lcurses' ],
#  to look like:    'solaris'   => [ '-I/usr/include/ncurses' , '-L/usr/gnu/lib -lncurses'],
#  Or (for 64-bit perl): 'solaris'   => [ '-I/usr/include/ncurses' , #  '-L/usr/gnu/lib/sparcv9 -lncurses'],
#  perl Makefile.PL PANELS MENUS FORMS
#  gmake install
#  exit
#
# ### Catalyst::Plugin::Prototype
#
# force install File::Fetch
# and then... CPAN 'upgrade' command
#
# export PATH=/usr/perl5/site_perl/5.16.1/bin:/usr/perl5/5.16.1/bin:$PATH
# export PATH=/opt/solarisstudio12.3/bin:$PATH
#
# pkgsend generate /usr/perl5/site_perl/5.16.1 > GMperlCPAN.p5m
# pkgdepend generate -md /usr/perl5/site_perl/5.16.1 \
#           GMperlCPAN.p5m > GMperlCPAN.p5m.1
#
# Create file "pathmod" with contents:
# <transform path=(^.+$) -> edit path .+ usr/perl5/site_perl/5.16.1/%<1>>
#
# pkgmogrify GMperlCPAN.p5m.1 pathmod > GMperlCPAN.p5m.2
#
# pkgdepend resolve -m GMperlCPAN.p5m.2
#
cat > GMperlCPAN.p5m.3 <<EOF
set name=pkg.fmri value=GMperl-5.16.1-CPAN@5.16.1.5.0,5.11-0.11.0
set name=pkg.summary value="CPAN modules compiled for GM Perl 5.16.1"
set name=pkg.description value="Provides multiple Perl CPAN modules in site_perl"
EOF

cat GMperlCPAN.p5m.2.res >> GMperlCPAN.p5m.3
# 
# Publish for SPARC:
# pkgsend -s http://${IPS_SERVER}/sparc-dev/ publish \
#         -d /usr/perl5/site_perl/5.16.1 \
#         GMperlCPAN.p5m.3
#
# Publish for x64:
# pkgsend -s http://${IPS_SERVER}/x86-dev/ publish \
#         -d /usr/perl5/site_perl/5.16.1 \
#         GMperlCPAN.p5m.3
#
#
# Merge two platforms (on njxs11be1), from this dir, as non-root user:
# ./merge.py -r -d /tmp/merge -v sparc,http://${IPS_SERVER}/sparc-dev/ \
#                             -v i386,http://${IPS_SERVER}/x86-dev/ arch GMperlCPAN
#
# And publish result to central repo:
#
# ./pkg_publish /tmp/merge/GMperlCPAN http://${IPS_SERVER}/all-dev/
#
# Rebuild the catalog on control:
# TODO: Make sure we're refreshing the right repo, the one we published to!
#       The one below *ISN'T* it - yet - fix that!
# root@control:/root# pkgrepo -s /export/ips-repos/GM rebuild
#
# Then sync control to kaos (using a preloaded SSH key in ssh-agent)...
#
%include Solaris.inc

Name:                    GMperl-5.16.1-CPAN
Summary:                 CPAN modules compiled for GM Perl 5.16.1
Version:                 5.16.1.0.0.1
# Source:                  http://
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

# libxml2, libexpat, libpcap
Requires:                GMperl-5.16.1
Requires:                library/libxml2
Requires:                library/libexpat
Requires:                system/library/libpcap
Requires:                library/gd
Requires:                database/sqlite-3

BuildRequires:           GMperl516
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

