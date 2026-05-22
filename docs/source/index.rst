.. SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
..
.. SPDX-License-Identifier: MPL-2.0
.. |logo-DSM| image:: https://www.geomar.de/fileadmin/content/forschen/fb2/mg/deepseamon/DSM-Logo_large_black_trans.gif
   :target: https://www.geomar.de/deepsea-monitoring
   :alt: DeepSea Monitoring Group - GEOMAR
   :height: 30
   
.. |logo-GEOMAR| image:: https://www.geomar.de/fileadmin/_processed_/a/0/csm_geomar_logo_kurz_4c-large_e50ee49df0.jpg
   :target: https://www.geomar.de/
   :alt: GEOMAR Helholtz-Centre for ocean research Kiel
   :height: 25
   
.. |logo-UGent| image:: https://www.ugent.be/++theme++ugent/static/images/logo_ugent_nl.svg
   :target: https://www.ugent.be/nl
   :alt: Ghent University
   :height: 25
   
.. |logo-belspo| image:: https://github.com/themachinethatgoesping/.github/blob/main/profile/BELSPO_logo.jpg
   :target: https://www.belspo.be
   :alt: belspo
   :height: 25

.. |logo-TURBEAMS| image:: https://github.com/themachinethatgoesping/.github/blob/main/profile/turbeams_black.png
   :target: https://hydrogeo.ugent.be/turbeams-about/
   :alt: TURBEAMS
   :height: 15

.. |logo-SSPIRIT| image:: https://github.com/themachinethatgoesping/.github/blob/main/profile/SSPIRIT-transparent.png
   :target: https://hydrogeo.ugent.be/sspirit-about/
   :alt: SSPIRIT
   :height: 25

.. |logo-Urcoustics| image:: https://urcoustics.com/wp-content/uploads/2025/09/urcoustics-1-no-background.svg
   :target: https://urcoustics.com/
   :alt: Urcoustics
   :height: 25
   
**********************
themachinethatgoesping
**********************

**themachinethatgoesping** (short: **Ping**) is created to enable advanced processing of multibeam and singlebeam echosounder data. 
Core components of this library are implemented in C++ (for performance) and then exposed as high level python interfaces (for usability). 
On top of the core, many libraries, tools and applications are implemented in Python directly, making use of the fast prototyping features of this language.

Ping currently supports Kongsberg .all/.wcd, .kmall/.kmwcd and Simrad .raw (EK80) formats. More formats will be added in the future.

.. admonition:: Note
   :class: important
   
   Ping is still in development. If you are interested in our plans and time line, contact me: peter.urban@ugent.be

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

    .. tab-item:: miniforge/mamba
        :sync: key_mamba

        .. code-block:: console

           # Latest development releases are made available on the themachinethatgoesping channel
           $ mamba install themachinethatgoesping -c themachinethatgoesping

    .. tab-item:: anaconda/conda
        :sync: key_mamba

        .. code-block:: console

           # Latest development releases are made available on the themachinethatgoesping channel
           $ conda install themachinethatgoesping -c themachinethatgoesping
           

If you need help setting up a python environment, see the :ref:`new_to_python` section.
For more details on the installation see :ref:`installation_user`. To install from source see :ref:`installation_from_source`.
To get started with **Ping** check out the :ref:`tutorials_section` section. 
Even if you consider yourself a user, rather than a developer, please check out the :ref:`contribute` section, as it contains some useful information on how to report bugs and request features.

Developer / contributor
-----------------------

If you want to contribute to **Ping** you want to install it from source using `meson <https://mesonbuild.com/>`_ and `ninja <https://ninja-build.org/>`_ (instead of pip). 
For details see :ref:`installation_from_source`.
You may also want to check out the :ref:`contribute` section.

Acknowledgements / Funding
==========================

- The code of this project is partly based on code that was written while working for the DeepSea Monitoring Group |logo-DSM| at GEOMAR, Helmholtz Centre for Ocean Research, Kiel, Germany. |logo-GEOMAR|
- Current development is happening at Ghent University, Ghent, Belgium |logo-UGent| within the  |logo-TURBEAMS|  project that is financed by the Belgian Science Policy Office |logo-belspo| and further within the |logo-SSPIRIT| project which enabled i.e. the implementation of the new Kongsberg .kmall file format
- Additional contributions come from |logo-Urcoustics|, a hydroacoustics and software consultancy based in Delft, The Netherlands

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

   demos/demo_01_introduction.ipynb
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
