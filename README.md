jbossas-script
==============

Script for JBoss EAP 6.X 

need JBoss EAP 6.2+ installed with RPM (cf Red Hat for details)

scripts provide command to :
 

Directory source projet layout 

 * bin  : scripts 
 * rpmbuild : rpm build directory


JBoss Standalone Instance layout 

def : instanceName

 * /etc/init.d/${instanceName} : Init.d script link to jbossas script
 * /etc/sysconfig/${instanceName} : System config for the instance (binding, JAVA_OPTS, MODULEPATH etc...)
 * /etc/jbossas/${instanceName} : JBoss instance configuration (user, standalone.xml)
 * /var/lib/jbossas/${instanceName} : JBoss instance woking directory
 * /usr/share/jbossas/bin/${instanceName}.sh : startup script
 
