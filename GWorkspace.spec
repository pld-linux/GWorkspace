Summary:	Workspace manager for GNUstep
Summary(pl.UTF-8):	Zarządca biurek dla GNUstepa
Name:		GWorkspace
Version:	0.8.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gnustep.it/enrico/gworkspace/gworkspace-%{version}.tar.gz
# Source0-md5:	16dc6b077517b60897cc0d057bb803f5
#Patch0: %{name}-link.patch
Patch1:		%{name}-initWithArguments.patch
URL:		http://www.gnustep.it/enrico/gworkspace/
BuildRequires:	gnustep-gui-devel >= 0.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GWorkspace is a workspace and file manager for GNUstep.

%description -l pl.UTF-8
GWorkspace to zarządca biurek i plików dla GNUstepa.

%package devel
Summary:	Header files for GWorkspace
Summary(pl.UTF-8):	Pliki nagłówkowe GWorkspace
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GWorkspace.

%description devel -l pl.UTF-8
Pliki nagłówkowe GWorkspace.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1

find . -type d -name CVS | xargs rm -rf

%build
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes
export GNUSTEP_INSTALLATION_DOMAIN=SYSTEM
%configure
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_bindir}/GWorkspace
%attr(755,root,root) %{_bindir}/Recycler
%attr(755,root,root) %{_bindir}/ddbd
%attr(755,root,root) %{_bindir}/fswatcher
%attr(755,root,root) %{_bindir}/lsfupdater
%attr(755,root,root) %{_bindir}/resizer
%attr(755,root,root) %{_bindir}/searchtool
%attr(755,root,root) %{_bindir}/wopen
%attr(755,root,root) %{_libdir}/GNUstep/Applications/GWorkspace.app/GWorkspace
%dir %{_libdir}/GNUstep/Applications/GWorkspace.app/Resources/
%{_libdir}/GNUstep/Applications/GWorkspace.app/Resources/*.tiff
%{_libdir}/GNUstep/Applications/GWorkspace.app/Resources/*.lproj
%{_libdir}/GNUstep/Applications/GWorkspace.app/Resources/*.desktop
%{_libdir}/GNUstep/Applications/GWorkspace.app/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Recycler.app/Recycler
%{_libdir}/GNUstep/Applications/Recycler.app/Resources/*.lproj
%{_libdir}/GNUstep/Applications/Recycler.app/Resources/*.plist
%{_libdir}/GNUstep/Applications/Recycler.app/Resources/*.desktop
%{_libdir}/GNUstep/Applications/Recycler.app/Resources/*.tiff
%dir %{_libdir}/GNUstep/Frameworks/Operation.framework
%dir %{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*
%{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/Current
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*/Operation
%dir %{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*/Resources
%{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*/Resources/*.lproj
%{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*/Resources/*.plist
%{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*/Resources/*.tiff
%{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*/libOperation.so
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/AppViewer.inspector/AppViewer
%{_libdir}/GNUstep/Bundles/AppViewer.inspector/Resources/*.lproj
%{_libdir}/GNUstep/Bundles/AppViewer.inspector/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/FModuleAnnotations.finder/FModuleAnnotations
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/FModuleContents.finder/FModuleContents
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/FModuleCrDate.finder/FModuleCrDate
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/FModuleKind.finder/FModuleKind
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/FModuleModDate.finder/FModuleModDate
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/FModuleName.finder/FModuleName
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/FModuleOwner.finder/FModuleOwner
%{_libdir}/GNUstep/Bundles/*.finder/Resources/*.gorm
%{_libdir}/GNUstep/Bundles/*.finder/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/FModuleSize.finder/FModuleSize
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/FolderViewer.inspector/FolderViewer
%dir %{_libdir}/GNUstep/Bundles/FolderViewer.inspector/Resources
%{_libdir}/GNUstep/Bundles/FolderViewer.inspector/Resources/*.lproj
%{_libdir}/GNUstep/Bundles/FolderViewer.inspector/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/IBViewViewer.inspector/IBViewViewer
%dir %{_libdir}/GNUstep/Bundles/IBViewViewer.inspector/Resources
%{_libdir}/GNUstep/Bundles/IBViewViewer.inspector/Resources/*.lproj
%{_libdir}/GNUstep/Bundles/IBViewViewer.inspector/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/ImageThumbnailer.thumb/ImageThumbnailer
%dir %{_libdir}/GNUstep/Bundles/ImageThumbnailer.thumb/Resources
%{_libdir}/GNUstep/Bundles/ImageThumbnailer.thumb/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/ImageViewer.inspector/ImageViewer
%dir %{_libdir}/GNUstep/Bundles/ImageViewer.inspector/Resources
%{_libdir}/GNUstep/Bundles/ImageViewer.inspector/Resources/*.lproj
%{_libdir}/GNUstep/Bundles/ImageViewer.inspector/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/MDModuleAnnotations.mdm/MDModuleAnnotations
%dir %{_libdir}/GNUstep/Bundles/MDModuleAnnotations.mdm/Resources
%{_libdir}/GNUstep/Bundles/MDModuleAnnotations.mdm/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/NSColorViewer.inspector/NSColorViewer
%dir %{_libdir}/GNUstep/Bundles/NSColorViewer.inspector/Resources
%{_libdir}/GNUstep/Bundles/NSColorViewer.inspector/Resources/*.lproj
%{_libdir}/GNUstep/Bundles/NSColorViewer.inspector/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/NSRTFViewer.inspector/NSRTFViewer
%dir %{_libdir}/GNUstep/Bundles/NSRTFViewer.inspector/Resources
%{_libdir}/GNUstep/Bundles/NSRTFViewer.inspector/Resources/*.lproj
%{_libdir}/GNUstep/Bundles/NSRTFViewer.inspector/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/NSTIFFViewer.inspector/NSTIFFViewer
%dir %{_libdir}/GNUstep/Bundles/NSTIFFViewer.inspector/Resources
%{_libdir}/GNUstep/Bundles/NSTIFFViewer.inspector/Resources/*.lproj
%{_libdir}/GNUstep/Bundles/NSTIFFViewer.inspector/Resources/*.plist
%dir %{_libdir}/GNUstep/Bundles/Role.extinfo/Resources
%{_libdir}/GNUstep/Bundles/Role.extinfo/Resources/*.plist
%{_libdir}/GNUstep/Bundles/Role.extinfo/Role
%dir %{_libdir}/GNUstep/Bundles/RtfViewer.inspector/Resources
%{_libdir}/GNUstep/Bundles/RtfViewer.inspector/Resources/*.lproj
%{_libdir}/GNUstep/Bundles/RtfViewer.inspector/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/RtfViewer.inspector/RtfViewer
%dir %{_libdir}/GNUstep/Bundles/SoundViewer.inspector/Resources
%{_libdir}/GNUstep/Bundles/SoundViewer.inspector/Resources/*.lproj
%{_libdir}/GNUstep/Bundles/SoundViewer.inspector/Resources/*.plist
%{_libdir}/GNUstep/Bundles/SoundViewer.inspector/Resources/*.tiff
%attr(755,root,root) %{_libdir}/GNUstep/Bundles/SoundViewer.inspector/SoundViewer
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/FSNode.framework/FSNode
%{_libdir}/GNUstep/Frameworks/FSNode.framework/Resources
%dir %{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*
%dir %{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*/FSNode
%dir %{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*/Resources
%{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*/Resources/*.tiff
%{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*/Resources/*.lproj
%{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*/libFSNode.so
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*/libFSNode.so.0
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*/libFSNode.so.0.1.0
%{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/Current
%{_libdir}/GNUstep/Frameworks/FSNode.framework/libFSNode.so
%{_libdir}/GNUstep/Frameworks/Inspector.framework/Inspector
%{_libdir}/GNUstep/Frameworks/Inspector.framework/Resources
%dir %{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*
%dir %{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*
%{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/Current
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*/Inspector
%dir %{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*/Resources
%{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*/Resources/*.tiff
%{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*/Resources/*.lproj
%{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*/Resources/*.plist
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*/libInspector.so
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*/libInspector.so.0
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*/libInspector.so.*.*.*
%{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*
%{_libdir}/GNUstep/Frameworks/Inspector.framework/libInspector.so
%{_libdir}/GNUstep/Frameworks/Operation.framework/Operation
%{_libdir}/GNUstep/Frameworks/Operation.framework/Resources
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*/libOperation.so.1
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*/libOperation.so.1.0.0
%{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*
%{_libdir}/GNUstep/Frameworks/Operation.framework/libOperation.so
%{_libdir}/GNUstep/Services/thumbnailer.service/Resources/*.plist
%dir %{_libdir}/GNUstep/Services/thumbnailer.service
%attr(755,root,root) %{_libdir}/GNUstep/Services/thumbnailer.service/thumbnailer
%{_libdir}/libDBKit.so
%attr(755,root,root) %{_libdir}/libDBKit.so.0.0.1
%{_libdir}/libFSNode.so
%attr(755,root,root) %{_libdir}/libFSNode.so.0.1.0
%{_libdir}/libInspector.so
%attr(755,root,root) %{_libdir}/libInspector.so.0.1.0
%{_libdir}/libOperation.so
%attr(755,root,root) %{_libdir}/libOperation.so.1.0.0

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/DBKit
%{_includedir}/DBKit/DBKBTree.h
%{_includedir}/DBKit/DBKBTreeNode.h
%{_includedir}/DBKit/DBKFixLenRecordsFile.h
%{_includedir}/DBKit/DBKPathsTree.h
%{_includedir}/DBKit/DBKVarLenRecordsFile.h
%{_includedir}/FSNode
%{_includedir}/Inspector
%{_includedir}/Operation
%dir %{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*/Headers
%{_libdir}/GNUstep/Frameworks/FSNode.framework/Versions/[0-9]*/Headers/*.h
%{_libdir}/GNUstep/Frameworks/Inspector.framework/Headers
%dir %{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*/Headers
%{_libdir}/GNUstep/Frameworks/Inspector.framework/Versions/[0-9]*/Headers/*.h
%{_libdir}/GNUstep/Frameworks/Operation.framework/Headers
%dir %{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*/Headers
%{_libdir}/GNUstep/Frameworks/Operation.framework/Versions/[0-9]*/Headers/*.h
%{_libdir}/GNUstep/Frameworks/FSNode.framework/Headers
