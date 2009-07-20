Summary:	Shoreline Firewall - an iptables-based firewall for Linux systems
Summary(pl.UTF-8):	Shoreline Firewall - zapora sieciowa oparta na iptables
Name:		shorewall-shell
Version:	4.2.10
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://shorewall.net/pub/shorewall/4.2/shorewall-%{version}/%{name}-%{version}.tgz
URL:		http://www.shorewall.net/
Requires(post,preun):	/sbin/chkconfig
Requires:	bash
Requires:	iproute2
Requires:	iptables
Requires:	rc-scripts
Provides:	shorewall-compiler
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Shoreline Firewall, more commonly known as "Shorewall", is an easy
to use Netfilter (iptables) based firewall that can be used on a
dedicated firewall system, a multi-function gateway/ router/server or
on a standalone GNU/Linux system.

This package provides the shell compiler for shorewall rules.

%description -l pl.UTF-8
Pakiet Shoreline Firewall, nazywany zwykle Shorewall, jest zaporą
sieciową opartą na wbudowanych w jądro Linuksa mechanizmach
filtrowania pakietów sieciowych (iptables). Shorewall jest bardzo
wszechstronny i może być wykorzystany jako zapora sieciowa,
wielofunkcyjna brama lub router. Pakiet ten łączy w sobie elastyczność
i prostotę konfiguracji.

Ten pakiet dostarcza kompilatora reguł shorewalla opartego na powłoce.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

export PREFIX=$RPM_BUILD_ROOT ; \
export OWNER=`id -n -u` ; \
export GROUP=`id -n -g` ;\
./install.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_usr}/share/%{name}
%attr(755,root,root) %{_usr}/share/%{name}/compiler
%{_usr}/share/%{name}/*
