## Explorer Links

The purpose of this plugin is to add a button to the file explorer built into chrome that lets you open the windows file explorer in the current directory.

![Screenshot](/screenshots/01.png)

To use this plugin, we must create a custom scheme for opening files in explorer. We to link the python script to the `customfile://` scheme in the Registry.

To do this, we add the structure

- "Computer\HKEY_CLASSES_ROOT\customfile\shell\open\command" in the registry.
- the `customfile` directory gets additionally to the default value a string containing "URL Protocol".
- the `command` directory gets the following **default** value: 
> "python" "\[ABSOLUTE PATH TO THIS DIRECTORY\]\handler.py" "%1" 