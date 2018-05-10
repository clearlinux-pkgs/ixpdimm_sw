#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ixpdimm_sw
Version  : 01.00.00.2460
Release  : 3
URL      : https://github.com/intel/ixpdimm_sw/archive/v01.00.00.2460.tar.gz
Source0  : https://github.com/intel/ixpdimm_sw/archive/v01.00.00.2460.tar.gz
Source1  : ixpdimm-monitor.service
Summary  : API for development of IXPDIMM management utilities
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0
Requires: ixpdimm_sw-bin
Requires: ixpdimm_sw-config
Requires: ixpdimm_sw-lib
Requires: ixpdimm_sw-data
Requires: ixpdimm_sw-doc
BuildRequires : cmake
BuildRequires : groff
BuildRequires : invm-frameworks-dev
BuildRequires : ndctl-dev
BuildRequires : numactl-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libkmod)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(zlib)
BuildRequires : python

%description
An application program interface (API) for configuring and managing

%package bin
Summary: bin components for the ixpdimm_sw package.
Group: Binaries
Requires: ixpdimm_sw-data
Requires: ixpdimm_sw-config

%description bin
bin components for the ixpdimm_sw package.


%package config
Summary: config components for the ixpdimm_sw package.
Group: Default

%description config
config components for the ixpdimm_sw package.


%package data
Summary: data components for the ixpdimm_sw package.
Group: Data

%description data
data components for the ixpdimm_sw package.


%package dev
Summary: dev components for the ixpdimm_sw package.
Group: Development
Requires: ixpdimm_sw-lib
Requires: ixpdimm_sw-bin
Requires: ixpdimm_sw-data
Provides: ixpdimm_sw-devel

%description dev
dev components for the ixpdimm_sw package.


%package doc
Summary: doc components for the ixpdimm_sw package.
Group: Documentation

%description doc
doc components for the ixpdimm_sw package.


%package lib
Summary: lib components for the ixpdimm_sw package.
Group: Libraries
Requires: ixpdimm_sw-data

%description lib
lib components for the ixpdimm_sw package.


%prep
%setup -q -n ixpdimm_sw-01.00.00.2460

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520550348
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_INSTALL_LIBDIR:PATH=lib64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DSBLIM-CMPI_INCLUDE_DIR=/usr/include/libinvm-cim
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1520550348
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/ixpdimm-monitor.service
## make_install_append content
mkdir -p %{buildroot}/usr/share/ixpdimm_sw/
mv %{buildroot}/var/lib/ixpdimm_sw/* %{buildroot}/usr/share/ixpdimm_sw/
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ixpdimm-cli
/usr/bin/ixpdimm-monitor

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/ixpdimm-monitor.service

%files data
%defattr(-,root,root,-)
/usr/share/ixpdimm_sw/apss.dat
/usr/share/ixpdimm_sw/public.rev0.pem

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libixpdimm-cim.so
/usr/lib64/libixpdimm-cli.so
/usr/lib64/libixpdimm-common.so
/usr/lib64/libixpdimm-core.so
/usr/lib64/libixpdimm.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libixpdimm-cim.so.1
/usr/lib64/libixpdimm-cim.so.1.0.0
/usr/lib64/libixpdimm-cli.so.1
/usr/lib64/libixpdimm-cli.so.1.0.0
/usr/lib64/libixpdimm-common.so.1
/usr/lib64/libixpdimm-common.so.1.0.0
/usr/lib64/libixpdimm-core.so.1
/usr/lib64/libixpdimm-core.so.1.0.0
/usr/lib64/libixpdimm.so.1
/usr/lib64/libixpdimm.so.1.0.0
