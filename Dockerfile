FROM centos:7
MAINTAINER Siddharth Bakshi

RUN yum -y install epel-release
RUN yum -y install boinc-client
RUN yum -y clean all
# RUN chmod -R 777 /root/
# RUN chmod -R 777 /var/
# RUN chmod -R 777 /home/
# RUN chmod -R 777 /etc/
# RUN chmod -R 777 /usr/

# COPY /global_prefs_override.xml /

# ENV boincurl www.worldcommunitygrid.org
# ENV boinckey 0306042ebf9cb4311fef19de74b91a2e

CMD usermod -u echo $( cut -d ',' -f 2 <<< "$(id)") newu; boinc --attach_project ${boincurl} ${boinckey}  --allow_multiple_clients