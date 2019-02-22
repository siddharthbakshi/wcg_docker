FROM centos:7
MAINTAINER Siddharth Bakshi

RUN yum -y install epel-release
RUN yum -y install boinc-client
RUN yum -y clean all
RUN chmod -R 777 ./

# COPY /global_prefs_override.xml /

# ENV boincurl www.worldcommunitygrid.org
# ENV boinckey 0306042ebf9cb4311fef19de74b91a2e

CMD boinc --attach_project ${boincurl} ${boinckey}  --allow_multiple_clients