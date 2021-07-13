FROM centos:7

RUN yum install -y yum-utils
RUN yum-builddep -y python3
RUN yum install -y make gcc configure pkgconfig

ADD cpython /code
WORKDIR /code

RUN ./configure --with-pydebug
RUN make regen-grammar
RUN make -j2 -s
