ip2location
===========
A simple python script to return the location and business details

###[setup]###
    pip install ip2location

###[usage]###
    >>>from ip2location import *
    >>>loc = IP2Location() # takes outgoing ip
    >>>loc.location
        {   u'City': u'London',
        u'Country': u'United Kingdom  ',
        u'Latitude': u'51.5142',
        u'Longitude': u'-0.0931',
        u'State/Region': u'London, City of'}