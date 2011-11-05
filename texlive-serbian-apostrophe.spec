# revision 23799
# category Package
# catalog-ctan /language/serbian/serbian-apostrophe
# catalog-date 2011-08-30 14:04:46 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-serbian-apostrophe
Version:	20110830
Release:	1
Summary:	Commands for Serbian words with apostrophes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/serbian/serbian-apostrophe
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-apostrophe.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-apostrophe.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a collection of commands (whose names are
Serbian words) whose expansion is the Serbian word with
appropriate apostrophes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/serbian-apostrophe/serbian-apostrophe.sty
%doc %{_texmfdistdir}/doc/latex/serbian-apostrophe/README
%doc %{_texmfdistdir}/doc/latex/serbian-apostrophe/apostrophe-list.pdf
%doc %{_texmfdistdir}/doc/latex/serbian-apostrophe/apostrophe-list.tex
%doc %{_texmfdistdir}/doc/latex/serbian-apostrophe/serbian-apostrophe.pdf
%doc %{_texmfdistdir}/doc/latex/serbian-apostrophe/serbian-apostrophe.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
