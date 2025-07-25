Summary:	Simple tool to check MP3s files
Summary(pl.UTF-8):	Proste narzędzie do sprawdzania plików MP3
Name:		mp3_check
Version:	1.98
Release:	3
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/mp3check/%{name}-%{version}.tar.gz
# Source0-md5:	d10e3d7d434af17cc036b752a816e492
Patch0:		%{name}-types.patch
URL:		http://mp3check.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3_check looks for invalid frame headers, missing frames, etc., and
generates useful statistics. This can be especially important when
building an archive, and you want high quality MP3s.

%description -l pl.UTF-8
mp3_check szuka złych ramek nagłówków, zgubionych ramek, itp. oraz
generuje użyteczny raport. mp3_check jest bardzo przydatny do
tworzenia archiwum, w którym zawarte są pliki MP3 o wysokiej jakości.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mp3_check $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO FOR_TESTING MILESTONE
%attr(755,root,root) %{_bindir}/mp3_check
