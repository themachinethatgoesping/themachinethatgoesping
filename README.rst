.. SPDX-FileCopyrightText: 2024 Peter Urban, Ghent University
..
.. SPDX-License-Identifier: MPL-2.0

.. |badge-ci| image:: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/ci.yml
   :alt: CI status
   
.. |badge-docs| image:: https://readthedocs.org/projects/themachinethatgoesping/badge/?version=latest&style
   :target: https://readthedocs.org/projects/themachinethatgoesping/builds/
   :alt: ci-readthedocs
   
.. |badge-ci-buildwheel| image:: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/cibuildwheels.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/cibuildwheels.yml
   :alt: ci-buildwheel
   
.. |badge-ci-python-linux| image:: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/python-package-linux.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/python-package-linux.yml
   :alt: ci-python-linux
   
.. |badge-ci-python-windows| image:: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/python-package-windows.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/python-package-windows.yml
   :alt: ci-python-windows
   
.. |badge-ci-python-mac| image:: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/python-package-mac.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/python-package-mac.yml
   :alt: ci-python-mac
   
.. |badge-license| image:: https://img.shields.io/badge/license:-MPL--2%2E0-green
   :target: https://opensource.org/license/mpl-2-0/
   :alt: license: MPL-2.0
   
.. |badge-themachinethatgoesping| image:: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/themachinethatgoesping/actions/workflows/ci.yml
   :alt: themachinethatgoesping
   
.. |badge-tutorials| image:: https://github.com/themachinethatgoesping/tutorials/actions/workflows/mybinder.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/tutorials/actions/workflows/ci.yml
   :alt: tutorials
   
.. |badge-tools| image:: https://github.com/themachinethatgoesping/tools/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/tools/actions/workflows/ci.yml
   :alt: tools

.. |badge-algorithms| image:: https://github.com/themachinethatgoesping/algorithms/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/algorithms/actions/workflows/ci.yml
   :alt: algorithms
   
.. |badge-navigation| image:: https://github.com/themachinethatgoesping/navigation/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/navigation/actions/workflows/ci.yml
   :alt: navigation
   
.. |badge-echosounders| image:: https://github.com/themachinethatgoesping/echosounders/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/echosounders/actions/workflows/ci.yml
   :alt: echosoudners
   
.. |badge-pingprocessing| image:: https://github.com/themachinethatgoesping/pingprocessing/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/pingprocessing/actions/workflows/ci.yml
   :alt: pingprocessing
   
.. |badge-gridding| image:: https://github.com/themachinethatgoesping/gridding/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/themachinethatgoesping/gridding/actions/workflows/ci.yml
   :alt: gridding
   
.. |info-python| image:: https://img.shields.io/badge/python-3%2E10 | 3%2E11 | 3%2E12 -informational
   :target: https://pypi.org/project/themachinethatgoesping/
   :alt: Python versions 3.10 | 3.11 | 3.12

.. |info-pypi| image:: https://img.shields.io/pypi/v/themachinethatgoesping
   :target: https://pypi.org/project/themachinethatgoesping/
   :alt: PyPI - Version

.. |info-docs| image:: https://img.shields.io/badge/Documentation-readthedocs-informational
   :target: https://themachinethatgoesping.readthedocs.io
   :alt: readthedocs
   
.. |logo-DSM| image:: https://www.geomar.de/fileadmin/content/forschen/fb2/mg/deepseamon/DSM-Logo_large_black_trans.gif
   :target: https://www.geomar.de/deepsea-monitoring
   :alt: DeepSea Monitoring Group - GEOMAR
   :height: 30
   
.. |logo-GEOMAR| image:: https://www.geomar.de/fileadmin/_processed_/a/0/csm_geomar_logo_kurz_4c-large_e50ee49df0.jpg
   :target: https://www.geomar.de/
   :alt: GEOMAR Helholtz-Centre for ocean research Kiel
   :height: 30
   
.. |logo-UGent| image:: https://www.ugent.be/++theme++ugent/static/images/logo_ugent_nl.svg
   :target: https://www.ugent.be/nl
   :alt: Ghent University
   :height: 30
   
.. |logo-belspo| image:: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Logo_BELSPO.jpg/800px-Logo_BELSPO.jpg
   :target: https://www.belspo.be
   :alt: belspo
   :height: 30
   

| |info-python| |info-pypi|

| |badge-license| |info-docs|

themachinethatgoesping
======================

| Super-project for themachinethatgoesping components (https://github.com/themachinethatgoesping)

| Hi there 👋 **themachinethatgosping** (short: **Ping**) aims at enabling advanced processing of multibeam and singlebeam echosounder data. Core components of this library are implemented in C++ (for performance) and are then exposed as high level python interfaces (for usability). On top of the core, many libraries, tools and applications will be implemented in Python directly, making use of the fast prototyping features of this language.
|
| This project is in early stage; at the moment it is just a powerfull raw data reader for Kongsberg .all/.wcd and Simard .raw data. However you can get glimples of what ping will be like and e.g. plot some simple echograms or extract the navigation data from the raw files (see tutorials repository)
|
| More will follow soon. If you are interested in our plans and time line, contact me: peter.urban@ugent.be

installation
============

**Ping** is distributed via pypi. Install e.g. via pip:

.. code-block:: python

  pip install themachinethatgoesping
  
Anaconda packages will follow.

To install ping from source, clone this repository and use pip:

.. code-block:: python
  
  pip install .
  
As a potential developer, you will prefer to use the `meson <https://mesonbuild.com/>`_ backend which provides a propper developer interface. (TODO: check/improve developer build instructions for windows/linux/mac) 
First clone this repository. Then install the build requirements:

.. code-block:: python
  
  pip install -r requirements.txt
  
Then call meson

.. code-block:: python

  meson setup builddir
  meson build -c builddir
  meson install -c builddir
  
WARNING: these instructions are only a preview; they are not yet complete. If you have no experience with meson, contact me: peter.urbam@ugent.be

tutorials
=========

We provide jupyter notebook tutorials with instalation instructions in the tutorials repository: `tutorials <https://github.com/themachinethatgoesping/tutorials>`_

status
######

| |badge-ci|
| |badge-docs|
| |badge-ci-python-linux|
| |badge-ci-python-windows|
| |badge-ci-python-mac|

relevant repositories
#####################

Ping consists of a number of repositories that represent individual modules. It is not necessary to check all of these repositories individually. The **themachinethatgoesping** repository includes all module repositories as subprojects. If you just want to test ping, the tutorials repository includes everything that is necessary.

- |badge-themachinethatgoesping| `themachinethatgoesping <https://github.com/themachinethatgoesping/themachinethatgoesping>`_: superproject that builds and installs all subprojects 

- |badge-tutorials| `tutorials <https://github.com/themachinethatgoesping/tutorials>`_: Tutorial and example notebooks

- |badge-tools| `tools <https://github.com/themachinethatgoesping/tools>`_: Shared functions and interfaces 

- |badge-algorithms| `algorithms <https://github.com/themachinethatgoesping/algorithms>`_: Algorithms for e.g. applying absorption, raytracing, bottomdetection on echograms and more.

- |badge-navigation| `navigation <https://github.com/themachinethatgoesping/navigation>`_: Store and transform navigation data

- |badge-echosounders| `echosounders <https://github.com/themachinethatgoesping/echosounders>`_: Read, write and process single- and multibeam echo sounder files.

- |badge-pingprocessing| `pingprocessing <https://github.com/themachinethatgoesping/pingprocessing>`_: Process ping files (e.g. create echograms).

- |badge-gridding| `gridding <https://github.com/themachinethatgoesping/gridding>`_: Gridding functions (python only test repo) 

license
#######
Most of ping is distributed under the Mozilla Public License Version 2.0 (MPL-2.0)

In simple terms: The MPL-2.0 license implements a non-viral copyleft; Licensed files are protected by the copyleft, but they can still be deeply integrated even in comercial, closed source projects, as long as the file itself stays open source. 

Note that this simplified description is not a legal advice and does not cover all aspects of the license. For this please refer to the license self: https://www.mozilla.org/en-US/MPL/2.0/FAQ/

For other sources that may be easyer to comprehend see also

- https://www.mozilla.org/en-US/MPL/2.0/
- https://fossa.com/blog/open-source-software-licenses-101-mozilla-public-license-2-0/
- https://opensource.org/license/mpl-2-0/

Contributing / Further development / Use
#######################################

This project is still in early stage (bootstrapping). Documentation is mediocore at best. If you are interested in testing/using/contributing to this project, please contact me: peter.urban@ugent.be 

Acknowledgements / Funding
==========================

- The code of this project is partly based on code that was written while working for the DeepSea Monitoring Group |logo-DSM| at GEOMAR, Helmholtz Centre for Ocean Research, Kiel, Germany. |logo-GEOMAR|
- Current development is happening at Ghent University, Ghent, Belgium |logo-UGent| within the TURBEAMS project |logo-TURBEAMS| that is financed by the Belgian Science Policy Office (belspo) |logo-belspo|
