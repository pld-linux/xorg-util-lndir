Summary:	lndir utility - create a directory of symbolic links to another directory tree
Summary(pl):	Narz�dzie lndir - tworzenie katalogu dowi�za� symbolicznych do innego drzewa
Name:		xorg-util-lndir
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/lndir-%{version}.tar.bz2
# Source0-md5:	e274ea9f55dfd62afa0a7b1e1ab4ba96
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The lndir program makes a shadow copy of a source directory tree,
except that the shadow is not populated with real files but instead
with symbolic links pointing at the real files in the source directory
tree. This is usually useful for maintaining source code for different
machine architectures. You create a shadow directory containing links
to the real source, which you will have usually mounted from a remote
machine.

%description -l pl
Program lndir tworzy kopi� �r�d�owego drzewa katalog�w z t� r�nic�,
�e nie kopiuje samych plik�w, a jedynie tworzy dowi�zania symboliczne
wskazuj�ce na prawdziwe pliki w �r�d�owym drzewie katalog�w. Jest to
zwykle przydatne do utrzymywania kodu �r�d�owego dla r�nych
architektur. Tworzy si� wtedy katalog zawieraj�cy dowi�zania do
prawdziwych �r�de�, kt�re mo�na mie� podmontowane ze zdalnej maszyny.

%prep
%setup -q -n lndir-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/lndir
%{_mandir}/man1/lndir.1x*
