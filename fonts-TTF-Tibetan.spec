Summary:	Free TrueType fonts for Tibetan script
Summary(pl.UTF-8):	Wolnodostępny font TrueType dla pisma tybetańskiego
Name:		fonts-TTF-Tibetan
Version:	1.901b
Release:	1
License:	GPL v2
Group:		Fonts
Source0:	https://collab.itc.virginia.edu/access/content/group/26a34146-33a6-48ce-001e-f16ce7908a6a/Tibetan%20fonts/Tibetan%20Unicode%20Fonts/TibetanMachineUnicodeFont.zip
# Source0-md5:	00baf42dd4609f1db8fab40bc3bd4f5c
URL:		http://www.thlib.org/tools/#wiki=/access/wiki/site/26a34146-33a6-48ce-001e-f16ce7908a6a/tibetan%20machine%20uni.html
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This is the alpha release of the Unicode character based Tibetan
Machine Uni OpenType font for writing Tibetan, Dzongkha and Ladakhi in
dbu can script with full support for the Sanskrit combinations found
in chos skad texts.

#%%description -l pl.UTF-8
# TODO

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

rm gpl.txt

install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc *.txt
%{ttffontsdir}/TibMachUni-%{version}.ttf
