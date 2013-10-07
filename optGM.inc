#==============================================================================
# ---- Custom macros
#
#
%__install              /usr/gnu/bin/install
%__id_u                 /usr/xpg4/bin/id -u

#==============================================================================
# ---- Studio Compiler specific macros
#
#
%__cc                   /opt/solarisstudio12.3/bin/cc
%__cxx                  /opt/solarisstudio12.3/bin/CC
%__make                 /usr/gnu/bin/make

#==============================================================================
# ---- configure macros.
#       Macro(s) slavishly copied from autoconf's config.status.
#
%_prefix                /opt/GM
%_exec_prefix           %{_prefix}
%_bindir                %{_exec_prefix}/bin
%_sbindir               %{_exec_prefix}/sbin
%_libexecdir            %{_exec_prefix}/libexec
%_datadir               %{_prefix}/share
%_sysconfdir            %{_prefix}/etc
%_sharedstatedir        %{_prefix}/com
%_localstatedir         %{_prefix}/var
%_lib                   /opt/GM/lib
%_libdir                %{_exec_prefix}/%{_lib}
%_includedir            %{_prefix}/include
%_oldincludedir         /opt/GM/include
%_infodir               %{_datadir}/info
%_mandir                %{_datadir}/man
%_docdir                %{_datadir}/doc
%_pkg_docdir            %{_docdir}/%{name}
%_javadir               %{_datadir}/java
%_global_cflags         -xO3 -g -xtarget=generic
%optflags               %{_global_cflags}
%cxx_optflags           -xO3 -g0 -xtarget=generic

#==============================================================================
# ---- specfile macros - reproduced here to ensure they overwrite what may have
#                        been previously set
#       Macro(s) here can be used reliably for reproducible builds.
#       (Note: Above is the goal, below are the macros under development)
#
# The configure macro does the following:
#       optionally change to a subdirectory (not implemented).
#       attempt to update config.guess and config.sub.
#       run configure with correct prefix, platform, and CFLAGS.
#       optionally restore current directory (not implemented).
# The configure macro should be invoked as %configure (rather than %{configure})
# because the rest of the arguments will be expanded using %*.
#
#------------------------------------------------------------------------------
# This is an improved version of %configure (from PLD team).
%configure \
  CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
  CXXFLAGS="${CXXFLAGS:-%cxx_optflags}" ; export CXXFLAGS ; \
  FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ; \
  ./configure --host=%{_host} --build=%{_build} \\\
        --target=%{_target_platform} \\\
        --program-prefix=%{?_program_prefix} \\\
        --prefix=%{_prefix} \\\
        --exec-prefix=%{_exec_prefix} \\\
        --bindir=%{_bindir} \\\
        --sbindir=%{_sbindir} \\\
        --sysconfdir=%{_sysconfdir} \\\
        --datadir=%{_datadir} \\\
        --includedir=%{_includedir} \\\
        --libdir=%{_libdir} \\\
        --libexecdir=%{_libexecdir} \\\
        --localstatedir=%{_localstatedir} \\\
        --sharedstatedir=%{_sharedstatedir} \\\
        --mandir=%{_mandir} \\\
        --infodir=%{_infodir}

#------------------------------------------------------------------------------
# The make install analogue of %configure:
%makeinstall \
  make \\\
        prefix=%{?buildroot:%{buildroot}}%{_prefix} \\\
        exec_prefix=%{?buildroot:%{buildroot}}%{_exec_prefix} \\\
        bindir=%{?buildroot:%{buildroot}}%{_bindir} \\\
        sbindir=%{?buildroot:%{buildroot}}%{_sbindir} \\\
        sysconfdir=%{?buildroot:%{buildroot}}%{_sysconfdir} \\\
        datadir=%{?buildroot:%{buildroot}}%{_datadir} \\\
        includedir=%{?buildroot:%{buildroot}}%{_includedir} \\\
        libdir=%{?buildroot:%{buildroot}}%{_libdir} \\\
        libexecdir=%{?buildroot:%{buildroot}}%{_libexecdir} \\\
        localstatedir=%{?buildroot:%{buildroot}}%{_localstatedir} \\\
        sharedstatedir=%{?buildroot:%{buildroot}}%{_sharedstatedir} \\\
        mandir=%{?buildroot:%{buildroot}}%{_mandir} \\\
        infodir=%{?buildroot:%{buildroot}}%{_infodir} \\\
  install

%pkgbuild_postprocess	%__pkgbuild_libdir/pkgbuild-postprocess
%find_lang		echo WARNING: find_lang not implemented
%_invalid_patches_terminate_build 1
