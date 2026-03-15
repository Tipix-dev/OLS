# installation for OLS

## Quick install
Download the .tar.gz archive from [GitHub Releases](https://github.com/artemkolba321-spec/OLS/releases) and go to it<br>

assemble the assembly
```Bash
make
```
This script installs OLS to `~/.local/share/OLS`<br>
next add to end .bashrc or .zshrc
```Bash
export PATH="$HOME/.local/share/OLS/bin:$PATH"
source "$HOME/.local/share/OLS/lib/env.sh"
```
This is necessary for OLS to work<br>
Then reload your shell:
```Bash
source ~/.bashrc
# or
source ~/.zshrc
```
everything is ready

## more details
### Why `~/.local/share/OLS`
> We decided not to touch the system folders, but we also decided not to go directly into /home, so `~/.local/share/OLS` is a good solution.

