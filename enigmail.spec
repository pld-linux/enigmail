#
# Conditional build:
%bcond_without	thunderbird	# Mozilla Thunderbird addon
%bcond_with	seamonkey	# Mozilla SeaMonkey addon
%bcond_without	iceape		# Iceape addon
# aliases:
%bcond_with	mozilla		# build both Mozilla packages
%bcond_without	iceapps		# don't build any Ice* packages

%if %{with mozilla}
%define		with_thunderbird	1
%define		with_seamonkey		1
%endif
%if %{without iceapps}
%undefine	with_iceape
%endif
Summary:	Mozilla mail clients extension for the GnuPG authentication and encryption features
Summary(pl.UTF-8):	Rozszerzenie klientów pocztowych Mozilla do uwierzytelniania i szyfrowania w oparciu o GnuPG
Name:		enigmail
Version:	1.9.5
Release:	3
Epoch:		1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Mail
Source0:	http://www.mozilla-enigmail.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	15eca51a6e7b3ff62b76e2dbea716305
URL:		http://www.mozilla-enigmail.org/
BuildRequires:	make >= 3.81
BuildRequires:	perl-base >= 5
BuildRequires:	python >= 1:2.7
BuildRequires:	zip
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

%package -n iceape-addon-enigmail
Summary:	Iceape extension for the authentication and encryption features provided by GnuPG
Summary(pl.UTF-8):	Rozszerzenie Iceape'a do uwierzytelniania i szyfrowania zapewnianego przez GnuPG
Group:		X11/Applications/Mail
Requires:	gnupg2 >= 2.0.7
Requires:	gnupg-agent >= 2.0.7
Requires:	iceape >= 2.35
Obsoletes:	seamonkey-addon-enigmail

%description -n iceape-addon-enigmail
Enigmail is an extension to the mail client of Iceape which allows
users to access the authentication and encryption features provided by
GnuPG.

Main Features:
- Encrypt/sign mail when sending, decrypt/authenticate received mail
- Support for inline-PGP (RFC 2440) and PGP/MIME (RFC 3156)
- Per-Account based encryption and signing defaults
- Per-Recipient rules for automated key selection, and
  enabling/disabling encryption and signing
- OpenPGP key management interface

%description -n iceape-addon-enigmail -l pl.UTF-8
Enigmail to rozszerzenie klienta pocztowego programu Iceape,
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

%prep
%setup -q -n %{name}

%build
%configure

%{__make} -j1

%install
for prog in %{?with_seamonkey:seamonkey} %{?with_iceape:iceape} ; do
ext_dir=$RPM_BUILD_ROOT%{_libdir}/$prog/extensions/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
install -d $ext_dir/{chrome,components,defaults/preferences,modules,wrappers}
cp -p build/dist/chrome/enigmail.jar $ext_dir/chrome
cp -p build/dist/components/*.{js,xpt} $ext_dir/components
cp -p build/dist/defaults/preferences/enigmail.js $ext_dir/defaults/preferences
cp -p build/dist/modules/*.js* $ext_dir/modules
cp -p build/dist/wrappers/*.sh $ext_dir/wrappers
cp -p build/dist/chrome.manifest $ext_dir
cp -p build/dist/install.rdf $ext_dir
done

for prog in %{?with_thunderbird:thunderbird} ; do
ext_dir=$RPM_BUILD_ROOT%{_datadir}/$prog/extensions/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
install -d $ext_dir/{chrome,components,defaults/preferences,modules,wrappers}
cp -p build/dist/chrome/enigmail.jar $ext_dir/chrome
cp -p build/dist/components/*.{js,xpt} $ext_dir/components
cp -p build/dist/defaults/preferences/enigmail.js $ext_dir/defaults/preferences
cp -p build/dist/modules/*.js* $ext_dir/modules
cp -p build/dist/wrappers/*.sh $ext_dir/wrappers
cp -p build/dist/chrome.manifest $ext_dir
cp -p build/dist/install.rdf $ext_dir
done

%clean
rm -rf $RPM_BUILD_ROOT

%define genfiles()\
%files -n %{1}-addon-enigmail\
%defattr(644,root,root,755)\
%dir %{2}/%{1}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}\
%{2}/%{1}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/chrome\
%{2}/%{1}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/components\
%{2}/%{1}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/defaults\
%{2}/%{1}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/modules\
%dir %{2}/%{1}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/wrappers\
%attr(755,root,root) %{2}/%{1}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/wrappers/gpg-agent-wrapper.sh\
%{2}/%{1}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/chrome.manifest\
%{2}/%{1}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}/install.rdf\
%{nil}

%{?with_thunderbird:%{expand:%genfiles thunderbird %{_datadir}}}
%{?with_seamonkey:%{expand:%genfiles seamonkey %{_libdir}}}
%{?with_iceape:%{expand:%genfiles iceape %{_libdir}}}
