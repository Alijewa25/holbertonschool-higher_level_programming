#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Python lüğətini XML faylına çevirir."""
    # 1. Kök elementi yaradırıq (<data>)
    root = ET.Element("data")
    
    # 2. Lüğətdəki hər bir elementi kökə uşaq element kimi əlavə edirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML-də bütün dəyərlər sətir (string) olmalıdır
    
    # 3. Ağacı yaradırıq və fayla yazırıq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """XML faylını oxuyur və onu Python lüğətinə çevirir."""
    try:
        # 1. XML faylını parse edirik (təhlil edirik)
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # 2. Boş bir lüğət yaradıb teqləri ora yığırıq
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text
            
        return deserialized_dict
    except (FileNotFoundError, ET.ParseError):
        return None
