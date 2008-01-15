%define module	Gtk2-Sexy
%define	name	perl-%{module}
%define	version	0.02
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface to the sexy widget collection 
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.chipx86.com/wiki/Libsexy
Source:		http://www.cpan.org/modules/by-module/Gtk2/%{module}-%{version}.tar.bz2
BuildRequires:	libsexy-devel
BuildRequires:	perl-devel
BuildRequires:	perl-Glib
BuildRequires:	perl-Cairo
BuildRequires:	perl-Gtk2
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module allows a perl developer to access the widgets of the sexy
widget collection, which currently includes the following widgets:
- SexyIconEntry: a GtkEntry with support for inline icons
- SexySpellEntry: a GtkEntry with inline spell checking
- SexyUrlLabel: a GtkLabel with support for embedded hyperlinks

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc examples/*
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2
%{perl_vendorarch}/auto/Gtk2

