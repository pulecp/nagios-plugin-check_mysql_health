# How to build

### RHEL/CentOS:

    yum install make rpm-build autoconf automake libtool
    rpmbuild -ba nagios-plugin-check_mysql_health.spec
    
##### Source: [https://labs.consol.de/nagios/check_mysql_health](https://labs.consol.de/nagios/check_mysql_health)
