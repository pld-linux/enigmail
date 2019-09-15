#
# Conditional build:
%bcond_without	thunderbird	# Mozilla Thunderbird addon
%bcond_without	seamonkey	# Mozilla SeaMonkey addon

Summary:	Mozilla mail clients extension for the GnuPG authentication and encryption features
Summary(pl.UTF-8):	Rozszerzenie klientów pocztowych Mozilla do uwierzytelniania i szyfrowania w oparciu o GnuPG
Name:		enigmail
Version:	2.1.2
Release:	1
Epoch:		1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Mail
Source0:	https://enigmail.net/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	50ace3f61a9c937d59b6a15bb9b260fa
URL:		http://enigmail.net/
BuildRequires:	make >= 3.81
BuildRequires:	perl-base >= 5
BuildRequires:	python >= 1:2.7
BuildRequires:	zip
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enigmail is an extension to the Mozilla-based mail clients (like
Mozilla Thunderbird, Mozilla Seamonkey or Iceape) which
allows users to access the authentication and encryption features
provided by GnuPG.

Main Features:
- Encrypt/sign mail when sending, decrypt/authenticate received mail
- Support for inline-PGP (RFC 2440) and PGP/MIME (RFC 3156)
- Per-Account based encryption and signing defaults
- Per-Recipient rules for automated key selection, and
  enabling/disabling encryption and signing
- OpenPGP key management interface

%description -l pl.UTF-8
Enigmail to rozszerzenie klientów pocztowych opartych na Mozilli (jak
Mozilla Thunderbird, Mozilla Seamonkey i Iceape), pozwalające
użytkownikom na dostęp do uwierzytelniania i szyfrowania zapewnianego
przez GnuPG.

Główne możliwości:
- szyfrowanie/podpisywanie poczty przy wysyłaniu,
  odszyfrowywanie/uwierzytelnianie poczty odebranej
- obsługa inline-PGP (RFC 2440) i PGP/MIME (RFC 3156)
- ustawienia domyślne szyfrowania i podpisywania dla każdego konta
- reguły automatycznego wyboru kluczy i włączenia szyfrowania oraz
  podpisywania dla każdego adresata
- interfejs do zarządzania kluczami OpenPGP

%package -n thunderbird-addon-enigmail
Summary:	Thunderbird extension for the authentication and encryption features provided by GnuPG
Summary(pl.UTF-8):	Rozszerzenie Thunderbirda do uwierzytelniania i szyfrowania zapewnianego przez GnuPG
Group:		X11/Applications/Mail
Requires:	gnupg2 >= 2.0.7
Requires:	gnupg-agent >= 2.0.7
Requires:	thunderbird >= 38.0
Obsoletes:	icedove-addon-enigmail
Obsoletes:	mozilla-thunderbird-addon-enigmail
BuildArch:	noarch

%description -n thunderbird-addon-enigmail
Enigmail is an extension to the Mozilla Thunderbird mail client of
which allows users to access the authentication and encryption
features provided by GnuPG.

Main Features:
- Encrypt/sign mail when sending, decrypt/authenticate received mail
- Support for inline-PGP (RFC 2440) and PGP/MIME (RFC 3156)
- Per-Account based encryption and signing defaults
- Per-Recipient rules for automated key selection, and
  enabling/disabling encryption and signing
- OpenPGP key management interface

%description -n thunderbird-addon-enigmail -l pl.UTF-8
Enigmail to rozszerzenie klienta pocztowego Mozilla Thunderbird,
pozwalające użytkownikom na dostęp do uwierzytelniania i szyfrowania
zapewnianego przez GnuPG.

Główne możliwości:
- szyfrowanie/podpisywanie poczty przy wysyłaniu,
  odszyfrowywanie/uwierzytelnianie poczty odebranej
- obsługa inline-PGP (RFC 2440) i PGP/MIME (RFC 3156)
- ustawienia domyślne szyfrowania i podpisywania dla każdego konta
- reguły automatycznego wyboru kluczy i włączenia szyfrowania oraz
  podpisywania dla każdego adresata
- interfejs do zarządzania kluczami OpenPGP

%package -n seamonkey-addon-enigmail
Summary:	SeaMonkey extension for the authentication and encryption features provided by GnuPG
Summary(pl.UTF-8):	Rozszerzenie SeaMonkeya do uwierzytelniania i szyfrowania zapewnianego przez GnuPG
Group:		X11/Applications/Mail
Requires:	gnupg2 >= 2.0.7
Requires:	gnupg-agent >= 2.0.7
Requires:	seamonkey >= 2.35
Obsoletes:	iceape-addon-enigmail
BuildArch:	noarch

%description -n seamonkey-addon-enigmail
Enigmail is an extension to the mail client of Mozilla SeaMonkey which
allows users to access the authentication and encryption features
provided by GnuPG.

Main Features:
- Encrypt/sign mail when sending, decrypt/authenticate received mail
- Support for inline-PGP (RFC 2440) and PGP/MIME (RFC 3156)
- Per-Account based encryption and signing defaults
- Per-Recipient rules for automated key selection, and
  enabling/disabling encryption and signing
- OpenPGP key management interface

%description -n seamonkey-addon-enigmail -l pl.UTF-8
Enigmail to rozszerzenie klienta pocztowego programu Mozilla
SeaMonkey, pozwalające użytkownikom na dostęp do uwierzytelniania i
szyfrowania zapewnianego przez GnuPG.

Główne możliwości:
- szyfrowanie/podpisywanie poczty przy wysyłaniu,
  odszyfrowywanie/uwierzytelnianie poczty odebranej
- obsługa inline-PGP (RFC 2440) i PGP/MIME (RFC 3156)
- ustawienia domyślne szyfrowania i podpisywania dla każdego konta
- reguły automatycznego wyboru kluczy i włączenia szyfrowania oraz
  podpisywania dla każdego adresata
- interfejs do zarządzania kluczami OpenPGP

%prep
%setup -q -n %{name}

%build
%configure

%{__make} -j1

%install
install -d $RPM_BUILD_ROOT%{_datadir}/thunderbird/distribution/extensions/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
unzip build/%{name}-%{version}.xpi -d $RPM_BUILD_ROOT%{_datadir}/thunderbird/distribution/extensions/\{847b3a00-7ab1-11d4-8f02-006008948af5\}/

install -d $RPM_BUILD_ROOT%{_datadir}/seamonkey/extensions/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
unzip build/%{name}-%{version}.xpi -d $RPM_BUILD_ROOT%{_datadir}/seamonkey/extensions/\{847b3a00-7ab1-11d4-8f02-006008948af5\}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with thunderbird}
%files -n thunderbird-addon-enigmail
%defattr(644,root,root,755)
%dir %{_datadir}/thunderbird/distribution/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}
%{_datadir}/thunderbird/distribution/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/chrome
%{_datadir}/thunderbird/distribution/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/bootstrap.js
%{_datadir}/thunderbird/distribution/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/chrome.manifest
%{_datadir}/thunderbird/distribution/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/install.rdf
%{_datadir}/thunderbird/distribution/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/manifest.json
%endif

%if %{with seamonkey}
%files -n seamonkey-addon-enigmail
%defattr(644,root,root,755)
%dir %{_datadir}/seamonkey/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}
%{_datadir}/seamonkey/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/chrome
%{_datadir}/seamonkey/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/bootstrap.js
%{_datadir}/seamonkey/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/chrome.manifest
%{_datadir}/seamonkey/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/install.rdf
%{_datadir}/seamonkey/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/manifest.json
%endif
