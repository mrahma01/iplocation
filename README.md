iplocation
===========
A simple python script to return the location and business details

###[setup]###
    pip install iplocation

###[usage]###
    >>> from iplocation import *
    >>> loc = IPLocation('207.97.227.239') # default takes your outgoing ip
    >>> loc.location
            {   u'Area Code': u'415',
            u'City': u'San Francisco',
            u'Country': u'United States  ',
            u'Latitude': u'37.7484',
            u'Longitude': u'-122.4156',
            u'Postal Code': u'94110',
            u'State/Region': u'California'}
        
    >>> loc.get_location('City')
            u'San Francisco'
        
    >>> loc.business
            {   u'Assignment': u'Static IP',
            u'Blacklist': u'',
            u'Decimal': u'3479299055',
            u'Hostname': u'github.com',
            u'IP': u'207.97.227.239',
            u'ISP': u'Rackspace Hosting',
            u'Organization': u'github',
            u'Services': u'None detected',
            u'Type': u'Corporate'}        
    >>> loc.get_business('ISP')
        u'Rackspace Hosting'
