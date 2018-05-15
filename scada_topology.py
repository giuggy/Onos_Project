#!/usr/bin/env python

"""
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import Node
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

class ScadaTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def addSwitch( self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13' }
        kwargs.update( opts )
        return super(ScadaTopo, self).addSwitch( name, **kwargs )

    def __init__( self ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self )

        # add nodes, switches first...
        MTU = self.addSwitch( 's1' )
        PCI_1 = self.addSwitch( 's10' )
        PCI_2 = self.addSwitch( 's11' )
        PCI_3 = self.addSwitch( 's12' )

    # ... and now hosts
        MTU_host_1 = self.addHost( 'h1' )
        MTU_host_2 = self.addHost( 'h2' )
        MTU_host_3 = self.addHost( 'h3' )
        PCI_1_host_1 = self.addHost( 'h11' )
        PCI_1_host_2 = self.addHost( 'h12' )
        PCI_1_host_3 = self.addHost( 'h13' )
        PCI_2_host_1 = self.addHost( 'h21' )
        PCI_2_host_2 = self.addHost( 'h22' )
        PCI_2_host_3 = self.addHost( 'h23' )
        PCI_3_host_1 = self.addHost( 'h31' )
        PCI_3_host_2 = self.addHost( 'h32' )
        PCI_3_host_3 = self.addHost( 'h33' )

        # add edges between switches
        self.addLink( MTU, PCI_1 )
        self.addLink( MTU, PCI_2 )
        self.addLink( MTU, PCI_3 )


        # add edges between switches
        self.addLink(MTU, MTU_host_1)
        self.addLink(MTU, MTU_host_2)
        self.addLink(MTU, MTU_host_3)
        self.addLink(PCI_1, PCI_1_host_1)
        self.addLink(PCI_1, PCI_1_host_2)
        self.addLink(PCI_1, PCI_1_host_3)
        self.addLink(PCI_2, PCI_2_host_1)
        self.addLink(PCI_2, PCI_2_host_2)
        self.addLink(PCI_2, PCI_2_host_3)
        self.addLink(PCI_3, PCI_3_host_1)
        self.addLink(PCI_3, PCI_3_host_2)
        self.addLink(PCI_3, PCI_3_host_3)


topos = { 'scada': ( lambda: ScadaTopo() ) }

if __name__ == '__main__':
    from onosnet import run
    run( ScadaTopo() )