%define snapshot 20200710
%define commit af2638fb6a1a1642a3b9b3320ca0ac352fdc0e78

Name:		plasma-dialer
Version:	1.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Camera app for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/plasma-camera/-/archive/master/plasma-camera-master.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(PkgConfig)

%description
Camera app for Plasma Mobile

%prep
%autosetup -p1 -n plasma-camera-master
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/plasma-camera
%{_datadir}/applications/org.kde.mobile.camera.desktop
%{_datadir}/metainfo/org.kde.mobile.camera.appdata.xml
