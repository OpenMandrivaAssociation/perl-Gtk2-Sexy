%define modname	Gtk2-Sexy
%define	modver	0.05

Summary:	Perl interface to the sexy widget collection 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://www.chipx86.com/wiki/Libsexy
Source0:	http://www.cpan.org/modules/by-module/Gtk2/%{modname}-%{modver}.tar.bz2
BuildRequires:	perl-Cairo
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Glib
BuildRequires:	perl-Gtk2
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(libsexy)

%description
This module allows a perl developer to access the widgets of the sexy
widget collection, which currently includes the following widgets:
- SexyIconEntry:	a GtkEntry with support for inline icons
- SexySpellEntry:	a GtkEntry with inline spell checking
- SexyUrlLabel:	a GtkLabel with support for embedded hyperlinks

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc examples/*
%{perl_vendorarch}/Gtk2
%{perl_vendorarch}/auto/Gtk2
%{_mandir}/man3/*

