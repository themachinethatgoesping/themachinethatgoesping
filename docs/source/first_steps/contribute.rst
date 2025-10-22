.. SPDX-FileCopyrightText: 2023 Peter Urban, Ghent University
..
.. SPDX-License-Identifier: MPL-2.0

.. _contribute:

Contribute
##########

.. admonition:: ToDo
   :class: admonition-todo

   This page still has to be written. .. Just contact me if you want to contribute: peter.urban@ugent.be :-)

.. _installation_from_source:

Installation from source (developer)
####################################

If you want to contribute to the development of **Ping** or if you want to use the latest features, you can install **Ping** from source. However, this requires a few more steps than installing from PyPi.

.. admonition:: Building on Windows / Mac
   :class: note

   We have no build instructions for Windows and Mac. (Except as github action workflows)
   If you are experienced with building c++ libraries on Windows or Mac, please contact us to help us improve the situation.

Installation on Linux (24.04 and above)
----------------------------------------

First install the build requirements:

.. tab-set::

    .. tab-item:: Ubuntu (24.04 or higher)
        :sync: key_ubuntu

        .. code-block:: console

           $ sudo apt update
           $ sudo apt install git git-lfs build-essential ccache pkg-config cmake libboost-all-dev libcurl4-openssl-dev

    .. tab-item:: Arch linux
        :sync: key_pipenv

        .. code-block:: console

           $ sudo pacman -Syu
           $ sudo pacman -Syy sudo git git-lfs base-devel ccache pkg-config cmake python-pip boost curl

Get the code:

.. tab-set::

    .. tab-item:: HTTPS
        :sync: key_github_https

        .. code-block:: console

           $ git clone https://github.com/themachinethatgoesping/themachinethatgoesping.git
           $ cd themachinethatgoesping

    .. tab-item:: SSH
        :sync: key_github_ssh

        .. code-block:: console

           $ git clone git@github.com:themachinethatgoesping/themachinethatgoesping.git
           $ cd themachinethatgoesping

With the pip/conda/mamba of your python environment (see :ref:`new_to_python`) install the build requirements

.. tab-set::

    .. tab-item:: pip
        :sync: key_pip

        .. code-block:: console

           $ pip install -r build-requirements.txt

    .. tab-item:: pipenv
        :sync: key_pipenv

        .. code-block:: console

           $ pipenv install -r build-requirements.txt

    .. tab-item:: conda
        :sync: key_conda

        .. code-block:: console

           $ conda install --file build-requirements.txt

    .. tab-item:: mamba
        :sync: key_mamba

        .. code-block:: console

           $ mamba install --file build-requirements.txt

**Ping** is using `meson <https://mesonbuild.com/>`_ as build system. Meson is installed via pip (it is in the build-requirements.txt)
To setup meson run (within the source directory):

.. code-block:: console

   $     meson setup builddir -Dunity=on -Dunity_size=9999999 
   
This will create a build directory called ``builddir``. You can change the name of the build directory to your liking. 
For general build options refer to the `meson documentation <https://mesonbuild.com/Reference-manual.html>`_.

To compile the project run:

.. code-block:: console

   $     meson compile -C builddir

To run the tests (c++/Catch2) run:

.. code-block:: console

   $     meson test -C builddir/ --print-errorlogs

To install the project run (by default into the side-packages in your python environment):

.. code-block:: console

   $     meson install -C builddir/

To run the tests (python/pytest) run (within the source directory):

.. code-block:: console

   $     pytest
           

.. admonition:: ToDo
   :class: admonition-todo

   Provide an overview of import build options. E.g.

   - pydev_install
   - install_env


.. admonition:: ToDo
   :class: admonition-todo

   Describe building python package with meson-python