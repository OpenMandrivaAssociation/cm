%define libmajor	0
%define libname		%mklibname %{name} %{libmajor}
%define libname_devel	%mklibname %{name} -d

Summary:	Ring class fields of imaginary quadratic number fields and of elliptic curves
Name:		cm
Version:	0.1
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.http://www.multiprecision.org/%{name}
Source0:	http://www.multiprecision.org/cm/download/%{name}-%{version}.tar.gz
BuildRequires:	libgmp-devel
BuildRequires:	libmpfr-devel
BuildRequires:	libmpc-devel
BuildRequires:	libmpfrcx-devel
BuildRequires:	ntl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Patch0:		cm-0.1-build.patch

%description
The CM software implements the construction of ring class fields of
imaginary quadratic number fields and of elliptic curves with complex
multiplication via floating point approximations. It consists of libraries
that can be called from within a C program and of executable command line
applications. For the implemented algorithms, see A. Enge, The complexity
of class polynomial computation via floating point approximations,
Mathematics of Computation 78 (266), 2009, pp. 1089-1107.

%package	-n %{libname}
Summary:	Arithmetic of complex numbers with arbitrarily high precision and correct rounding
Group:		System/Libraries

%description	-n %{libname}
The CM software implements the construction of ring class fields of
imaginary quadratic number fields and of elliptic curves with complex
multiplication via floating point approximations. It consists of libraries
that can be called from within a C program and of executable command line
applications. For the implemented algorithms, see A. Enge, The complexity
of class polynomial computation via floating point approximations,
Mathematics of Computation 78 (266), 2009, pp. 1089-1107.

%package	-n %{libname_devel}
Summary:	Development headers and libraries for CM
Group:		Development/C
Requires(post):	info-install
Requires(preun):info-install
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{libname_devel}
Development headers and libraries for CM.

%prep
%setup -q

%patch0 -p1

%build
autoreconf
%configure			\
	--enable-shared		\
	--disable-static

%make

%install
%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/%{name}
mv -f %{buildroot}%{_datadir}/{af,df} %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 0644 AUTHORS NEWS README %{buildroot}%{_docdir}/%{name}

%check
make check

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/classpol
%{_bindir}/cm
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files		-n %{libname}
%defattr(-,root,root)
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%{_libdir}/lib*.so.%{libmajor}*

%files		-n %{libname_devel}
%defattr(-,root,root)
%{_includedir}/*.h
%{_infodir}/cm.info*
%{_libdir}/lib*.la 
%{_libdir}/lib*.so
