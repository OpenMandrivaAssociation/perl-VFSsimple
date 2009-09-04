%define module	VFSsimple
%define name	perl-%{module}
%define version	0.03
%define release	%mkrel 5

Summary:	A library to magically access to file w/o carry the method
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	WTFPL
Group:		Development/Perl
Requires:	perl
URL:		http://nanardon.zarb.org/darcsweb/darcsweb.cgi?r=VFSsimple;a=summary
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBI/%{module}-%{version}.tar.gz
BuildRequires:	perl(URI)
BuildArch: noarch

Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A library to magically access to file w/o carry the method

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make CFLAGS="%{optflags}"

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/*
%{perl_vendorlib}/*
%{_mandir}/*/*
