Summary:	Collection of SHAREWARE ATM Fonts for Linux
Summary(pl):	Kolekcja czcionek SHAREWARE ATM dla Linuxa
Name:		sharefonts
Version:	0.10
Release:	11
Copyright:	shareware
Group:		X11/Fonts
Group(pl):	X11/Fonty
Source:		ftp://sunsite.unc.edu/pub/Linux/X11/fonts/%{name}-%{version}.tar.gz
Requires:	type1inst >= 0.6.1
Prereq:		type1inst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_fontdir	/usr/share/fonts

%description
This is a collection of 22 fonts from the CICA archives that are shareware.
NOTICE: They are not free. You have to pay a fee for constant use. They are
licensed by the authors not by me. Read the <font>.shareware notices for
each font to find out how to license them. I have just collected them and
put them into a usable format for X11. The collection was motivated by the
lack of good fonts for Linux especially X11 and ghostscript. Scaled bitmaps
look really ugly!

%description -l pl
To jest kolekcja 22 shareware'owych czcionek, pochodz±cych z archiwów CICA. 
UWAGA: Nie s± one za darmo. Musisz ui¶ciæ op³atê je¶li chcesz ich u¿ywaæ
d³u¿ej, ni¿ to przewiduje ich status. Zapoznaj siê z informacjami w plikach 
<czcionka>.shareware, by dowiedzieæ siê, jak zdobyæ licencjê na ich u¿ywanie.

%prep
%setup -q -n sharefont

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontdir}/Type1
install *.pfb $RPM_BUILD_ROOT%{_fontdir}/Type1

gzip -9nf README *.shareware

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_fontdir}/Type1
type1inst -nogs -quiet

%postun
cd %{_fontdir}/Type1
type1inst -nogs -quiet

%files
%defattr(644,root,root,755)
%doc README.gz *.shareware.gz
%{_fontdir}/Type1/*.pfb
