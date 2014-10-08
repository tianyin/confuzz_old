#!/usr/bin/python

import os
import re
from lxml import etree
from io import StringIO, BytesIO

#if not os.path.exists(OUTPUT_DIR):
#    os.mkdir(OUTPUT_DIR) 

def parse(xmlfile):
    tree = etree.parse(open(xmlfile))
    ppts = tree.xpath('//property')
    for ppt in ppts:
        #There's always a name
        value = None;
        desc = None;
        #name
        n = ppt.xpath('./name')
        for x in n: name = x.text.strip()
	#value
        v = ppt.xpath('./value')  
	for y in v: 
	    value = y.text
        #desc
        d = ppt.xpath('./description')
        for z in d: desc = z.text
        
	nameList = file('name_list.txt', 'a')
	nameList.write(name)
	nameList.write('\n')
	nameList.close

	new_config_file_name = './' + name + '.xml'
	
	# This is the simplest error, just set the configuration to 'Hello'
	# We can put more fancy errors later.

	if value != None:
	    y.text = 'Hello'
	    tree.write(new_config_file_name)
	    
	elif value == None:
	    # insert a ivalue & generate a xml file
	    valueElt = etree.SubElement(ppt, 'value')
	    valueElt.text = 'Hello'
	   # newElt = etree.SubElement(ppt, 'test')
	   # newElt.text = 'test'
	    tree.write(new_config_file_name)
	    ppt.remove(valueElt)
	    
	# After the wrong configuration files are generated, 
	# what we need is to put the files in the right directory 
	# and restart the software.

if __name__ == "__main__":
    parse('tt.xml')
