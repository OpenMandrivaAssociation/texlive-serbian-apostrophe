%global tl_name serbian-apostrophe
%global tl_revision 23799

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Commands for Serbian words with apostrophes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/serbian/filipovic/serbian-apostrophe
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-apostrophe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-apostrophe.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a collection of commands (whose names are Serbian
words) whose expansion is the Serbian word with appropriate apostrophes.

