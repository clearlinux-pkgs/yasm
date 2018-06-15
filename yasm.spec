#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yasm
Version  : e256985c4929f4e550d8f70cad5fb936f81b7b06
Release  : 22
URL      : https://github.com/yasm/yasm/archive/e256985c4929f4e550d8f70cad5fb936f81b7b06.tar.gz
Source0  : https://github.com/yasm/yasm/archive/e256985c4929f4e550d8f70cad5fb936f81b7b06.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: yasm-bin
Requires: yasm-doc
BuildRequires : cmake
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : xmlto
Patch1: no-timestamp.patch

%description


%package bin
Summary: bin components for the yasm package.
Group: Binaries

%description bin
bin components for the yasm package.


%package dev
Summary: dev components for the yasm package.
Group: Development
Requires: yasm-bin
Provides: yasm-devel

%description dev
dev components for the yasm package.


%package doc
Summary: doc components for the yasm package.
Group: Documentation

%description doc
doc components for the yasm package.


%prep
%setup -q -n yasm-e256985c4929f4e550d8f70cad5fb936f81b7b06
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511056496
%autogen --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1511056496
rm -rf %{buildroot}
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
/usr/include/*.h
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man7/*
