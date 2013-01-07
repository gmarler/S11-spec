#!/bin/ksh
#
#
print -- "Setting up pkgbuild environment - please wait..."
pkgbuild_version=$(/opt/pkgbuild/bin/pkgbuild --version | head -1)
print -- "${pkgbuild_version}"

myarch=$(/bin/uname -p)
if [[ $myarch == "i386" ]]; then
  myarch=x86
fi

save_IFS="$IFS"
IFS=" 
"
ENV_SET=$(/bin/env | grep '^[a-zA-Z0-9_]*=' | cut -f1 -d=)
if [[ "x$ZSH_VERSION" != x ]]; then
  set -o sh_word_split
else
  for var in $ENV_SET; do
    case $var in
      HISTSIZE|LANG|PS1|PS2|HZ|TERM|SHELL|OLDPWD|PATH|MAIL|PWD|TZ|SHLVL|HOME|LOGNAME|PRINTER|HOSTNAME|_|CC|CXX|EDITOR|SSH_*|DISPLAY|LESS*|LS_COLORS|LS_OPTIONS|TERMINFO|PAGER|MANPATH|VISUAL|XAUTHORITY|CVSROOT|CVS_RSH|DBUS_*|SESSION_MANAGER|JDS_CBE_ENV_QUIET|PKGBUILD_IPS_SERVER)
        ;;
      *)
        test "x$JDS_CBE_ENV_QUIET" != x1 && echo Unsetting $var
        unset $var
        ;;
    esac
  done
fi

IFS="$save_IFS"

CBE_PREFIX=/opt/pkgbuild

invalid_env=no

# Build environment config file for the Desktop CBE
CC_name='Solaris Studio'
CC_version='5.12'
CC_release='Ceres'
CC_rev='cc: Sun C 5.12 SunOS Patch 148918-01 2012/05/08'
cc_dir='/opt/solarisstudio12.3/bin'
CC='/opt/solarisstudio12.3/bin/cc'
CXX='/opt/solarisstudio12.3/bin/CC'


if [[ $invalid_env != yes ]]; then
  # backward compat with old JDS CBEs:
  CC32="$CC"
  CC64="$CC"
  CXX32="$CXX"
  CXX64="$CXX"
  export CC32 CC64 CXX32 CXX64

  if [[ "x$JDS_CBE_ENV_QUIET" != x1 ]]; then
    print -- "Using CC=$CC"
    print -- "Using CXX=$CXX"
  fi

  CCDIR=$(/bin/dirname $CC)
  if [[ $CCDIR != /usr/bin ]]; then
    PATH="$CBE_PREFIX/bin:$CCDIR:/usr/ccs/bin:/usr/gnu/bin:/usr/bin:/usr/sbin:/bin:/usr/sfw/bin"
  else
    PATH="$CBE_PREFIX/bin:/usr/ccs/bin:/usr/gnu/bin:/usr/bin:/usr/sbin:/bin:/usr/sfw/bin"
  fi

  test "x$JDS_CBE_ENV_QUIET" != x1  && \
    print -- "Setting PATH=$PATH"
  export PATH

  CONFIG_SHELL="/bin/ksh"
  test "x$JDS_CBE_ENV_QUIET" != x1  && \
    print -- "Setting CONFIG_SHELL=$CONFIG_SHELL"
  export CONFIG_SHELL

  MAKESHELL="/bin/ksh"
  test "x$JDS_CBE_ENV_QUIET" != x1  && \
    print -- "Setting MAKESHELL=$MAKESHELL"
  export MAKESHELL

  MAKE="/usr/gnu/bin/make"
  test "x$JDS_CBE_ENV_QUIET" != x1  && \
    print -- "Setting MAKE=$MAKE"
  export MAKE

  M4="/usr/gnu/bin/m4"
  test "x$JDS_CBE_ENV_QUIET" != x1  && \
    print -- "Setting M4=$M4"
  export M4
fi

bash_opts="--norc --noprofile"
ksh_opts="-p"
ksh93_opts="-p"
csh_opts="-f"
tcsh_opts="-f"

subshell=${SHELL:-/bin/bash}
subshell_name=`basename $subshell`
eval subshell_opts='"$'${subshell_name}_opts'"'

# start a subshell if the script is directly executed, or if the
# shell is zsh.  (with zsh, it's not possible to tell if the script
# is being sourced or executed, or at least I couldn't figure out
# how)
if [[ x`/bin/basename $0` == xenv.sh ]]; then
  if [[ $invalid_env == no ]]; then
    if [[ "x$ZSH_VERSION" == x ]]; then
      print -- "Starting subshell $subshell $subshell_opts"
      exec $subshell $subshell_opts
    else
      print -- "Starting subshell $subshell $subshell_opts"
      $subshell $subshell_opts
    fi
  else
    /bin/false
  fi
else
  # set return value
  test $invalid_env != yes
fi


