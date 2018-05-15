#!/usr/bin/env python

"""
"""
from mininet.topo import Topo

class AttMplsTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def addSwitch( self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13' }
        kwargs.update( opts )
        return super(AttMplsTopo, self).addSwitch( name, **kwargs )

    def __init__( self ):

        "Create a topology."

        # Initialize Topology
        Topo.__init__( self )


        CHCG = self.addSwitch('s1')  # 41.877461, -87.642892
        ATLN = self.addSwitch('s2')  # 33.749017, -84.394168
        NY54 = self.addSwitch('s3')  # 40.728270, -73.994483

        CH_h1 = self.addHost('h11')
        CH_h2 = self.addHost('h12')
        CH_h3 = self.addHost('h13')

        AT_h1 = self.addHost('h21')
        AT_h2 = self.addHost('h22')
        AT_h3 = self.addHost('h23')

        NY_h1 = self.addHost('h1')

        self.addLink(CHCG, CH_h1)
        self.addLink(CHCG, CH_h2)
        self.addLink(CHCG, CH_h3)

        self.addLink(ATLN, AT_h1)
        self.addLink(ATLN, AT_h2)
        self.addLink(ATLN, AT_h3)

        self.addLink(NY54, CHCG)
        self.addLink(NY54, ATLN)

        self.addLink(NY54, NY_h1)

topos = { 'att': ( lambda: AttMplsTopo() ) }

if __name__ == '__main__':
    from onosnet import run
    run( AttMplsTopo() )

