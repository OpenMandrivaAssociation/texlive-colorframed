%global tl_name colorframed
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9b
Release:	%{tl_revision}.1
Summary:	Fix color problems with the package framed
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/colorframed
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorframed.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorframed.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package fixes problems with colour loss that occurs in the
environments of the framed package.

