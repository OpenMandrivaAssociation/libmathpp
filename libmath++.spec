%define	version	0.0.3
%define release	 %mkrel 2

%define major	0
%define libname %mklibname math++ %{major}

Summary:	C++ Math Type Library
Name:		libmath++
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
URL:		http://www.surakware.net/projects/%{name}/index.xml
Source:		%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.0.3-gcc34.patch.bz2
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
%patch0 -p1 -b .gcc34

%build
%configure2_5x
%make
make api-doc

%install
rm -rf %{buildroot}
%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

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

