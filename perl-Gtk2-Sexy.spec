%define upstream_name	 Gtk2-Sexy
%define	upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	7

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.50.0-7
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-4
+ Revision: 702778
- rebuilt against libpng-1.5.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-3
+ Revision: 667188
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 564641
- rebuild for perl 5.12.1

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 409300
- rebuild using %%perl_convert_version

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.1
+ Revision: 320433
- update to new version 0.05

* Mon Sep 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
+ Revision: 278252
- update to new version 0.04

* Fri Jun 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.0
+ Revision: 218703
- update to new version 0.03

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.02-2mdv2008.1
+ Revision: 152112
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 0.02-1mdv2008.1
+ Revision: 135846
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jun 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2007.0
- New version 0.02
- spec cleanup
- fix directory ownership
- drop useless patch

* Tue Mar 21 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.01-3mdk
- Add BuildRequires

* Thu Mar 16 2006 Götz Waschk <waschk@mandriva.org> 0.01-2mdk
- fix buildrequires
- rebuild for new libsexy

* Wed Mar 15 2006 Olivier Blin <oblin@mandriva.com> 0.01-1mdk
- initial Mandriva release
- Patch0: fix bootstrap version

