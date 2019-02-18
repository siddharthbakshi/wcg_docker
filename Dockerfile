FROM centos:7
MAINTAINER sbakshi

##Install BOINC
RUN yum -y install epel-release
RUN yum -y install boinc-client
RUN yum -y clean all

##Start BOINC
CMD boinc --attach_project ${boincurl} ${boinckey}
