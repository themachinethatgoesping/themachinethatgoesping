.. SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
..
.. SPDX-License-Identifier: MPL-2.0

Usage
=====

.. _installation:

Installation
------------
Note, this is all ficitonal at the moment! Themachinethatgoesping is not released or published anywhere.

To use themachinethatgoesping, first install it using pip:

.. code-block:: console

   (.venv) $ pip install themachinethatgoesping

Open files
----------------

To open a file you can use the input library. For Kongsberg .all files e.g.:

For example:

>>> import themachinethatgoesping.echofiles as pingfiles
>>> ifi = pingfiles.KongsbergAll('awesomesurvey.all',progress=True)
>>> ping = ifi['watercolumnping'][0]

