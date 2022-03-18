# i3-keys
Generates a keybinding help page from your i3 config.

Written By Ella Pash

## Explanation
It scrapes the i3 config file for all keybindings, formats them in html and then opens it in a browser.

The script does this by assuming your keybindings are organized into blocks with comments as headings.
e.g.
```
# change borders
bindsym $mod+u border none
bindsym $mod+y border pixel 1
bindsym $mod+n border normal
```
It will then extract each block into a section on the output page with the comment as the heading and the keybindings listed below.
e.g.
```
change borders:
 - mod+u -> border none
 - mod+y -> border pixel 1
 - mod+n -> border normal
```

## Usage
Simply group all your keybindings in your i3 config into blocks with headings like this:
 ```
# change borders
bindsym $mod+u border none
bindsym $mod+y border pixel 1
bindsym $mod+n border normal
```
Then run the script to generate a keybinding help page.

The script takes two optional arguments:
- -c or --config 
  - specifies the i3 config file
  - by default set to "~/.i3/config"
- -o or --output
  - specifies the output file
  - by default set to stdout

## Install
Simply run the script or add the following to your i3 config to create a help shortcut.
```
bindsym $mod+Shift+h exec python3 path-to-script/i3-keys.py --out path-to-script/out.html &
```

# License
The following project is under the MIT license. Click [here](LICENSE) to view it.