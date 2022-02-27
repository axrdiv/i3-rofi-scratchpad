# i3-rofi-scratchpad
`i3-rofi-scratchpad` help you using rofi to select scratchpad windows.

![i3-rofi-scratchpad](./img/i3-rofi.gif)

## Requirements
- Rofi
- i3ipc
    `pip install i3ipc`
- python-rofi
    `pip install python-rofi`

## Installation
Copy python files to i3 config folder (e.g. `~/.i3/`).
```bash
cd i3-rofi-scratchpad/src
cp * ~/.i3/
```
Then modify i3 config file.
```
bindsym $mod+x exec --no-startup-id "python ~/.i3/i3ipc_find_scratchpad.py"
bindsym $mod+minus exec "python ~/.i3/i3ipc_hide_all_scratchpad_window.py"
```
