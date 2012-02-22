
try:
    from storytext.javaswttoolkit import util
    util.ignoreLabels.append("=")
except ImportError:
    pass # from CPython, possibly

customEventTypes = []
