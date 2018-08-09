## How to build

RHEL/CentOS:

    yum install make rpm-build autoconf automake libtool
    rpmbuild -ba nagios-plugin-check_mysql_health.spec
