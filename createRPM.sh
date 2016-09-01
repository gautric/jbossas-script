#!/bin/sh

CURRENTDIR=$(pwd)

#Clean
rm -rf rpmbuild/SOURCES/*
rm -rf rpmbuild/BUILD/*
rm -rf rpmbuild/BUILDROOT/*
rm -rf rpmbuild/RPMS/*

#Build package
mkdir jbossas-script
cp -rf bin/* jbossas-script
rm -f jbossas-script/*~
tar -zvcf rpmbuild/SOURCES/jbossas-script.tar.gz jbossas-script
rm -rf jbossas-script

#Build RPM
rpmbuild --define "_topdir ${CURRENTDIR}/rpmbuild" -bb rpmbuild/SPECS/jbossas-script.spec

#Test RPM
# rpm -e jbossas-script
# rpm -Uvh rpmbuild/RPMS/noarch/*.rpm
#cp rpmbuild/RPMS/noarch/*.rpm ~/JBoss/eap/RPMS
