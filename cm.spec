%define libmajor	1
%define libname		%mklibname %{name}
%define devname		%mklibname %{name} -d

Summary:	Ring class fields of imaginary quadratic number fields and of elliptic curves
Name:		cm
Version:	0.4.2
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		https://www.multiprecision.org/%{name}
Source0:	https://www.multiprecision.org/downloads/%{name}-%{version}.tar.gz
#Patch0:		cm-0.2-link.patch
Patch1:		cm-0.4.2-fix-tests.patch
BuildRequires:	pkgconfig(gmp) >= 4.3.2
BuildRequires:	pkgconfig(mpfr) >= 2.4.2
BuildRequires:	libmpc-devel >= 0.8.2
BuildRequires:	mpfrcx-devel >= 0.4
BuildRequires:	libpari-devel >= 2.5.1
BuildRequires:	ntl-devel
BuildRequires:	zlib-devel

%description
The CM software implements the construction of ring class fields of
imaginary quadratic number fields and of elliptic curves with complex
multiplication via floating point approximations. It consists of libraries
that can be called from within a C program and of executable command line
applications. For the implemented algorithms, see A. Enge, The complexity
of class polynomial computation via floating point approximations,
Mathematics of Computation 78 (266), 2009, pp. 1089-1107.

%package	-n %{libname}
Summary:	Arithmetic of complex numbers with arbitrarily high precision
Group:		System/Libraries

%description	-n %{libname}
The CM software implements the construction of ring class fields of
imaginary quadratic number fields and of elliptic curves with complex
multiplication via floating point approximations. It consists of libraries
that can be called from within a C program and of executable command line
applications. For the implemented algorithms, see A. Enge, The complexity
of class polynomial computation via floating point approximations,
Mathematics of Computation 78 (266), 2009, pp. 1089-1107.

%package	-n %{devname}
Summary:	Development headers and libraries for CM
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{devname}
Development headers and libraries for CM.

%prep
%autosetup -p1
autoreconf -if
%configure

%build
%make_build

%install
%make_install

%check
make check

%files
%{_bindir}/classpol
%{_bindir}/cm
%{_bindir}/ecpp
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/lib*.so.%{libmajor}*

%files -n %{devname}
%{_includedir}/*.h
%{_infodir}/cm.info*
%{_libdir}/lib*.so

