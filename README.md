# clean_downloads.py

A small python script to clean your downloads folder. 

## Dependencies
This script has one dependency, being the python module send2trash.
It can be installed via the following command:

```
  pip install send2trash
```

## Setup:

1. Open clean_downloads.py
2. Change the `PATH` global string variable to ***your*** absolute downloads directory.

## Configuration:

* The `LIST_EXTENSIONS` global variable can be appended with whatever file extensions you would like to filter through and delete.
* By default, clean_downloads.py looks for .zip, .rar, .7z, .png, and .jpg files.

## Execute:
```
  python3 clean_downloads.py
```
