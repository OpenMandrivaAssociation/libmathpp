%define major	0
%define libname %mklibname math++ %{major}

Summary:	C++ Math Type Library
Name:		libmath++
Version:	0.0.4
Release:	4
License:	LGPLv2+
Group:		System/Libraries
# 16 Jun 2009 / incubusss
# upstream source no more available, suing the 0.0.4 tarball downloaded
# from Debian repository renamed to %{name}-%{version} and bz2 compressed
# http://ftp.de.debian.org/debian/pool/main/libm/libmath++/libmath++_0.0.4.orig.tar.gz
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	doxygen

%description
%{name} is a template based math library, written in C++,
for symbolic and numeric calculus applications.


%package -n	%{libname}
Summary:	C++ Math Type Library
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n	%{libname}
%{name} is a template based math library, written in C++,
for symbolic and numeric calculus applications.


%package -n	%{libname}-devel
Summary:	Development related files for %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{EVRD}
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
%makeinstall_std

%files -n %{libname}
%doc COPYING README
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%doc doc/user-api
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.4-2mdv2011.0
+ Revision: 620150
- the mass rebuild of 2010.0 packages

* Tue Jun 16 2009 Jérôme Brenier <incubusss@mandriva.org> 0.0.4-1mdv2010.0
+ Revision: 386428
- update to version 0.0.4
- use autoreconf
- drop gcc 3.4 patch
- fix license tag
- remove URL tag : upstream web site dead

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.0.3-2mdv2008.1
+ Revision: 128803
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import libmath++


* Fri Jun 04 2004 Abel Cheung <deaddog@deaddog.org> 0.0.3-2mdk
- P0: Temp fix for g++ 3.4

* Sat Nov 01 2003 Abel Cheung <deaddog@deaddog.org> 0.0.3-1mdk
- First Mandrake package
