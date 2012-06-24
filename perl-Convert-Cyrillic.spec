%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	Cyrillic
Summary:	Convert::Cyrillic perl module
Name:		perl-Convert-Cyrillic
Version:	1.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/Convert/cyrillic-%{version}.tar.gz
Source0:	cyrillic-%{version}.tar.gz
# Source0-md5:	d54ca5e24d2a7913862a8ce534f7ae74
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
All Russian WEB sites have to provide different encodings of Russian
texts. Four main encodings are CP1251 for Windows, KOI8 for UNIX, MAC
for Macintosh and transliteration for users accepting only English
texts.

This suite is intended for webmasters solving various issues related
to multiple charsets.

%prep
%setup -q -n cyrillic-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Convert/Cyrillic.pm
%{perl_vendorlib}/Convert/Cyrillic/Utils.pm
%{perl_vendorlib}/Lingua/DetectCharset.pm
%{perl_vendorlib}/Lingua/DetectCharset/StatKoi.pm
%{perl_vendorlib}/Lingua/DetectCharset/StatKoi8r.pm
%{perl_vendorlib}/Lingua/DetectCharset/StatKoi8u.pm
%{perl_vendorlib}/Lingua/DetectCharset/StatWin.pm
%{perl_vendorlib}/Lingua/DetectCharset/StatUtf8.pm
%{_mandir}/man3/*
