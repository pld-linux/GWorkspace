Summary:	Workspace manager for GNUstep
Summary(pl):	Zarz±dca biurek dla GNUstepa
Name:		GWorkspace
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gnustep.it/enrico/gworkspace/gworkspace-%{version}.tar.gz
# Source0-md5:	c24f9d4801b04cdf61e763aa07061e77
URL:		http://www.gnustep.it/enrico/gworkspace/
BuildRequires:	gnustep-gui-devel >= 0.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/lib/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif

%define		gstriple	%{gscpu}/%{gsos}/%{libcombo}
%define		gsservicedir	%{_prefix}/System/Library/Services

%description
GWorkspace is a workspace and file manager for GNUstep.

%description -l pl
GWorkspace to zarz±dca biurek i plików dla GNUstepa.

%prep
%setup -q

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

%dir %{_prefix}/System/Applications/GWorkspace.app
%attr(755,root,root) %{_prefix}/System/Applications/GWorkspace.app/GWorkspace
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.desktop
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.plist
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.tiff

%dir %{_prefix}/System/Applications/GWorkspace.app
%dir %{_prefix}/System/Applications/GWorkspace.app/%{gscpu}
%dir %{_prefix}/System/Applications/GWorkspace.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/GWorkspace.app/%{gstriple}
%attr(755,root,root) %{_prefix}/System/Applications/GWorkspace.app/%{gstriple}/GWorkspace
%{_prefix}/System/Applications/GWorkspace.app/%{gstriple}/*.openapp
%{_prefix}/System/Applications/GWorkspace.app/GWorkspace
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.plist
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.desktop
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.tiff
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
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/Resources/*.plist
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/Resources/*.tiff
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/Resources/English.lproj
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/%{gscpu}
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/%{gstriple}
%attr(755,root,root) %{_prefix}/System/Applications/GWorkspace.app/Resources/*.viewer/%{gstriple}/*
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources/*.inspector
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources/*.inspector/Resources
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.inspector/Resources/*.plist
%{_prefix}/System/Applications/GWorkspace.app/Resources/*.inspector/Resources/*.tiff
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources/*.inspector/%{gscpu}
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources/*.inspector/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/GWorkspace.app/Resources/*.inspector/%{gstriple}
%attr(755,root,root) %{_prefix}/System/Applications/GWorkspace.app/Resources/*.inspector/%{gstriple}/*
%dir %{_prefix}/System/Applications/GWorkspace.app/%{gscpu}
%dir %{_prefix}/System/Applications/GWorkspace.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/GWorkspace.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/GWorkspace.app/%{gstriple}/GWorkspace
%{_prefix}/System/Applications/GWorkspace.app/%{gstriple}/*.openapp

%attr(755,root,root) %{_prefix}/System/Tools/%{gstriple}/*

%dir %{_prefix}/System/Library/Bundles/*.thumb
%dir %{_prefix}/System/Library/Bundles/*.thumb/%{gscpu}
%dir %{_prefix}/System/Library/Bundles/*.thumb/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/Bundles/*.thumb/%{gstriple}
%attr(755,root,root) %{_prefix}/System/Library/Bundles/*.thumb/%{gstriple}/*
%dir %{_prefix}/System/Library/Bundles/*.thumb/Resources
%{_prefix}/System/Library/Bundles/*.thumb/Resources/*.plist
%dir %{_prefix}/System/Library/Bundles/*.viewer
%dir %{_prefix}/System/Library/Bundles/*.viewer/%{gscpu}
%dir %{_prefix}/System/Library/Bundles/*.viewer/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/Bundles/*.viewer/%{gstriple}
%attr(755,root,root) %{_prefix}/System/Library/Bundles/*.viewer/%{gstriple}/*
%dir %{_prefix}/System/Library/Bundles/*.viewer/Resources
%{_prefix}/System/Library/Bundles/*.viewer/Resources/*.plist
%{_prefix}/System/Library/Bundles/*.viewer/Resources/*.tiff
%{_prefix}/System/Library/Bundles/*.viewer/Resources/English.lproj
%dir %{_prefix}/System/Library/Bundles/*.inspector
%dir %{_prefix}/System/Library/Bundles/*.inspector/%{gscpu}
%dir %{_prefix}/System/Library/Bundles/*.inspector/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Library/Bundles/*.inspector/%{gstriple}
%attr(755,root,root) %{_prefix}/System/Library/Bundles/*.inspector/%{gstriple}/*
%dir %{_prefix}/System/Library/Bundles/*.inspector/Resources
%{_prefix}/System/Library/Bundles/*.inspector/Resources/*.plist
%{_prefix}/System/Library/Bundles/*.inspector/Resources/*.tiff

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

# some -devel?
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gstriple}/lib*.so
%{_prefix}/System/Library/Headers/%{libcombo}/GWorkspace
