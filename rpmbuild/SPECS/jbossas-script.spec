%global  version     0.9
%global  sp          FP5

Summary:        JBoss Script for JBoss RPM %{version}
Name:           jbossas-script
Version:        %{sp}
Release:        22
License:        none
Source:         %{name}.tar.gz
# This package doesn't contain any binary files so it's architecture independent, hence
# specify noarch for the BuildArch.
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-build
Group:          System/Base
Requires:       java >= 1.7

%description
This package provides some script for JBoss EAP 6.X (RPM mode) %{name} %{version}

%prep
%setup -n %{name}

%build

%install
# create directories where the files will be located
mkdir -p $RPM_BUILD_ROOT%{_datadir}/java

# put the files in to the relevant directories.
# the argument on -m is the permissions expressed as octal. (See chmod man page for details.)
install -m 444 db2jcc.jar $RPM_BUILD_ROOT%{_datadir}/java/db2jcc-%{db2version}-${DB2_BUILD_VERSION}.jar
install -m 444 db2jcc4.jar $RPM_BUILD_ROOT%{_datadir}/java/db2jcc4-%{db2version}-${DB2_4_BUILD_VERSION}.jar

pushd $RPM_BUILD_ROOT%{_datadir}/java
ln -s db2jcc-%{db2version}-${DB2_BUILD_VERSION}.jar db2jcc-%{db2version}.jar
ln -s db2jcc4-%{db2version}-${DB2_4_BUILD_VERSION}.jar db2jcc4-%{db2version}.jar
popd

%post

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_tmppath}/%{name}
rm -rf %{_topdir}/BUILD/%{name}

# list files owned by the package here
%files
%defattr(-,root,root)
%{_datadir}/java/*.jar


%changelog
* Wed Jun 20 2014 First Version
- ${release} 
