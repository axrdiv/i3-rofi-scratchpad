import i3ipc
from itertools import compress

i3 = i3ipc.Connection()
workspaces = i3.get_workspaces()
current_workspace = workspaces[[x.ipc_data['focused'] for x in workspaces].index(True)]

descends = i3.get_tree().find_by_id(current_workspace.ipc_data['id']).descendants()

scratchpad_states = [x.ipc_data['scratchpad_state'] != 'none' for x in descends]
for desc in compress(descends, scratchpad_states):
    if not desc.ipc_data['nodes'][0]['sticky']:
        desc.command("move scratchpad")
