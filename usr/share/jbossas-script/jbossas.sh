
EXECUTE=`ps -elf | grep "/bin/sh -c export JAVA_HOME" | grep "standalone.sh" `

for var in $EXECUTE
do
  # Remove quotes
  p=`echo $var | tr -d '"'`
  case $p in         
    -Djboss.server.name=*)
      JBOSS_SERVER_NAME=`echo $p | cut -f2 -d=`
    ;;
  esac
done

[ -f /etc/sysconfig/${JBOSS_SERVER_NAME} ] && . /etc/sysconfig/${JBOSS_SERVER_NAME} && export JBOSS_MODULEPATH=${JBOSS_MODULEPATH}

