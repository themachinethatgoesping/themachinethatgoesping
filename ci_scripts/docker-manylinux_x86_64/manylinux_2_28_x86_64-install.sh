#!/bin/bash

# install source build dependencies
yum install -y bzip2 curl zlib

#export BOOST_VERSION="1.74.0"
#export BOOST_VERSION_="1_74_0"
export BOOST_VERSION="1.89.0"
export BOOST_VERSION_="1_89_0"
export BOOST_MODULES="--with-iostreams"

export CCACHE_VERSION="4.8.3"


# -- install package versions from source --
# BOOST
echo get https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VERSION}/source/boost_${BOOST_VERSION_}.tar.bz2

curl -O -L https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VERSION}/source/boost_${BOOST_VERSION_}.tar.bz2 && \
    tar -xf boost_${BOOST_VERSION_}.tar.bz2 && \
    cd boost_* && \
    ./bootstrap.sh  && \
    ./b2 install --variant=release --threading=multi --link=static ${BOOST_MODULES} --prefix=/usr/local cxxflags=-fPIC cflags=-fPIC && \
    cd .. && \
    /usr/bin/rm -r boost*


# -- install ccache () --
echo get https://github.com/ccache/ccache/releases/download/v${CCACHE_VERSION}/ccache-${CCACHE_VERSION}-linux-x86_64.tar.xz

curl -O -L https://github.com/ccache/ccache/releases/download/v${CCACHE_VERSION}/ccache-${CCACHE_VERSION}-linux-x86_64.tar.xz
tar -xf ccache-${CCACHE_VERSION}-linux-x86_64.tar.xz
cd ccache-${CCACHE_VERSION}-linux-x86_64
mv ccache /usr/local/bin/
cd ..
/usr/bin/rm -r ccache*

# install build requirements
#yum install -y git git-lfs ccache


# install dependencies (c++)
yum install -y pkgconfig cmake libcurl-devel
