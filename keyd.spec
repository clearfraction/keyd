Name:           keyd
Version:        2.4.3
Release:        0
Summary:        A key remapping daemon for Linux
License:        MIT
URL:            https://github.com/rvaiya/keyd
Source0:        https://github.com/rvaiya/keyd/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  pypi-python_xlib-python3
Provides: %{name} = %{version}-%{release}

%description
This is a VA-API implementation that uses VDPAU as a backend.

%prep
%setup -n %{name}-%{version}

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export LDFLAGS="-Wl,-rpath=/opt/3rd-party/bundles/clearfraction/usr/lib64,-rpath=/usr/lib64"
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
make %{?_smp_mflags}


%install
install -m755 -d %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}/layouts %{buildroot}%{_unitdir}
install -m755 bin/* %{buildroot}%{_bindir}
install -m644 data/keyd.compose %{buildroot}%{_datadir}/%{name}
install -m644 layouts/* %{buildroot}%{_datadir}/%{name}/layouts
install -D -m644 keyd.service -t %{buildroot}/usr/lib/systemd/user/
sed -i 's|/usr/bin/keyd|/opt/3rd-party/bundles/clearfraction/usr/bin/keyd|g' %{buildroot}/usr/lib/systemd/user/keyd.service


%files
/usr/bin/*
/usr/share/keyd/*
/usr/lib/systemd/user/keyd.service

%changelog
# based on https://github.com/clearfraction/gstreamer-libav
