# skribbl-scripts
A collection of scripts for skribbl.io.

# Usage
Go to the command-line, ensure you have installed python, then type:
```bash
$ python3 [script].py [file].py
```

with ```script``` is the python-script, you want to run. and ```file```
is the input file.

For example you can type ```python3 shuffle_wordlist.py skribbl.txt```
with a ```skribbl.txt``` file, which has each word in an separate line.

The script would generate from skribbl.txt with the content of

```
Tree
House
Garden
```

a file namend ```skribbl.txt.shuffle.txt``` with all content,
shuffled and separated by a ```,```, e.g.:

```
House,Tree,Garden,
```
