
Summary:	Simple tool to check mp3s files
Summary(pl):	Proste narz�dzie do sprawdzania plik�w mp3
Name:		mp3_check
Version:	1.98
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://freshmeat.net/redir/mp3_check/6710/url_tgz/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3_check looks for invalid frame headers, missing frames, etc., and
generates useful statistics. This can be especially important when
building an archive, and you want high quality MP3s

%description -l pl
mp3_check szuka z�ych ramem nag�owkow, zgubionych ramek, itd. oraz
generuje u�yteczny raport. mp3_check jest bardzi przydatny to
tworzenia archiw�w, w ktorym zawarte s� pliki mp3 o wysokiej jako�ci.

%prep
%setup -q

%build
%{__make} CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mp3_check $RPM_BUILD_ROOT%{_bindir}
gzip -9nf  TODO FOR_TESTING MILESTONE
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mp3_check
%doc *.gz
