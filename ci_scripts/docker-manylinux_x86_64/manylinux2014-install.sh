#!/bin/bash

# install source build dependcies
yum install -y bzip2 curl zlib

export BOOST_VERSION="1.74.0"
export BOOST_VERSION_="1_74_0"
export BOOST_MODULES="--with-filesystem"

echo get https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VERSION}/source/boost_${BOOST_VERSION_}.tar.bz2

# -- install package versions from source --
# BOOST
curl -O -L https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VERSION}/source/boost_${BOOST_VERSION_}.tar.bz2 && \
    tar -xf boost_${BOOST_VERSION_}.tar.bz2 && \
    cd boost_* && \
    ./bootstrap.sh  && \
    ./b2 install --variant=release --threading=multi --link=static ${BOOST_MODULES} -d0 && \
    cd .. && \
    rm -r boost*

# install build requirements
#yum install -y git git-lfs ccache


# install dependecies (c++)
yum install -y pkgconfig cmake libcurl-devel
