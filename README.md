# robofogExport

![RoboFog About Screen](./aboutRoboFog.png)

This is a collection of scripts that will assist extracting font data from old RoboFog files. These script have to run in RoboFog, so you still need [some sort of emulator](http://sheepshaver.cebix.net) or [old computer](https://en.wikipedia.org/wiki/Mac_OS_9).

## Brief reminder of OS9 and Python 1.5

* RoboFog and Python 1.5 did not have any Unicode or UTF-8 support.
* RobofogExport will generates files in Mac encoding.
* RoboFog had no plistlib
* RoboFog had no kerning groups
* RoboFog did not have support for pens
* Background glyphs are exported with a `#` prefix. 
* Export only
* Filenames have a maximum length of around 31 characters.

## Exporting

* Make sure the whole folder is available to Robofog.
* Open a font
* Run the ExportFontToUFO.py script
* Open the UFO in RoboFont. Other UFO-reading apps might also work, but are untested.
* Optionally: run the `finishRoboFogExport.py` script to move background glyphs in the right place.

Ouput might look like this:
```python
Exporting TestRoboFogFile to UFO:
FogUFOExportLib version1.1
making glyph rename table...
	writing .glifs...
writing kerning.plist...
writing fontinfo.plist...
writing metainfo.plist...
writing lib.plist...
Saved at Unix:Users:erik:SharedWithOS9:TestRoboFogFile_RF.ufo
Done!
```

## Credits

RoboFog was a program developed by Petr van Blokland, Just van Rossum, Erik van Blokland, on top of Fontographer 3.5 source material.
