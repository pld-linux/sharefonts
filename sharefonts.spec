Summary:	Collection of SHAREWARE ATM Fonts for Linux
Name:		sharefonts
Version:	0.10
Release:	11
Copyright:	shareware
BuildArchitectures: noarch
Group:		X11/fonts
Source:		ftp://sunsite.unc.edu/pub/Linux/X11/fonts/%{name}-%{version}.tar.gz
Requires:	type1inst >= 0.6.1
Prereq:		type1inst
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_fontdir	/usr/share/fonts

%description
This is a collection of 22 fonts from the CICA archives that are shareware.
NOTICE: They are not free. You have to pay a fee for constant use. They are
licensed by the authors not by me. Read the <font>.shareware notices for
each font to find out how to license them. I have just collected them and
put them into a usable format for X11. The collection was motivated by the
lack of good fonts for Linux especially X11 and ghostscript. Scaled bitmaps
look really ugly!

%prep
%setup -q -n sharefont

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_fontdir}/Type1
install *.pfb $RPM_BUILD_ROOT/%{_fontdir}/Type1

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
