# SPDX-FileCopyrightText: 2022 GEOMAR Helmholtz Centre for Ocean Research Kiel
# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: MPL-2.0

import sys as __internal_module_sysy__
from pkgutil import extend_path as __extend_path__

#append path to the python source folders of themachinethatgoesping subprojects
#each folder contains a subfolder called themachinethatgoesping
for __submodule in pydev_install_modules:
  __internal_module_sysy__.path.append("{}/{}/python/".format(pydev_install_src_path,__submodule))

#append all paths in sys that contain themachinethatgoesping to this package
__path__ = __extend_path__(__path__, __name__)
pydev_install_module_paths = __path__
