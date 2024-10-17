Summary: An interthread communication library
Name: sigx
Version: 2.0.2
Release: %mkrel 3
License: LGPLv2+
Group: Sound
Source0: http://triendl.info/sigx/%{name}-%{version}.tar.bz2
BuildRequires: gtkmm2.4-devel
BuildRequires: libsigc++2.0-devel
BuildRequires: scons
BuildRequires: boost-devel
URL: https://triendl.info/sigx
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
An interthread communication library for c++ on top of libsigc++ and glibmm.

#---------------------------------------------------------------
%define major 2
%define libname %mklibname %name %major

%package -n %libname
Group: System/Libraries
Summary: Shared libraries for %name

%description -n %libname
This package contains shared libraries for %name.

%files -n %libname
%defattr(-, root, root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

#---------------------------------------------------------------
%define develname %mklibname %name -d

%package -n %develname
Group: System/Libraries
Summary: Development files for %name
Requires: %libname = %version
Provides: %name-devel = %version-%release

%description -n %develname
This package contains development files for %name.

%files -n %develname
%defattr(-, root, root)
%{_libdir}/*.so
%{_includedir}/sigx-2.0
%{_libdir}/sigx-2.0/sigxconfig.h
%{_libdir}/pkgconfig/*.pc

%prep
%setup -qn %{name}

sed -i -e 's#\/lib#\/%{_lib}#' SConstruct sigx.pc.in

%build
%setup_compile_flags
%scons PREFIX=%{_prefix}

%install
rm -rf %buildroot
%setup_compile_flags
%scons_install

%clean
rm -rf %buildroot
