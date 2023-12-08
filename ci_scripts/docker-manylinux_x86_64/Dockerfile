#!/bin/bash

# SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

#FROM quay.io/pypa/manylinux2014_x86_64
FROM quay.io/pypa/manylinux_2_28_x86_64
LABEL maintainer="Peter Urban <peter.urban@ugent.be>"

RUN yum makecache --refresh

# manual package versions
ARG BOOST_VERSION="1.82.0"
ARG BOOST_VERSION_="1_82_0"
ARG BOOST_MODULES="--with-iostreams --with-filesystem"

ARG CCACHE_VERSION="4.7.5"

# install source build dependencies
RUN yum update -y
RUN yum install -y git git-lfs
RUN yum install -y bzip2 curl zlib
RUN yum install -y pkgconfig cmake
#RUN yum install -y proj
RUN yum install -y gcc-toolset-12

# -- install package versions from source --
# BOOST
RUN curl -O -L https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VERSION}/source/boost_${BOOST_VERSION_}.tar.bz2
RUN tar -xf boost_${BOOST_VERSION_}.tar.bz2
RUN cd boost_${BOOST_VERSION_} && ./bootstrap.sh
RUN cd boost_${BOOST_VERSION_} && ./b2 install --variant=release --threading=multi --link=static ${BOOST_MODULES} cxxflags=-fPIC cflags=-fPIC
#RUN /usr/bin/rm -r boost*


# -- install ccache () --
RUN curl -O -L https://github.com/ccache/ccache/releases/download/v${CCACHE_VERSION}/ccache-${CCACHE_VERSION}-linux-x86_64.tar.xz
RUN tar -xf ccache-${CCACHE_VERSION}-linux-x86_64.tar.xz
RUN mv ccache-${CCACHE_VERSION}-linux-x86_64/ccache /usr/local/bin/ -v
#RUN /usr/bin/rm -r ccache*

# --- for testing the image --
# # install dependencies (meson & python)
# # this is best done in the ci scripts!
# ENV PATH "/opt/_internal/cpython-3.10.4/bin:$PATH"
# RUN python3.10 -m pip install --upgrade pip
# RUN python3.10 -m pip install --upgrade meson ninja pytest build twine auditwheel
#
# # test the installation
# RUN git clone https://github.com/themachinethatgoesping/themachinethatgoesping.git --recursive -j2
# RUN cd themachinethatgoesping && python3.10 -m build -w .
