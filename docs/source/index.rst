.. SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
..
.. SPDX-License-Identifier: MPL-2.0

Welcome to themachinethatgoesping's documentation!
==================================================


**themachinethatgoesping** (short: ping)  is about to become a set Python libraries for enabling advanced processing strategies for multibeam and singlebeam echosounder data.
Our approach is to implement core components of this library in C++ and create python interfaces using pybind11.
The functionality of the c++ core components will thus also be accessibly both, from C++ and Python.
However, many libraries, tools and applications will be implemented in Python directly, making use of the fast prototyping features of this language.

Most of the libraries will be released using the Mozilla Public License 2.0 (MPL 2.0) which implements a non-infecting copyleft on file basis. It should thus be compatible with proprietary applications, with GPL >2.0 but also MIT and BSD projects (if the license of the files is not changes). More detailed information will follow soon.

We just started with the development, so don't expect to many useful features yet.
If you are interested, contact peter.urban@ugent.be

Check out the :doc:`usage` section for further information (future)
how to :ref:`installation` the project (future).

.. note::

   This project is under active development. Actually, as state of 06/2022 it does not really exist yet :-)

Contents
--------

.. toctree::

   usage
   api

.. toctree::
   :caption: Usage
   :maxdepth: 2

   usage/navigation_data_processing

.. toctree::
   :caption: Module Api
   :maxdepth: 2

   modules/tools
   modules/navigation
   modules/gridding
