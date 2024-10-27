#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yasm
Version  : e256985c4929f4e550d8f70cad5fb936f81b7b06
Release  : 33
URL      : https://github.com/yasm/yasm/archive/e256985c4929f4e550d8f70cad5fb936f81b7b06.tar.gz
Source0  : https://github.com/yasm/yasm/archive/e256985c4929f4e550d8f70cad5fb936f81b7b06.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0-Perl BSD-2-Clause
Requires: yasm-bin = %{version}-%{release}
Requires: yasm-license = %{version}-%{release}
Requires: yasm-man = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : xmlto
Patch1: no-timestamp.patch
Patch2: 0001-Fix-compat-issues-with-autoconf-2.70.patch

%description


%package bin
Summary: bin components for the yasm package.
Group: Binaries
Requires: yasm-license = %{version}-%{release}

%description bin
bin components for the yasm package.


%package dev
Summary: dev components for the yasm package.
Group: Development
Requires: yasm-bin = %{version}-%{release}
Provides: yasm-devel = %{version}-%{release}
Requires: yasm = %{version}-%{release}

%description dev
dev components for the yasm package.


%package license
Summary: license components for the yasm package.
Group: Default

%description license
license components for the yasm package.


%package man
Summary: man components for the yasm package.
Group: Default

%description man
man components for the yasm package.


%prep
%setup -q -n yasm-e256985c4929f4e550d8f70cad5fb936f81b7b06
cd %{_builddir}/yasm-e256985c4929f4e550d8f70cad5fb936f81b7b06
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608109552
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1608109552
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yasm
cp %{_builddir}/yasm-e256985c4929f4e550d8f70cad5fb936f81b7b06/Artistic.txt %{buildroot}/usr/share/package-licenses/yasm/be0627fff2e8aef3d2a14d5d7486babc8a4873ba
cp %{_builddir}/yasm-e256985c4929f4e550d8f70cad5fb936f81b7b06/COPYING %{buildroot}/usr/share/package-licenses/yasm/4c46a1174c20e1d600ee083a1ef85ed7bbae2eb2
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vsyasm
/usr/bin/yasm
/usr/bin/ytasm

%files dev
%defattr(-,root,root,-)
/usr/include/libyasm-stdint.h
/usr/include/libyasm.h
/usr/include/libyasm/arch.h
/usr/include/libyasm/assocdat.h
/usr/include/libyasm/bitvect.h
/usr/include/libyasm/bytecode.h
/usr/include/libyasm/compat-queue.h
/usr/include/libyasm/coretype.h
/usr/include/libyasm/dbgfmt.h
/usr/include/libyasm/errwarn.h
/usr/include/libyasm/expr.h
/usr/include/libyasm/file.h
/usr/include/libyasm/floatnum.h
/usr/include/libyasm/hamt.h
/usr/include/libyasm/insn.h
/usr/include/libyasm/intnum.h
/usr/include/libyasm/inttree.h
/usr/include/libyasm/linemap.h
/usr/include/libyasm/listfmt.h
/usr/include/libyasm/md5.h
/usr/include/libyasm/module.h
/usr/include/libyasm/objfmt.h
/usr/include/libyasm/parser.h
/usr/include/libyasm/phash.h
/usr/include/libyasm/preproc.h
/usr/include/libyasm/section.h
/usr/include/libyasm/symrec.h
/usr/include/libyasm/valparam.h
/usr/include/libyasm/value.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/yasm/4c46a1174c20e1d600ee083a1ef85ed7bbae2eb2
/usr/share/package-licenses/yasm/be0627fff2e8aef3d2a14d5d7486babc8a4873ba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/yasm.1
/usr/share/man/man7/yasm_arch.7
/usr/share/man/man7/yasm_dbgfmts.7
/usr/share/man/man7/yasm_objfmts.7
/usr/share/man/man7/yasm_parsers.7
