Summary:	Workspace manager for GNUstep
Summary(pl):	Zarz±dca biurek dla GNUstepa
Name:		GWorkspace
Version:	0.6.5
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://www.gnustep.it/enrico/gworkspace/gworkspace-%{version}.tar.gz
# Source0-md5:	bef75bb09fc11b7c437bfe8abeb0c602
Patch0:		%{name}-link.patch
URL:		http://www.gnustep.it/enrico/gworkspace/
BuildRequires:	gnustep-gui-devel >= 0.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%define		gstriple	%{gscpu}/%{gsos}/%{libcombo}
%define		gsservicedir	%{_prefix}/System/Library/Services

%description
GWorkspace is a workspace and file manager for GNUstep.

%description -l pl
GWorkspace to zarz±dca biurek i plików dla GNUstepa.

%package devel
Summary:	Header files for GWorkspace
Summary(pl):	Pliki nag³ówkowe GWorkspace
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GWorkspace.

%description devel -l pl
Pliki nag³ówkowe GWorkspace.

%prep
%setup -q
%patch0 -p1

find . -type d -name CVS | xargs rm -rf

%build
%configure
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	debug=no \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install debug=no \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO 

%dir %{_prefix}/System/Applications/Desktop.app
%attr(755,root,root) %dir %{_prefix}/System/Applications/Desktop.app/Desktop
%dir %{_prefix}/System/Applications/Desktop.app/Resources
%{_prefix}/System/Applications/Desktop.app/Resources/*.desktop
%{_prefix}/System/Applications/Desktop.app/Resources/*.plist
%{_prefix}/System/Applications/Desktop.app/Resources/*.tiff
%{_prefix}/System/Applications/Desktop.app/Resources/English.lproj
%dir %{_prefix}/System/Applications/Desktop.app/%{gscpu}
%dir %{_prefix}/System/Applications/Desktop.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Desktop.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Desktop.app/%{gstriple}/Desktop
%{_prefix}/System/Applications/Desktop.app/%{gstriple}/*.openapp

%dir %{_prefix}/System/Applications/Finder.app
%attr(755,root,root) %dir %{_prefix}/System/Applications/Finder.app/Finder
%dir %{_prefix}/System/Applications/Finder.app/Resources
%{_prefix}/System/Applications/Finder.app/Resources/*.desktop
%{_prefix}/System/Applications/Finder.app/Resources/*.plist
%{_prefix}/System/Applications/Finder.app/Resources/*.tiff
%{_prefix}/System/Applications/Finder.app/Resources/English.lproj
%dir %{_prefix}/System/Applications/Finder.app/Resources/*.finder
%{_prefix}/System/Applications/Finder.app/Resources/*.finder/Resources
%attr(755,root,root) %{_prefix}/System/Applications/Finder.app/Resources/*.finder/%{gscpu}
%dir %{_prefix}/System/Applications/Finder.app/%{gscpu}
%dir %{_prefix}/System/Applications/Finder.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Finder.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Finder.app/%{gstriple}/Finder
%{_prefix}/System/Applications/Finder.app/%{gstriple}/*.openapp

%dir %{_prefix}/System/Applications/GWorkspace.app
%attr(755,root,root) %{_prefix}/System/Applications/GWorkspace.app/GWorkspace
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.desktop
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.plist
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.tiff
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.gorm
%lang(nl) %{_prefix}/System/Applications/GWorkspace.app/Resources/Dutch.lproj
%{_prefix}/System/Applications/GWorkspace.app/Resources/English.lproj
%lang(fr) %{_prefix}/System/Applications/GWorkspace.app/Resources/French.lproj
%lang(de) %{_prefix}/System/Applications/GWorkspace.app/Resources/German.lproj
%lang(it) %{_prefix}/System/Applications/GWorkspace.app/Resources/Italian.lproj
%lang(pt) %{_prefix}/System/Applications/GWorkspace.app/Resources/Portuguese.lproj
%lang(ro) %{_prefix}/System/Applications/GWorkspace.app/Resources/Romanian.lproj
%lang(es) %{_prefix}/System/Applications/GWorkspace.app/Resources/Spanish.lproj
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/Resources
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/Resources/*.gorm
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/Resources/*.plist
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/Resources/*.tiff
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/Resources/English.lproj
%attr(755,root,root) %{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/%{gscpu}
%dir %{_prefix}/System/Applications/GWorkspace.app/%{gscpu}
%dir %{_prefix}/System/Applications/GWorkspace.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/GWorkspace.app/%{gstriple}
%attr(755,root,root) %{_prefix}/System/Applications/GWorkspace.app/%{gstriple}/GWorkspace
%{_prefix}/System/Applications/GWorkspace.app/%{gstriple}/*.openapp

%dir %{_prefix}/System/Applications/Inspector.app
%attr(755,root,root) %dir %{_prefix}/System/Applications/Inspector.app/Inspector
%dir %{_prefix}/System/Applications/Inspector.app/Resources
%{_prefix}/System/Applications/Inspector.app/Resources/*.desktop
%{_prefix}/System/Applications/Inspector.app/Resources/*.plist
%{_prefix}/System/Applications/Inspector.app/Resources/*.tiff
%{_prefix}/System/Applications/Inspector.app/Resources/English.lproj
%dir %{_prefix}/System/Applications/Inspector.app/Resources/*.inspector
%{_prefix}/System/Applications/Inspector.app/Resources/*.inspector/Resources
%attr(755,root,root) %{_prefix}/System/Applications/Inspector.app/Resources/*.inspector/%{gscpu}
%dir %{_prefix}/System/Applications/Inspector.app/%{gscpu}
%dir %{_prefix}/System/Applications/Inspector.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Inspector.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Inspector.app/%{gstriple}/Inspector
%{_prefix}/System/Applications/Inspector.app/%{gstriple}/*.openapp

%dir %{_prefix}/System/Applications/Operation.app
%attr(755,root,root) %dir %{_prefix}/System/Applications/Operation.app/Operation
%dir %{_prefix}/System/Applications/Operation.app/Resources
%{_prefix}/System/Applications/Operation.app/Resources/*.desktop
%{_prefix}/System/Applications/Operation.app/Resources/*.plist
%{_prefix}/System/Applications/Operation.app/Resources/*.tiff
%{_prefix}/System/Applications/Operation.app/Resources/English.lproj
%dir %{_prefix}/System/Applications/Operation.app/%{gscpu}
%dir %{_prefix}/System/Applications/Operation.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Operation.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Operation.app/%{gstriple}/Operation
%{_prefix}/System/Applications/Operation.app/%{gstriple}/*.openapp

%dir %{_prefix}/System/Library/Bundles/*.inspector
%attr(755,root,root) %{_prefix}/System/Library/Bundles/*.inspector/%{gscpu}
%{_prefix}/System/Library/Bundles/*.inspector/Resources
%dir %{_prefix}/System/Library/Bundles/*.finder
%{_prefix}/System/Library/Bundles/*.finder/Resources
%attr(755,root,root) %{_prefix}/System/Library/Bundles/*.finder/%{gscpu}
%dir %{_prefix}/System/Library/Bundles/*.thumb
%{_prefix}/System/Library/Bundles/*.thumb/Resources
%attr(755,root,root) %{_prefix}/System/Library/Bundles/*.thumb/%{gscpu}
%dir %{_prefix}/System/Library/Bundles/*.viewer
%dir %{_prefix}/System/Library/Bundles/*.viewer/Resources
%{_prefix}/System/Library/Bundles/*.viewer/Resources/*.plist
%{_prefix}/System/Library/Bundles/*.viewer/Resources/*.tiff
%{_prefix}/System/Library/Bundles/*.viewer/Resources/English.lproj
%attr(755,root,root) %{_prefix}/System/Library/Bundles/*.viewer/%{gscpu}

%dir %{_prefix}/System/Library/Frameworks/FSNode.framework
%{_prefix}/System/Library/Frameworks/FSNode.framework/Resources
%dir %{_prefix}/System/Library/Frameworks/FSNode.framework/Versions
%{_prefix}/System/Library/Frameworks/FSNode.framework/Versions/Current
%dir %{_prefix}/System/Library/Frameworks/FSNode.framework/Versions/A
%{_prefix}/System/Library/Frameworks/FSNode.framework/Versions/A/Resources/*.plist
%{_prefix}/System/Library/Frameworks/FSNode.framework/Versions/A/Resources/*.tiff
%{_prefix}/System/Library/Frameworks/FSNode.framework/Versions/A/Resources/English.lproj
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/FSNode.framework/Versions/A/%{gscpu}

%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gstriple}/lib*.so.*

%dir %{gsservicedir}/thumbnailer.service
%dir %{gsservicedir}/thumbnailer.service/%{gscpu}
%dir %{gsservicedir}/thumbnailer.service/%{gscpu}/%{gsos}
%dir %{gsservicedir}/thumbnailer.service/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{gsservicedir}/thumbnailer.service/%{gstriple}/*
%dir %{gsservicedir}/thumbnailer.service/Resources
%{gsservicedir}/*.service/Resources/*.plist
%dir %{gsservicedir}/thumbnailer.service/Resources/*.thumb
%dir %{gsservicedir}/thumbnailer.service/Resources/*.thumb/%{gscpu}
%dir %{gsservicedir}/thumbnailer.service/Resources/*.thumb/%{gscpu}/%{gsos}
%dir %{gsservicedir}/thumbnailer.service/Resources/*.thumb/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{gsservicedir}/thumbnailer.service/Resources/*.thumb/%{gstriple}/*
%dir %{gsservicedir}/thumbnailer.service/Resources/*.thumb/Resources
%{gsservicedir}/thumbnailer.service/Resources/ImageThumbnailer.thumb/Resources/*.plist

%attr(755,root,root) %{_prefix}/System/Tools/%{gstriple}/*

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Frameworks/FSNode.framework/Versions/A/Headers
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gstriple}/lib*.so
%{_prefix}/System/Library/Headers/%{libcombo}/GWorkspace
