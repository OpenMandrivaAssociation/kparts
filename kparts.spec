%define major 5
%define libname %mklibname KF5Parts %{major}
%define devname %mklibname KF5Parts -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kparts
Version:	5.116.0
Release:	2
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Document centric plugin system
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)
# For QCH format docs
BuildRequires: qt5-assistant
BuildRequires: doxygen
Requires: %{libname} = %{EVRD}

%description
Document centric plugin system.

%package -n %{libname}
Summary: Document centric plugin system
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Document centric plugin system.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Parts library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Parts library.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_datadir}/kservicetypes5/*
%{_datadir}/kdevappwizard/templates/*
%{_libdir}/qt5/plugins/*.so
%{_datadir}/qlogging-categories5/kparts.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*.pri

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
