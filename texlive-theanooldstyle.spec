Name:		texlive-theanooldstyle
Version:	64519
Release:	2
Summary:	Theano OldStyle fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/theanooldstyle
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theanooldstyle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theanooldstyle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the Theano OldStyle font designed by
Alexey Kryukov, in both TrueType and Type1 formats, with
support for both traditional and modern LaTeX processors. An
artificially-emboldened variant has been provided but there are
no italic variants. The package is named after Theano, a famous
Ancient Greek woman philosopher, who was first a student of
Pythagoras, and supposedly became his wife.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/theanooldstyle
%{_texmfdistdir}/fonts/vf/public/theanooldstyle
%{_texmfdistdir}/fonts/type1/public/theanooldstyle
%{_texmfdistdir}/fonts/truetype/public/theanooldstyle
%{_texmfdistdir}/fonts/tfm/public/theanooldstyle
%{_texmfdistdir}/fonts/map/dvips/theanooldstyle
%{_texmfdistdir}/fonts/enc/dvips/theanooldstyle
%doc %{_texmfdistdir}/doc/fonts/theanooldstyle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
