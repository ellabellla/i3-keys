#!/usr/bin/env python3
"""
    i3-keys
    
    A program to scape the i3 config and display the keybinds in an easy to read format.
    
    Author: Ella Pash
"""
import argparse, os, re, markdown, webbrowser

def parse_args():
    """parse command line arguments and return an input data and an output stream

    Returns:
        config: config file contents
        out: out stream (either stdout or a file)
    """
    parser = argparse.ArgumentParser('i3Key Scraper')
    parser.add_argument('-c', '--config', type=argparse.FileType('r'), default=os.path.expanduser('~/.i3/config'))
    parser.add_argument('-o','--out', type=argparse.FileType('w'), default='-')
    
    args = parser.parse_args();
    
    config = args.config.read()
    args.config.close()
    
    args.config = config
    
    return args

def extract_keybinds(contents):
    """extract each commented keybind block to an array

    Args:
        contents (string): contents of the i3 config

    Returns:
        array: array of tuples containing the matched commented keybind block
    """
    return re.findall(r'((#(((?!bindsym)(?!exec).)*?)\n)+(#?\s*bindsym\s\$(mod|alt)(.*?)\s(.*?)\n)+)', contents)

prettify_extract_comments = re.compile(r'#\s*(((?!bindsym).)*?)\r?\n')
prettify_extract_shortcut = re.compile(r'(#?)\s*bindsym\s\$(mod|alt)(.*?)\s(.*)')
def prettify_keybind(keybind):
    """extract each part of a keybind block and format it into markdown

    Args:
        keybind (string): keybind block

    Returns:
        string: formatted keybind block
    """
    comments = '\n'.join([ '## ' + comment[0] for comment in prettify_extract_comments.findall(keybind)]);
    shortcut = '\n'.join([f'- {shortcut[1] +shortcut[2]} -> {shortcut[3]} {( "(not in use)" if shortcut[0] == "#" else "")}' for shortcut in prettify_extract_shortcut.findall(keybind)])
    return f'{comments}:\n{shortcut}';

def process_config(file_contents):
    """extract all keybind blocks and format them into markdown

    Args:
        file_contents (string): i3 config contents

    Returns:
        string: formatted keybind list
    """
    return '\n\n'.join([prettify_keybind(key[0]) for key in extract_keybinds(file_contents)])
    
def main():
    """generate formatted list of keybind blocks from the i3 config, convert to html then open in a browser
    """
    args = parse_args()
    
    html = markdown.markdown('# i3 Keybinds\n'+process_config(args.config))
    args.out.write(html)
    args.out.close()
    
    if args.out.name != '<stdout>':
        webbrowser.open_new(args.out.name)
    



if __name__ == "__main__":
    main()