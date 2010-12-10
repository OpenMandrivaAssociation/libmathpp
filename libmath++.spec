%define	version	0.0.4
%define release	%mkrel 2

%define major	0
%define libname %mklibname math++ %{major}

Summary:	C++ Math Type Library
Name:		libmath++
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		System/Libraries
# 16 Jun 2009 / incubusss
# upstream source no more available, suing the 0.0.4 tarball downloaded
# from Debian repository renamed to %{name}-%{version} and bz2 compressed
# http://ftp.de.debian.org/debian/pool/main/libm/libmath++/libmath++_0.0.4.orig.tar.gz
Source:		%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	doxygen

%description
%{name} is a template based math library, written in C++,
for symbolic and numeric calculus applications.


%package -n	%{libname}
Summary:	C++ Math Type Library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
%{name} is a template based math library, written in C++,
for symbolic and numeric calculus applications.


%package -n	%{libname}-devel
Summary:	Development related files for %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
%{name} is a template based math library, written in C++,
for symbolic and numeric calculus applications.

You need to install this package if you want to develop or compile
any applications/libraries that needs %{name}.

%prep
%setup -q

%build
autoreconf -f -i
%configure2_5x
%make
make api-doc

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING README
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc doc/user-api
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la

