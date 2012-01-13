#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Attribute
%define		pnam	Handlers
Summary:	Attribute::Handlers - simpler definition of attribute handlers
Summary(pl.UTF-8):	Attribute::Handlers - prostsze definiowanie programów obsługi atrybutów
Name:		perl-Attribute-Handlers
Version:	0.93
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Attribute/SMUELLER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5658992d2bc52ee5a5547425c1bec074
URL:		http://search.cpan.org/dist/Attribute-Handlers/
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

%description -l pl.UTF-8
Ten moduł pozwala klasom pakietu definiować podprogramy obsługi
atrybutów. Zmienne i podprogramy zdefiniowane w danym pakiecie lub
pakietach wywodzących się od pakietu mogą otrzymać atrybuty o tych
samych nazwach co podprogramy obsługi, które zostaną wywołane na końcu
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
%{_mandir}/man3/Attribute::Handlers.3pm*
