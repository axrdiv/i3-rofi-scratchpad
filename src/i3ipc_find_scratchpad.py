import i3ipc
from rofi import Rofi

i3 = i3ipc.Connection()
scratchpad_windows = []
for leaf in i3.get_tree().scratchpad().leaves():
    scratchpad_windows.append(leaf)

if len(scratchpad_windows):
    #  sort by window's name
    scratchpad_windows = sorted(scratchpad_windows, key=lambda x: x.ipc_data['name'])

    r = Rofi()
    scratchpad_windows_name = list(map(lambda x: x.ipc_data['name'], scratchpad_windows))
    index, _ = r.select('Select Window in Scratchpad', scratchpad_windows_name)
    r.close()

    # select == -1 means nothing select
    if index != -1:
        scratchpad_windows[index].command('focus')
else:
    r = Rofi()
    r.exit_with_error('  Nothing in Scratchpad.')
