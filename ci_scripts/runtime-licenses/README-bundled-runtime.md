# Bundled runtime libraries (macOS wheels)

The macOS (arm64) wheels of `themachinethatgoesping` are compiled with GCC
(installed via Homebrew) because Apple's libc++ does not yet implement
`std::chrono::parse` (LLVM issue #166051).

So that the wheel runs without a separate GCC installation, the following GCC
runtime libraries are bundled inside the wheel (in the per-package `.dylibs`
folder, relinked with delocate/repairwheel):

- **libstdc++** — GNU Standard C++ Library
- **libgcc_s** — GCC low-level runtime support
- **libgomp** — GNU OpenMP runtime

## License of the bundled libraries

These libraries are part of GCC and are licensed under:

    GPL-3.0-or-later WITH GCC-exception-3.1

The *GCC Runtime Library Exception* (version 3.1) grants explicit permission to
distribute these runtime libraries together with independently-licensed
programs, provided the program was produced by an "Eligible Compilation
Process" (i.e. compiled with GCC). That condition is met here. Consequently this
package itself remains licensed under **MPL-2.0**; the exception does not extend
the GPL to it.

Full license texts are included next to this file:

- `GPL-3.0-or-later.txt` — GNU General Public License, version 3
- `GCC-Runtime-Library-Exception-3.1.txt` — GCC Runtime Library Exception 3.1

The complete corresponding source code for the bundled libraries is available
from the GNU Project at <https://gcc.gnu.org/> and via Homebrew
(`brew install gcc`).
