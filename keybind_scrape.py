import argparse
import os
import re
import markdown
import webbrowser

def parse_args():
    parser = argparse.ArgumentParser('i3Key Scaper')
    parser.add_argument('-c', '--config', type=argparse.FileType('r'), default=os.path.expanduser('~/.i3/config'))
    parser.add_argument('-o','--out', type=argparse.FileType('w'), default='-')
    
    args = parser.parse_args();
    
    config = args.config.read()
    args.config.close()
    
    args.config = config
    
    return args

def extract_keybinds(contents):
    return re.findall(r'((#(((?!bindsym)(?!exec).)*?)\n)+(#?\s*bindsym\s\$(mod|alt)(.*?)\s(.*?)\n)+)', contents)

prettify_extract_comments = re.compile(r'#\s*(((?!bindsym).)*?)\r?\n')
prettify_extract_shortcut = re.compile(r'(#?)\s*bindsym\s\$(mod|alt)(.*?)\s(.*)')
def prettify_keybind(keybind):
    comments = '\n'.join([ '## ' + comment[0] for comment in prettify_extract_comments.findall(keybind)]);
    shortcut = '\n'.join([f'- {shortcut[1] +shortcut[2]} -> {shortcut[3]} {( "(not in use)" if shortcut[0] == "#" else "")}' for shortcut in prettify_extract_shortcut.findall(keybind)])
    return f'{comments}:\n{shortcut}';

def process_config(file_contents):
    return '\n\n'.join([prettify_keybind(key[0]) for key in extract_keybinds(file_contents)])
    
def main():
    args = parse_args()
    
    html = markdown.markdown('# i3 Keybinds\n'+process_config(args.config))
    args.out.write(html)
    args.out.close()
    
    if args.out.name != '<stdout>':
        webbrowser.open(args.out.name)
    
    
    
    
    


if __name__ == "__main__":
    main()