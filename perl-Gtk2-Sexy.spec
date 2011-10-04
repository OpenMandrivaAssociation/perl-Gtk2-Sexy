%define upstream_name	 Gtk2-Sexy
%define	upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Perl interface to the sexy widget collection 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.chipx86.com/wiki/Libsexy
Source0:	http://www.cpan.org/modules/by-module/Gtk2/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	libsexy-devel
BuildRequires:	perl-Cairo
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Glib
BuildRequires:	perl-Gtk2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module allows a perl developer to access the widgets of the sexy
widget collection, which currently includes the following widgets:
- SexyIconEntry: a GtkEntry with support for inline icons
- SexySpellEntry: a GtkEntry with inline spell checking
- SexyUrlLabel: a GtkLabel with support for embedded hyperlinks

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
