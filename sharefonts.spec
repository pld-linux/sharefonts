Summary:	Collection of SHAREWARE ATM Fonts for Linux
Summary(pl.UTF-8):   Kolekcja czcionek SHAREWARE ATM dla Linuksa
Name:		sharefonts
Version:	0.10
Release:	13
License:	Shareware
Group:		Fonts
Source0:	ftp://sunsite.unc.edu/pub/Linux/X11/fonts/%{name}-%{version}.tar.gz
# Source0-md5:	fd407f15efc7f06e320c10fd73d66c1f
Source1:	%{name}.Fontmap
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_t1fontsdir	%{_fontsdir}/Type1

%description
This is a collection of 21 fonts from the CICA archives that are
shareware. NOTICE: They are not free. You have to pay a fee for
constant use. They are licensed by the authors not by me. Read the
<font>.shareware notices for each font to find out how to license
them. I have just collected them and put them into a usable format for
X11. The collection was motivated by the lack of good fonts for Linux
especially X11 and ghostscript. Scaled bitmaps look really ugly!

%description -l pl.UTF-8
To jest kolekcja 21 shareware'owych czcionek, pochodzących z archiwów
CICA. UWAGA: Nie są one za darmo. Musisz uiścić opłatę jeśli chcesz
ich używać dłużej, niż to przewiduje ich status. Zapoznaj się z
informacjami w plikach <czcionka>.shareware, by dowiedzieć się, jak
zdobyć licencję na ich używanie.

%prep
%setup -q -n sharefont

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_t1fontsdir}
install *.pfb $RPM_BUILD_ROOT%{_t1fontsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.%{name}
tail -n +2 fonts.dir > $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc README *.shareware
%{_t1fontsdir}/*
