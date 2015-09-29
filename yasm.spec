#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yasm
Version  : 1.3.0
Release  : 11
URL      : http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
Source0  : http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: yasm-bin
Requires: yasm-doc
BuildRequires : cmake
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : xmlto

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

%description dev
dev components for the yasm package.


%package doc
Summary: doc components for the yasm package.
Group: Documentation

%description doc
doc components for the yasm package.


%prep
%setup -q -n yasm-1.3.0

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%install
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
