Summary:	Collection of SHAREWARE ATM Fonts for Linux
Summary(pl):	Kolekcja czcionek SHAREWARE ATM dla Linuksa
Name:		sharefonts
Version:	0.10
Release:	12
License:	Shareware
Group:		X11/Fonts
Source0:	ftp://sunsite.unc.edu/pub/Linux/X11/fonts/%{name}-%{version}.tar.gz
Source1:	%{name}.Fontmap
Prereq:		textutils
Prereq:		sed
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

%description -l pl
To jest kolekcja 21 shareware'owych czcionek, pochodz±cych z archiwów
CICA. UWAGA: Nie s± one za darmo. Musisz ui¶ciæ op³atê je¶li chcesz
ich u¿ywaæ d³u¿ej, ni¿ to przewiduje ich status. Zapoznaj siê z
informacjami w plikach <czcionka>.shareware, by dowiedzieæ siê, jak
zdobyæ licencjê na ich u¿ywanie.

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
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap

%postun
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap 2>/dev/null

%files
%defattr(644,root,root,755)
%doc README *.shareware
%{_t1fontsdir}/*
