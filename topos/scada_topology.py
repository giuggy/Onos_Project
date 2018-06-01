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


class ScadaTopo(Topo):

    def addSwitch(self, name, **opts):
        kwargs = {'protocols': 'OpenFlow13'}
        kwargs.update(opts)
        return super(ScadaTopo, self).addSwitch(name, **kwargs)

    def __init__(self):
        # Create a topology.

        # Initialize Topology
        Topo.__init__(self)

        # add nodes, switches first...
        mtu = self.addSwitch('switch1')
        pci_1 = self.addSwitch('switch10')
        pci_2 = self.addSwitch('switch11')
        pci_3 = self.addSwitch('switch12')

        # ... and now hosts
        mtu_host_1 = self.addHost('h1')
        mtu_host_2 = self.addHost('h2')
        mtu_host_3 = self.addHost('h3')
        pci_1_host_1 = self.addHost('h11')
        pci_1_host_2 = self.addHost('h12')
        pci_1_host_3 = self.addHost('h13')
        pci_2_host_1 = self.addHost('h21')
        pci_2_host_2 = self.addHost('h22')
        pci_2_host_3 = self.addHost('h23')
        pci_3_host_1 = self.addHost('h31')
        pci_3_host_2 = self.addHost('h32')
        pci_3_host_3 = self.addHost('h33')

        # add edges between switches
        self.addLink(mtu, pci_1)
        self.addLink(mtu, pci_2)
        self.addLink(mtu, pci_3)

        # add edges between switch and host
        self.addLink(mtu, mtu_host_1)
        self.addLink(mtu, mtu_host_2)
        self.addLink(mtu, mtu_host_3)
        self.addLink(pci_1, pci_1_host_1)
        self.addLink(pci_1, pci_1_host_2)
        self.addLink(pci_1, pci_1_host_3)
        self.addLink(pci_2, pci_2_host_1)
        self.addLink(pci_2, pci_2_host_2)
        self.addLink(pci_2, pci_2_host_3)
        self.addLink(pci_3, pci_3_host_1)
        self.addLink(pci_3, pci_3_host_2)
        self.addLink(pci_3, pci_3_host_3)


topos = {'scada': (lambda: ScadaTopo())}

if __name__ == '__main__':
    from onosnet import run

    run(ScadaTopo())
