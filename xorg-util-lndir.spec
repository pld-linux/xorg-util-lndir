Summary:	lndir utility - create a directory of symbolic links to another directory tree
Summary(pl.UTF-8):	Narzędzie lndir - tworzenie katalogu dowiązań symbolicznych do innego drzewa
Name:		xorg-util-lndir
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	https://xorg.freedesktop.org/releases/individual/util/lndir-%{version}.tar.xz
# Source0-md5:	a56ce1f81960e4b5af1730e4f5262162
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libbsd-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The lndir program makes a shadow copy of a source directory tree,
except that the shadow is not populated with real files but instead
with symbolic links pointing at the real files in the source directory
tree. This is usually useful for maintaining source code for different
machine architectures. You create a shadow directory containing links
to the real source, which you will have usually mounted from a remote
machine.

%description -l pl.UTF-8
Program lndir tworzy kopię źródłowego drzewa katalogów z tą różnicą,
że nie kopiuje samych plików, a jedynie tworzy dowiązania symboliczne
wskazujące na prawdziwe pliki w źródłowym drzewie katalogów. Jest to
zwykle przydatne do utrzymywania kodu źródłowego dla różnych
architektur. Tworzy się wtedy katalog zawierający dowiązania do
prawdziwych źródeł, które można mieć podmontowane ze zdalnej maszyny.

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/lndir
%{_mandir}/man1/lndir.1*
