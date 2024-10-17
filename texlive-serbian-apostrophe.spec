Name:		texlive-serbian-apostrophe
Version:	23799
Release:	2
Summary:	Commands for Serbian words with apostrophes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/serbian/serbian-apostrophe
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-apostrophe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-apostrophe.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a collection of commands (whose names are
Serbian words) whose expansion is the Serbian word with
appropriate apostrophes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/serbian-apostrophe/serbian-apostrophe.sty
%doc %{_texmfdistdir}/doc/latex/serbian-apostrophe/README
%doc %{_texmfdistdir}/doc/latex/serbian-apostrophe/apostrophe-list.pdf
%doc %{_texmfdistdir}/doc/latex/serbian-apostrophe/apostrophe-list.tex
%doc %{_texmfdistdir}/doc/latex/serbian-apostrophe/serbian-apostrophe.pdf
%doc %{_texmfdistdir}/doc/latex/serbian-apostrophe/serbian-apostrophe.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
