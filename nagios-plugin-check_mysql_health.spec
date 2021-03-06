%define		plugin	check_mysql_health
%include	/usr/lib/rpm/macros.perl
%undefine _disable_source_fetch
Summary:	Nagios plugin: monitor various performance-related characteristics of a MySQL DB
Summary(pl.UTF-8):	Wtyczka Nagiosa monitorująca parametry wydajnościowe bazy danych MySQL
Name:		nagios-plugin-%{plugin}
Version:	2.2.2
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	https://labs.consol.de/assets/downloads/nagios/check_mysql_health-%{version}.tar.gz
%define         SHA256SUM0 bae2a2b415a902a42287459acdc4dda5278decd43bd24b4ac7770ec2ad11559f
Source1:	https://raw.githubusercontent.com/pld-linux/nagios-plugin-check_mysql_health/master/%{plugin}.cfg
URL:		http://labs.consol.de/lang/en/nagios/check_mysql_health/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Requires:	nagios-common >= 3.2.3-3
Obsoletes:	nagios-plugin-check_mysql_perf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins
%define		statedir	/var/spool/nagios/%{plugin}

%description
Nagios plugin which allows you to monitor various performance-related
characteristics of a MySQL database.

%description -l pl.UTF-8
Wtyczka Nagiosa pozwalająca na monitorowanie różnych parametrów bazy
danych MySQL związanych z wydajnością.

%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -
%setup -q -n %{plugin}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
# NOTE: _target macro becames "noarch" if ./builder passes --target=noarch, so
# be sure use plain rpmbuild.
%configure \
	--host=%{_host} \
	--build=%{_host} \
	--with-perl=%{__perl} \
	--libdir=%{plugindir} \
	--libexecdir=%{plugindir} \
	--with-mymodules-dir=%{plugindir} \
	--with-mymodules-dyn-dir=%{plugindir} \
	--with-statefiles-dir=%{statedir} \
	--with-nagios-user=nagios \
	--with-nagios-group=nagios
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{statedir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
%attr(770,root,nagios) %dir %{statedir}

