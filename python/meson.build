# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# -- python sources --
sources = [
    '__init__.py',
]


if get_option('build_pythonmodule').enabled()

    #install python sources
    foreach source : sources
        fields = source.split('/')

        # add folder path if there is a / in sources
        if fields.length() == 1
            pth = pythoninstallpath
            #subdir = projectnamespace
        else
            pth = pythoninstallpath + source.replace(fields[-1],'/')
            #subdir = projectnamespace + '/' + source.replace(fields[-1],'/')
        endif

        install_data(source, install_dir : pth, install_tag : 'python-runtime')
        #pymod.install_sources(source, subdir : subdir, install_tag : 'python-runtime')
    endforeach



endif

