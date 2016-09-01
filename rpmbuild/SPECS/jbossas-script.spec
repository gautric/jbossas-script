%global version 1.0

Summary:        JBoss Script for JBoss RPM %{version}
Name:           jbossas-script
Version:        %{version}
Release:        31
License:        GPL
Source:         %{name}.tar.gz
# This package doesn't contain any binary files so it's architecture independent, hence
# specify noarch for the BuildArch.
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-build
Group:          System/Base
Requires:       java >= 1.7
Requires:       bash
Requires:       coreutils

%description
This package provides some script for JBoss EAP 6.X (RPM mode) and RHEL 7 %{name} %{version}

%prep
%setup -n %{name}

%build

%install
rm -rf ${RPM_BUILD_ROOT}

# Directory structure
mkdir -p ${RPM_BUILD_ROOT}/etc/bash_completion.d
mkdir -p ${RPM_BUILD_ROOT}/etc/profile.d
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/usr/share/jbossas-script
mkdir -p ${RPM_BUILD_ROOT}/usr/share/jbossas-config

# Copy
install -m 755 jboss 		${RPM_BUILD_ROOT}/usr/share/jbossas-script
install -m 755 jbossas.sh 	${RPM_BUILD_ROOT}/usr/share/jbossas-script

install -m 444 functions 		                ${RPM_BUILD_ROOT}/usr/share/jbossas-script
install -m 444 etc_sysconfig_intanceName    ${RPM_BUILD_ROOT}/usr/share/jbossas-script
install -m 444 jbossas.service              ${RPM_BUILD_ROOT}/usr/share/jbossas-script

install -m 755 jbossCreateInstance 	        ${RPM_BUILD_ROOT}/usr/share/jbossas-script
install -m 755 jbossDeleteInstance	        ${RPM_BUILD_ROOT}/usr/share/jbossas-script
install -m 755 jbossListConfiguration 	    ${RPM_BUILD_ROOT}/usr/share/jbossas-script
install -m 755 jbossListInstance 	          ${RPM_BUILD_ROOT}/usr/share/jbossas-script
install -m 755 jbossStopInstance 	          ${RPM_BUILD_ROOT}/usr/share/jbossas-script
install -m 755 _jboss_complete.bash         ${RPM_BUILD_ROOT}/usr/share/jbossas-script

# Symbolic link
pushd ${RPM_BUILD_ROOT}/usr/bin
ln -s /usr/share/jbossas-script/jboss jboss
popd

pushd ${RPM_BUILD_ROOT}/etc/profile.d
ln -s /usr/share/jbossas-script/jbossas.sh jbossas.sh
popd

pushd ${RPM_BUILD_ROOT}/usr/share/jbossas-config
ln -s /etc/jbossas/standalone standalone
popd

pushd ${RPM_BUILD_ROOT}/etc/bash_completion.d
ln -s /usr/share/jbossas-script/_jboss_complete.bash jboss_complete.bash
popd



%post

%clean
rm -rf ${RPM_BUILD_ROOT}
rm -rf %{_tmppath}/%{name}
rm -rf %{_topdir}/BUILD/%{name}

# list files owned by the package here
%files
%defattr(755,root,root)
/etc/profile.d/jbossas.sh
/usr/bin/jboss
/etc/bash_completion.d/jboss_complete.bash
%{_datadir}/jbossas-script/*
%{_datadir}/jbossas-config/*

%changelog
* Fri Jun 20 2014 First Version
- ${release}
