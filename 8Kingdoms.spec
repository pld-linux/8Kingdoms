Summary:	8 Kingdoms is a 3D turn-based fantasy strategic game
Summary(hu.UTF-8):	8 Kingdoms egy 3D-s körökre osztott stratégiai játék
Summary(pl.UTF-8):	Strategiczna turowa gra 3D w świecie fantasy
Name:		8Kingdoms
Version:	1.1.0
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Games
# http://heanet.dl.sourceforge.net/sourceforge/kralovstvi/8Kingdoms-1.1.0.tar.gz
Source0:	http://dl.sourceforge.net/kralovstvi/%{name}-%{version}.tar.gz
# Source0-md5:	8409daf3d44e294dcfb50b85e87a3fa1
# Patch0:		%{name}-%{version}.patch
URL:		http://kralovstvi.sourceforge.net/index.php
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	expat-devel
BuildRequires:	sed >= 4.0
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
8 Kingdoms is a 3D turn-based fantasy strategic game in which players
become kings, build their empires and conquer enemy kingdoms.

%description -l hu.UTF-8
8 Kingdoms egy 3D-s körökre osztott stratégiai játék, amelyben a
játékosok királyokká válnak, felépítik a hatalmukat és meghóditják az
ellenséges birodalmakat.

%description -l pl.UTF-8
8 Kingdoms jest turową strategiczną grą w świecie fantasy z grafiką
3D. Gracze wcielają się w królów, budują swoje imperia i podbijają
wrogie królestwa.

%prep
%setup -q
# %patch0 -p1
%{__sed} -i "s,games,share," configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--datarootdir=%{_datadir}/%{name} \
	CPPFLAGS="-include limits.h -include string.h"
%{__sed} -i "s@pkgdatadir =.*@pkgdatadir = %{_datadir}/%{name}@" Makefile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}

%dir %{_datadir}/8Kingdoms/
%dir %{_datadir}/8Kingdoms/res/
%dir %{_datadir}/8Kingdoms/res/xml
%dir %{_datadir}/8Kingdoms/res/xml/languages
%dir %{_datadir}/8Kingdoms/res/xml/maps
%dir %{_datadir}/8Kingdoms/res/xml/units
%dir %{_datadir}/8Kingdoms/res/xml/scripts
%dir %{_datadir}/8Kingdoms/res/xml/scripts/ai
%dir %{_datadir}/8Kingdoms/res/xml/terrains
%dir %{_datadir}/8Kingdoms/res/xml/symbols
%dir %{_datadir}/8Kingdoms/res/xml/buildings
%dir %{_datadir}/8Kingdoms/res/xml/bonuses
%dir %{_datadir}/8Kingdoms/res/model
%dir %{_datadir}/8Kingdoms/res/model/units
%dir %{_datadir}/8Kingdoms/res/model/units/elf
%dir %{_datadir}/8Kingdoms/res/model/units/light_cavalry
%dir %{_datadir}/8Kingdoms/res/model/units/mage
%dir %{_datadir}/8Kingdoms/res/model/units/heavy_infantry
%dir %{_datadir}/8Kingdoms/res/model/units/dwarf
%dir %{_datadir}/8Kingdoms/res/model/units/spearman
%dir %{_datadir}/8Kingdoms/res/model/units/sappers
%dir %{_datadir}/8Kingdoms/res/model/units/archer_cavalry
%dir %{_datadir}/8Kingdoms/res/model/units/light_infantry
%dir %{_datadir}/8Kingdoms/res/model/units/archer
%dir %{_datadir}/8Kingdoms/res/model/units/catapult
%dir %{_datadir}/8Kingdoms/res/model/units/heavy_cavalry
%dir %{_datadir}/8Kingdoms/res/model/units/builder
%dir %{_datadir}/8Kingdoms/res/model/terrain
%dir %{_datadir}/8Kingdoms/res/model/buildings
%dir %{_datadir}/8Kingdoms/res/bitmap
%dir %{_datadir}/8Kingdoms/res/bitmap/units
%dir %{_datadir}/8Kingdoms/res/bitmap/effects
%dir %{_datadir}/8Kingdoms/res/bitmap/terrain
%dir %{_datadir}/8Kingdoms/res/bitmap/buildings
%dir %{_datadir}/8Kingdoms/res/sounds

%{_datadir}/8Kingdoms/res/*
%{_datadir}/8Kingdoms/res/xml/*
%{_datadir}/8Kingdoms/res/xml/languages/*
%{_datadir}/8Kingdoms/res/xml/maps/*
%{_datadir}/8Kingdoms/res/xml/units/*
%{_datadir}/8Kingdoms/res/xml/scripts/*
%{_datadir}/8Kingdoms/res/xml/scripts/ai/*
%{_datadir}/8Kingdoms/res/xml/terrains/*
%{_datadir}/8Kingdoms/res/xml/symbols/*
%{_datadir}/8Kingdoms/res/xml/buildings/*
%{_datadir}/8Kingdoms/res/xml/bonuses/*
%{_datadir}/8Kingdoms/res/model/*
%{_datadir}/8Kingdoms/res/model/units/*
%{_datadir}/8Kingdoms/res/model/units/elf/*
%{_datadir}/8Kingdoms/res/model/units/light_cavalry/*
%{_datadir}/8Kingdoms/res/model/units/mage/*
%{_datadir}/8Kingdoms/res/model/units/heavy_infantry/*
%{_datadir}/8Kingdoms/res/model/units/dwarf/*
%{_datadir}/8Kingdoms/res/model/units/spearman/*
%{_datadir}/8Kingdoms/res/model/units/sappers/*
%{_datadir}/8Kingdoms/res/model/units/archer_cavalry/*
%{_datadir}/8Kingdoms/res/model/units/light_infantry/*
%{_datadir}/8Kingdoms/res/model/units/archer/*
%{_datadir}/8Kingdoms/res/model/units/catapult/*
%{_datadir}/8Kingdoms/res/model/units/heavy_cavalry/*
%{_datadir}/8Kingdoms/res/model/units/builder/*
%{_datadir}/8Kingdoms/res/model/terrain/*
%{_datadir}/8Kingdoms/res/model/buildings/*
%{_datadir}/8Kingdoms/res/bitmap/*
%{_datadir}/8Kingdoms/res/bitmap/units/*
%{_datadir}/8Kingdoms/res/bitmap/effects/*
%{_datadir}/8Kingdoms/res/bitmap/terrain/*
%{_datadir}/8Kingdoms/res/bitmap/buildings/*
%{_datadir}/8Kingdoms/res/sounds/*
