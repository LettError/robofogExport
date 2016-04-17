
# finish the export from RoboFog.

"""

    put the background glyphs in the right place

"""

def cleanupBackground(f):
    moved = []
    for g in f:
        if g.name[0] == "#":
            # do we have a foreground companion?
            other = g.name.replace("#", "")
            if other not in f:
                print "background glyph %s has no foreground"%g.name
                continue
            bg = f[other].getLayer("background")
            bg.clear()
            moved.append(g.name)
            print bg
            bg.appendGlyph(g)
    for name in moved:
        f.removeGlyph(name)

f = CurrentFont()
cleanupBackground(f)
print 'done'
    