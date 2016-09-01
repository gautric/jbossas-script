#
# This script provides completion stuff for jboss script
#

_jbossInstanceList()
{
    JBOSS_EAP6_DEFAULT_SYSCTL_SERVICE=${JBOSS_EAP6_DEFAULT_SYSCTL_SERVICE:-"/usr/share/jbossas-script/jbossas.service"}
    [ ! -f ${JBOSS_EAP6_DEFAULT_SYSCTL_SERVICE} ] && return ;
    find  /lib/systemd/system/* -xtype l -follow -inum `ls -i ${JBOSS_EAP6_DEFAULT_SYSCTL_SERVICE} | awk '{print $1}'` | sed "s/.*@//" | sed "s/\.service//"
}

_jbossStartedInstance()
{
   EXECUTE=`ps -elf | grep "[Standalone]"  `
   RET=""
   for var in $EXECUTE
   do
     # Remove quotes
     p=`echo $var | tr -d '"'`
     case $p in
       -Djboss.server.name=*)
         RET="$RET $(echo $p | cut -f2 -d=)"
       ;;
     esac
   done
   echo $RET
}

_incrementLastInstance()
{
    LAST_INSTANCE=$(_jbossInstanceList | sort -n | tail -n1)
    NUMBER=$(echo $LAST_INSTANCE |  sed "s/.*[^0-9]//g")
    NUMBER_1=`expr $NUMBER + 1`
    SIZE=`expr length $NUMBER`
    SIZE_1=`expr length $NUMBER_1`
    DIFF=$(expr $SIZE_1 - $SIZE | sed 's/-//')
    for i in `seq $DIFF`; do NUMBER_1="0${NUMBER_1}"; done
    echo $LAST_INSTANCE | sed "s/\(.*\)$NUMBER/\1$NUMBER_1/"
}

_autoCompleteInstanceList()
{
    COMPREPLY=( $(compgen -W "$(_jbossInstanceList)" -- $cur) )
}

_jboss()
{
    local cur=${COMP_WORDS[COMP_CWORD]}
    local prev=${COMP_WORDS[COMP_CWORD-1]}

    case "$prev" in
        jboss)
            if [ -z "$(_jbossInstanceList)" ] ;
            then
                COMPREPLY=( $(compgen -W "create" -- $cur) )
            else
                COMPREPLY=( $(compgen -W "create delete clean start stop status list adduser" -- $cur) )
            fi
        return 0
        ;;


        create)
            if [ -z "$(_jbossInstanceList)" ] ;
            then
                COMPREPLY=( $(compgen -W "eap-01 eap-001 eap-0001" -- $cur) )
            else
                COMPREPLY=( $(compgen -W "$(_incrementLastInstance)" -- $cur) )
            fi
        return 0
        ;;

        start)
            _autoCompleteInstanceList
        return 0
        ;;

        stop)
            COMPREPLY=( $(compgen -W "$(_jbossStartedInstance)" -- $cur) )
        return 0
        ;;

        clean)
            _autoCompleteInstanceList
        return 0
        ;;

        delete)
            _autoCompleteInstanceList
        return 0
        ;;

        list)
             COMPREPLY=( $(compgen -W "running all" -- $cur) )
        return 0
        ;;

        status)
            _autoCompleteInstanceList
        return 0
        ;;
    esac
}

complete -F _jboss jboss
