%define snapshot 20210401
%define commit 78c2e161c31b07be15f67c53bb556c3100a956b6

Name:		plasma-camera
Version:	2.1.1
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Camera app for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/plasma-camera/-/archive/v%{version}/plasma-camera-v%{version}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildSystem:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(PkgConfig)

%description
Camera app for Plasma Mobile

%files -f %{name}.lang
%{_bindir}/plasma-camera
%{_datadir}/applications/org.kde.plasma.camera.desktop
%{_datadir}/metainfo/org.kde.plasma.camera.appdata.xml
