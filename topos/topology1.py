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

        # add nodes, switches first...
        NY54 = self.addSwitch( 's25' ) # 40.728270, -73.99448

        # ... and now hosts
        CMBR_host = self.addHost( 'h1' )
        CHCG_host = self.addHost( 'h2' )

        # add edges between switch and corresponding host
        self.addLink( NY54 , CMBR_host )
        self.addLink( NY54 , CHCG_host )


topos = { 'att': ( lambda: AttMplsTopo() ) }

if __name__ == '__main__':
    from onosnet import run
    run( AttMplsTopo() )