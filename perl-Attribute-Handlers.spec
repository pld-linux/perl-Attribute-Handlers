%include	/usr/lib/rpm/macros.perl
%define	pdir	Attribute
%define	pnam	Handlers
Summary:	Attribute::Handlers perl extension
Summary(pl):	Rozszerzenie perla: Attribute::Handlers
Name:		perl-Attribute-Handlers
Version:	0.76
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows that package's class to define attribute handler
subroutines for specific attributes. Variables and subroutines
subsequently defined in that package, or in packages derived from that
package may be given attributes with the same names as the attribute
handler subroutines, which will then be called at the end of the
compilation phase (i.e. in a `CHECK' block).

%description -l pl
Ten modu³ pozwala klasom pakietu definiowaæ podprogramy obs³ugi
atrybutów. Zmienne i podprogramy zdefiniowane w danym pakiecie lub
pakietach wywodz±cych siê od pakietu mog± otrzymaæ atrybuty o tych
samych nazwach co podprogramy obs³ugi, które zostan± wywo³ane na koñcu
fazy kompilacji (w bloku "CHECK").

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
