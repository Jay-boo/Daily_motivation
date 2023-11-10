#!/bin/bash -e

# NAME: gui-launcher

# Check whether the user is logged-in
while [ -z "$(pgrep gnome-session -n -U $UID)" ]; do sleep 3; done

# Export the current desktop session environment variables
# Sometimes it try to change $UID so we must remove -e option or use 2>/dev/null
export $(xargs -0 -a "/proc/$(pgrep gnome-session -n -U $UID)/environ") 2>/dev/null 

# Execute the input command
# nohup "$@" >/dev/null 2>&1 &
nohup "$@" >> /home/jay/projects/daily_motiv/daily_job.log 2>&1

exit 0
