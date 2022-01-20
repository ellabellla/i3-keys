rm ~/tmp/out.html
touch ~/tmp/out.html
python3 ~/projects/i3-keys/keybind_scrape.py --out ~/tmp/out.html
google-chrome-stable ~/tmp/out.html