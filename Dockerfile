FROM centos:7
MAINTAINER Siddharth Bakshi

RUN yum -y install epel-release
RUN yum -y install boinc-client
RUN yum -y clean all
RUN chmod -R 777 /root/
RUN chmod -R 777 /var/
RUN chmod -R 777 /home/
RUN chmod -R 777 /etc/
RUN chmod -R 777 /usr/
RUN chmod -R 777 /bin/
RUN chmod -R 777 /lib/
RUN chmod -R 777 /sbin/
# RUN for ID in $(cat /etc/passwd | grep /home | cut -d ':' -f1);  do adduser $ID boinc;done
# RUN chmod 777 /var/lib/boinc/
# RUN chmod 777 /var/lib/boinc/*.*

#echo $( cut -d ',' -f 2 <<< "$(id)")

# COPY /global_prefs_override.xml /

# ENV boincurl www.worldcommunitygrid.org
# ENV boinckey 0306042ebf9cb4311fef19de74b91a2e

CMD boinc --attach_project ${boincurl} ${boinckey} --allow_multiple_clients