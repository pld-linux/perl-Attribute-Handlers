#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Attribute
%define	pnam	Handlers
Summary:	Attribute::Handlers - simpler definition of attribute handlers
Summary(pl):	Attribute::Handlers - prostsze definiowanie programów obs³ugi atrybutów
Name:		perl-Attribute-Handlers
Version:	0.78
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c935f240bee1baf4b46e7d69bf2f1636
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Attribute/Handlers.pm
%{_mandir}/man3/*
