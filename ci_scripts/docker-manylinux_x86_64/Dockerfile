#!/bin/bash

# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

FROM quay.io/pypa/manylinux2014_x86_64
LABEL maintainer="Peter Urban <peter.urban@ugent.be>"

ADD manylinux2014-install.sh manylinux2014-install.sh
RUN bash manylinux2014-install.sh

RUN yum install -y git git-lfs ccache
#
# # package versions
# ARG BOOST_VERSION=1.74.0
# ARG BOOST_VERSION_=1_74_0
# ARG BOOST_MODULES="filesystem"
#
#
# # install source build dependcies
# RUN yum install -y bzip2 curl zlib
#
#
# # -- install package versions from source --
# # BOOST
# RUN curl -O -L https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VERSION}/source/boost_${BOOST_VERSION_}.tar.bz2 && \
#     tar -xf boost_${BOOST_VERSION_}.tar.bz2 && \
#     cd boost_* && \
#     ./bootstrap.sh --with-libraries=${BOOST_MODULES} && \
#     ./b2 install --variant=release --threading=multi --link=static && \
#     cd .. && \
#     rm -rv boost*
#
#
# # install build requirements
# RUN yum install -y git git-lfs
#
# # install dependecies (c++)
# RUN yum install -y ccache pkgconfig cmake libcurl-devel


# install dependcies (meson & python)
# this is best done in the ci scripts!
# ENV PATH "/opt/_internal/cpython-3.10.4/bin:$PATH"
# RUN python3.10 -m pip install --upgrade pip
# RUN python3.10 -m pip install --upgrade meson ninja pytest build twine auditwheel
