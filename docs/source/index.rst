.. SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
..
.. SPDX-License-Identifier: MPL-2.0

**********************
themachinethatgoesping
**********************

**themachinethatgoesping** (short: **ping**) aims at enabling advanced processing of multibeam and singlebeam echosounder data. 
Core components of this library are implemented in C++ (for performance) and are then exposed as high level python interfaces (for usability). 
On top of the core, many libraries, tools and applications will be implemented in Python directly, making use of the fast prototyping features of this language.

More will follow soon. If you are interested in our plans and time line, contact me: peter.urban@ugent.be

.. admonition:: Note
   :class: important

   This project is in early stage; at the moment it is just a powerful raw data reader for Kongsberg .all/.wcd and Simard .raw data. 
   However you can already get a glimpse of what ping will be like and e.g. plot some simple echograms or extract the navigation data from the raw files (see tutorials repository)

.. _where_to_start:

Where to start?
===============

New to python
-------------

Before you can use **ping**, you need to install python on your system and understand the basics of the language.
If you are new to python, there are many good tutorials on the internet. We linked some in the :ref:`new_to_python` section.

Once you understand how to install python and python packages on your system, and you are able to execute a tutorial e.g. in a jupyter notebook, you are ready to progress to the next section.

Python user
-----------------------

**Ping** is available on PyPi and can be installed with pip or pipenv:

.. tab-set::

    .. tab-item:: pip
        :sync: key_pip

        .. code-block:: console

           $ pip install themachinethatgoesping

    .. tab-item:: pipenv
        :sync: key_pipenv

        .. code-block:: console

           $ pipenv install themachinethatgoesping
           
.. admonition:: Conda / mamba
   :class: important

   Currently there are no conda packages available. 
   However, you can install ping with pip in a conda environment. 
   Conda forge packages will follow in the future.

For more installation options (e.g. from source) see :ref:`installation_user`. 
To get started with **ping** check out the :ref:`run_tutorials` section. 
Even if you consider yourself a user, rather than a developer, please check out the :ref:`contribute` section, as it contains some useful information on how to report bugs and request features.

Developer / contributor
-----------------------

If you want to contribute to **ping** you want to install it from source using `meson <https://mesonbuild.com/>`_ and `ninja <https://ninja-build.org/>`_ (instead of pip). 
For details see :ref:`installation_from_source`.
You may also want to check out the :ref:`contribute` section.

.. toctree::
   :caption: First steps
   :maxdepth: 2
   :hidden:

   Where to start<self>
   first_steps/new_to_python
   first_steps/installation
   first_steps/run_tutorials
   first_steps/contribute

.. toctree::
   :caption: How to
   :maxdepth: 2
   :hidden:

.. toctree::
   :caption: Module usage
   :maxdepth: 2
   :hidden:

   usage/navigation_data_processing

.. toctree::
   :caption: Module Api
   :maxdepth: 2
   :hidden:

   modules/tools
   modules/navigation
   modules/gridding
