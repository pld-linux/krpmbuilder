Summary:	KRPMBuilder makes the building of spec files and RPM packages easy
Name:		krpmbuilder
Version:	1.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/krpmbuilder/%{name}-%{version}.tar.gz
# Source0-md5:	99b84803171d64f1347617b5facd3851
URL:		http://krpmbuilder.sourceforge.net/
BuildRequires:	libpng-devel
Buildrequires:	qt-devel
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KRPMBuilder is a KDE application that makes the building of spec files
and RPM packages easy. After editing the spec-file in an intuitive,
KDE-based GUI, you can execute RPM inside KRPMBuilder and control the
progress of the package build process.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Development/krpmbuilder.desktop $RPM_BUILD_ROOT%{_desktopdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/*/*x*/apps/%{name}.png
%{_datadir}/apps/krpmbuilder/pics/*.png
