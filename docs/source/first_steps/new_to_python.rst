.. SPDX-FileCopyrightText: 2023 Peter Urban, Ghent University
..
.. SPDX-License-Identifier: MPL-2.0

.. _new_to_python:

New to python
#############

This page is intended for people who are new to Python. It will give a brief
introduction to setting up a working Python environment. Once you have a working
Python environment, you can start learning Python by following the tutorials:

- **Python Tutorial**: `https://docs.python.org/3/tutorial/index.html` The official Python tutorial provided by the Python Software Foundation.
- **Python Crash Course:** https://ehmatthes.github.io/pcc/: A beginner-friendly tutorial that covers the basics of Python programming.
- **Learn Python:** https://www.learnpython.org/: An interactive tutorial that allows you to write and run Python code directly in your browser.
- **Codecademy Python:** https://www.codecademy.com/learn/learn-python: A comprehensive Python course with interactive exercises and projects.

These tutorials will help you learn the fundamentals of Python and get you started on your programming journey. Enjoy learning Python!

.. admonition:: Note
   :class: admonition-note
   Please note that we do not take any responsibility for the content in external links. Use them at your own discretion.

********************************************
Setting up a Python environment (Mambaforge)
********************************************

There is different ways to setting up a python environment, here we will use mambaforge. 
Other possibilities would be to use Anaconda, Miniconda, poetry or the python package manager pip or pipenv.
Mamba is a reimplementation of the conda package manager in C++ and is designed to be compatible with conda.
We use mamba instead of conda because it is faster and more reliable when dealing with packages from conda-forge.

.. admonition:: Windows / Mac
   :class: note

   While we are building pypi packages for Windows and Mac, support and performance is not guaranteed.
   On windows and MacOS we currently do not support openMP and therefore no multithreading is avaliable.
   Furthermore we currently only create builds for MacOS with the new m-chips.
   If you are experienced with building python packages on windows and mac, please contact us to help us improve the situation.


First download the mambaforge installer from the following link: https://conda-forge.org/miniforge/
use the Mambaforge installer that fits your system. E.g. 

- Mambaforge-<latest version number>-Windows-x86_64.exe for Windows.
- Mambaforge-<latest version number>-Linux-x86_64.sh for Linux.
- Mambaforge-<latest version number>-MacOSX-arm64.sh for macos (m-chips).

Run the installer and follow the instructions. On linux/mac open a terminal and make sure that the mamba executable is in your path.
On windows you can use the miniforge prompt to open a terminal with run mamba.

Best practice when dealing with mamba/conda environments is to keep the base environment clean and create new environments for each project.
To create a new environment with the name 'ping' with mamba that uses python 3.12 use the following command:

.. code-block:: console

   $ mamba create -n ping python==3.12

once the environment is created you can activate it with the following command:

.. code-block:: console
   $ mamba activate ping

Once activated all packages that you install with mamba (or pip) will be installed only in the 'ping' environment without affecting other environments.

To update packages with mamba use the following command:

.. code-block:: console
   $ mamba upgrade --all

Remember that the upgrade command will update all packages in the current environment. 
To upgrade mamba itself you thus have to run it in the base environment. To upgrade packages in the 'ping' environment you have to activate it first.
