#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize the dictionary into XML and save it to the given filename."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)
    return True

def deserialize_from_xml(filename):
    """Read the XML data from the file and return
    a deserialized Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {child.tag: child.text for child in root}
        return dictionary
    except ET.ParseError:
        return None
