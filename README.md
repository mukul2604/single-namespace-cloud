CLIs
====

CLI to add, remove files from our system
----------------------------------------
The idea is to not give control to the user which cloud his data is going to.
That detail is useless for the user particularly if we are claiming to manage
data storage based on network conditions.

cf add <filename>
cf remove <filename>
cf add -i <filename>
cf add --imp <filename>


CLI to view current namespace - Basically ls like command
---------------------------------------------------------
This should show the entire namespace
cf ls

This should list the entire namespace segragated by which cloud profile has what
This will be useful for the demo
cf ls -s
cf ls --seg


TODO
====
CLI runs then exits
Who will our CLI ask the network stats from:
        A running process - Who starts it? What happens if it crashed?
        Read from a file that a background process keeps updating - Synchronization

Automatic background running server which updates files on the cloud or resurects them
