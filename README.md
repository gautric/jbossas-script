#Script for JBoss EAP 6.X 

JBoss EAP 6.2+ installed with RPM (cf Red Hat for details) needed.

### Scripts provide command to :

* *jboss create ${instanceName}*
* *jboss start ${instanceName}*
* *jboss stop ${instanceName}*
* *jboss delete ${instanceName}*
* *jboss clean ${instanceName}*
* *jboss adduser ${instanceName}*
 
Bash Auto Completion is also provide
 

### Directory source projet layout 

 * *bin  : scripts*
 * *rpmbuild : rpm build directory*

### JBoss Standalone Instance layout 

def : instanceName

* */etc/init.d/${instanceName}* : Init.d script link to jbossas script
* */etc/sysconfig/${instanceName}* : System config for the instance (binding, JAVA_OPTS, MODULEPATH etc...)
* */etc/jbossas/${instanceName}* : JBoss instance configuration (user, standalone.xml)
* */var/lib/jbossas/${instanceName}* : JBoss instance working directory
* */usr/share/jbossas/bin/${instanceName}.sh* : startup script
* */var/log/jbossas/${instanceName}* : log directory
* */var/cache/jbossas/${instanceName}* : tmp directory


