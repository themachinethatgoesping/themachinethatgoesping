.. SPDX-FileCopyrightText: 2023 Peter Urban, Ghent University
..
.. SPDX-License-Identifier: MPL-2.0

.. _installation:

.. _installation_user:

Installation (user)
###################

If you did not yet install python, please refer to the section :ref:`New to python <setting_up_python>` first.
**Ping** is available on PyPi and can be installed with pip. We currently do not provide conda packages. However you can install the package in your conda/mamba environment using pip.

.. tab-set::

    .. tab-item:: mamba
        :sync: key_mamba

        .. code-block:: console

           # Here we assume that the name of the environment is "ping"
           $ mamba activate -n ping

           $ pip install themachinethatgoesping

    .. tab-item:: conda
        :sync: key_conda

        .. code-block:: console

           # Here we assume that the name of the environment is "ping"
           $ conda activate -n ping

           $ pip install themachinethatgoesping

    .. tab-item:: pip
        :sync: key_pip

        .. code-block:: console

           $ pip install themachinethatgoesping
           
If you want to update the package use

.. code-block:: console
   
   $ pip install --upgrade themachinethatgoesping

.. admonition:: Windows / Mac
   :class: note

   While we are building pypi packages for Windows and Mac, support and performance is not guaranteed.
   On windows and MacOS we currently do not support openMP and therefore no multithreading is available.
   Furthermore we currently only create builds for MacOS with the new m-chips.
   If you are experienced with building python packages on windows and mac, please contact us to help us improve the situation.



