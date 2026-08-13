%global tl_name theanooldstyle
%global tl_revision 78931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Theano OldStyle fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/theanooldstyle
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/theanooldstyle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/theanooldstyle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides the Theano OldStyle font designed by Alexey
Kryukov, in both TrueType and Type1 formats, with support for both
traditional and modern LaTeX processors. An artificially-emboldened
variant has been provided but there are no italic variants. The package
is named after Theano, a famous Ancient Greek woman philosopher, who was
first a student of Pythagoras, and supposedly became his wife.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from theanooldstyle:
Map TheanoOldStyle.map
TL_DROPIN_EOF
