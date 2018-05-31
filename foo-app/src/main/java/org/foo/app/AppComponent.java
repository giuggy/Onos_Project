package org.foo.app;


import org.apache.felix.scr.annotations.Activate;
import org.apache.felix.scr.annotations.Component;
import org.apache.felix.scr.annotations.Deactivate;
import org.apache.felix.scr.annotations.Reference;
import org.apache.felix.scr.annotations.ReferenceCardinality;
import org.apache.felix.scr.annotations.Service;
import org.onosproject.net.Device;
import org.onosproject.net.Port;
import org.onosproject.net.device.DeviceService;
import org.onosproject.net.device.PortStatistics;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Timer;


@Component(immediate = true)
public class AppComponent {

    private final Logger log = LoggerFactory.getLogger(getClass());

    /*
        @Activate
        protected void activate() {
            log.info("Started");
        }

        @Deactivate
        protected void deactivate() {
            log.info("Stopped");
        }
    */

    @Activate
    protected void activate() {

        log.info("Started");

        Iterable<Device> devices = deviceService.getDevices();

        for (Device d : devices) {
            log.info("#### Device id " + d.id().toString());

            List<Port> ports = deviceService.getPorts(d.id());
            for (Port port : ports) {
                log.info("Getting info for port " + port.number());
                PortStatistics portstat = deviceService.getStatisticsForPort(d.id(), port.number());
                PortStatistics portdeltastat = deviceService.getDeltaStatisticsForPort(d.id(), port.number());
                if (portstat != null)
                    log.info("portstat bytes recieved " + portstat.bytesReceived());
                else
                    log.info("Unable to read portStats");

                if (portdeltastat != null)
                    log.info("portdeltastat bytes recieved " + portdeltastat.bytesReceived());
                else
                    log.info("Unable to read portDeltaStats");
            }

        }
    }
    //

    @Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
    protected DeviceService deviceService;


    @Deactivate
    protected void deactivate() {
        for(portStatsReaderTask task : this.getMap().values()) {
            task.setExit(true);
            task.getTimer().cancel();
        }
        log.info("Stopped");
    }

    public Map<Integer, portStatsReaderTask> getMap() {
        return map;
    }

    public void setMap(Map<Integer, portStatsReaderTask> map) {
        this.map = map;
    }

    private Map<Integer,portStatsReaderTask> map = new HashMap<Integer,portStatsReaderTask>();
}
