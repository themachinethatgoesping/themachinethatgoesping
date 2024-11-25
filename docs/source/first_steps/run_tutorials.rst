.. SPDX-FileCopyrightText: 2023 Peter Urban, Ghent University
..
.. SPDX-License-Identifier: MPL-2.0

.. _tutorials_section:

Tutorials
#########

We provide `jupyerlab <https://github.com/jupyterlab/jupyterlab>`_ based tutorials in the `tutorials <https://github.com/themachinethatgoesping/tutorials>`_ repository of themachinethatgoesping.
The repository still needs some cleaning, please be patient and concentrate on the `demo <https://github.com/themachinethatgoesping/tutorials/tree/main/demo>`_ folder for now.

.. _install tutorials and requirements:

**********************************
Install tutorials and requirements
**********************************

To run the tutorials you need to install ping first. You can find the installation instructions `here <installation>`_.
First clone the `tutorials repository <https://github.com/themachinethatgoesping/tutorials>`_ using your favorite git application or the following command:

.. code-block:: console

   $ git clone https://github.com/themachinethatgoesping/tutorials.git

A requirements file is provided in the repository. However, we recommend installing the requirements using poetry to ensure all packages are on a version that was tested.
You can install the tutorial requirements using the following command:

.. tab-set::

    .. tab-item:: miniforge / poetry
        :sync: key_mamba

        .. code-block:: console

            # first enter the tutorials directory
            $ cd tutorials

            # Here we assume that you are using miniforge / mamba and created and environment called "ping"
            $ mamba activate -n ping

            # install poetry
            $ pip install poetry

            # install the requirements fixed in the pyproject.toml and the poetry.lock file
            $ poetry install

    .. tab-item:: anaconda / poetry
        :sync: key_conda

        .. code-block:: console

            # first enter the tutorials directory
            $ cd tutorials

            # Here we assume that you are using conda and created and environment called "ping"
            $ conda activate -n ping

            # install poetry
            $ pip install poetry

            # install the requirements fixed in the pyproject.toml and the poetry.lock file
            $ poetry install
            
    .. tab-item:: anaconda / conda
        :sync: key_conda_pip

        .. code-block:: console

            # first enter the tutorials directory
            $ cd tutorials

            # Here we assume that the name of the environment is "ping"
            $ conda activate -n ping

            # if you want to update the package use
            $ conda install --file requirements.txt

            
    .. tab-item:: minforge / mamba
        :sync: key_mamba_pip

        .. code-block:: console

            # first enter the tutorials directory
            $ cd tutorials

            # Here we assume that the name of the environment is "ping"
            $ mamba activate -n ping

            # if you want to update the package use
            $ mamba install --file requirements.txt
            
    .. tab-item:: pip
        :sync: key_pip

        .. code-block:: console

            # first enter the tutorials directory
            $ cd tutorials

            # if you want to update the package use
            $ pip install -r requirements.txt

.. _run_tutorials:

*************
Run tutorials
*************

You can find the tutorials in the `demo <https://github.com/themachinethatgoesping/tutorials/tree/main/demo>`_ folder of the tutorials `repository <https://github.com/themachinethatgoesping/tutorials>`_.
To open jupyerlab in the demo folder, you can use the following command in the terminal/miniforge prompt:

.. code-block:: console

   $ mamba activate -n ping

   $ cd tutorials/demo

   $ jupyter lab .

The last prompt will open a jupyter lab instance in your browser. You can now open the tutorials and run them.