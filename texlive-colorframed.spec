Name:		texlive-colorframed
Version:	64551
Release:	2
Summary:	Fix color problems with the package "framed"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colorframed
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorframed.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorframed.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package fixes problems with colour loss that occurres in
the environments of the framed package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/colorframed
%doc %{_texmfdistdir}/doc/latex/colorframed

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
