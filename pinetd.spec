# TODO
# - package it, initscript
Summary:	Portable INET Daemon Framework
Name:		pinetd
Version:	0.0.328
Release:	0.3
License:	GPL v2
Group:		Applications
Source0:	%{name}.tar.bz2
# Source0-md5:	94e4cdfdaefeceb4b89e0654daf443c8
URL:		http://www.pinetd.net/
Requires:	/usr/bin/php
Requires:	php(dom)
Requires:	php(filter)
Requires:	php(ftp)
Requires:	php(gd)
Requires:	php(hash)
Requires:	php(iconv)
Requires:	php(mbstring)
Requires:	php(mysqli)
Requires:	php(pcre)
Requires:	php(proctitle)
Requires:	php(sockets)
Requires:	php(sqlite)
Requires:	php(tokenizer)
Requires:	php(xml)
Requires:	php(zlib)
#Requires:	php-common >= 4:5.3
Requires:	php-mhash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
PInetd (Portable INET Daemon) is an Open Source server framework &
daemon written in PHP, allowing anyone to easily create a TCP server,
daemon, etc. You can either use it as a developper, and build your own
application.

%prep
%setup -q -n %{name}

cat > %{name}.sh <<'EOF'
#!/bin/sh
exec /usr/bin/php -d date.timezone=$(date +%Z) %{_appdir}/code/root.php ${1:+"$@"}
EOF

find -name .svn | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_appdir},%{_sysconfdir}/%{name}}
install -p %{name}.sh $RPM_BUILD_ROOT%{_sbindir}/%{name}
cp -a code $RPM_BUILD_ROOT%{_appdir}
cp -a etc/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%dir %{_sysconfdir}/pinetd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pinetd/default_config.xml
%attr(755,root,root) %{_sbindir}/pinetd
%{_appdir}
