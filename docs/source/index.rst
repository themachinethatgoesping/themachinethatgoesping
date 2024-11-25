.. SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
..
.. SPDX-License-Identifier: MPL-2.0

**********************
themachinethatgoesping
**********************

**themachinethatgoesping** (short: **Ping**) is created to enable advanced processing of multibeam and singlebeam echosounder data. 
Core components of this library are implemented in C++ (for performance) and then exposed as high level python interfaces (for usability). 
On top of the core, many libraries, tools and applications are implemented in Python directly, making use of the fast prototyping features of this language.

Ping is still in early stage. If you are interested in our plans and time line, contact me: peter.urban@ugent.be

.. admonition:: Note
   :class: important
   
   Ping is still in early stage. If you are interested in our plans and time line, contact me: peter.urban@ugent.be

.. _where_to_start:

Where to start?
===============

New to python
-------------

Before you can use **Ping**, you need to install python on your system and understand the basics of the language.
If you are new to python, there are many good tutorials on the internet. We linked some in the :ref:`new_to_python` section.

Once you understand how to install python and python packages on your system, and you are able to execute a tutorial e.g. in a jupyter notebook, you are ready to progress to the next section.

Python user
-----------------------

**Ping** is available on PyPi and can be installed with pip:

.. tab-set::

    .. tab-item:: pip
        :sync: key_pip

        .. code-block:: console

           $ pip install themachinethatgoesping
           
.. admonition:: Conda / mamba
   :class: important

   Currently there are no conda packages available. 
   However, you can install ping with pip in a conda environment. 

If you need help setting up a python environment, see the :ref:`new_to_python` section.
For more details on the installation see :ref:`installation_user`. To install from source see :ref:`installation_from_source`.
To get started with **Ping** check out the :ref:`tutorials_section` section. 
Even if you consider yourself a user, rather than a developer, please check out the :ref:`contribute` section, as it contains some useful information on how to report bugs and request features.

Developer / contributor
-----------------------

If you want to contribute to **Ping** you want to install it from source using `meson <https://mesonbuild.com/>`_ and `ninja <https://ninja-build.org/>`_ (instead of pip). 
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
   :caption: Demos
   :maxdepth: 2
   :hidden:

   demos/tutorial_01_data_access_basic.ipynb
   demos/tutorial_02_data_access_advanced.ipynb
   demos/tutorial_03_WCI_viewer.ipynb
   demos/tutorial_04_extract_wcd.ipynb
   demos/tutorial_05_wedge_view_WCI.ipynb
   demos/tutorial_06_echograms.ipynb

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
