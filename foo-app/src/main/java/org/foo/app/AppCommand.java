/*
 * Copyright 2018-present Open Networking Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.foo.app;

import org.apache.karaf.shell.commands.Argument;
import org.apache.karaf.shell.commands.Command;
import org.apache.karaf.shell.commands.Option;
import org.onosproject.cli.AbstractShellCommand;
import org.onosproject.net.flow.FlowEntry;
import org.onosproject.net.flow.StoredFlowEntry;
import org.onosproject.net.flow.instructions.Instruction;
import org.onosproject.net.statistic.FlowEntryWithLoad;
import org.onosproject.net.statistic.FlowStatisticService;
import org.onosproject.net.statistic.SummaryFlowEntryWithLoad;


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
import static org.onosproject.net.DeviceId.deviceId;
import static org.onosproject.net.PortNumber.portNumber;


/**
 * Sample Apache Karaf CLI command
 */
@Command(scope = "onos", name = "sample",
         description = "Sample Apache Karaf CLI command")
public class AppCommand extends AbstractShellCommand {


    @Override
    protected void execute() {

        print("Hello %s", "World" );
        try{
            DeviceService deviceService = get(DeviceService.class);
            FlowStatisticService flowStatsService = get(FlowStatisticService.class);

            Iterable<Device> devices = deviceService.getDevices();
            for(Device d : devices){
                print("Device " + d.id().toString());

                List<Port> ports = deviceService.getPorts(d.id());
                for (Port port : ports) {
                    print("Getting info for port " + port.number());
                    PortStatistics portstat = deviceService.getStatisticsForPort(d.id(), port.number());
                    PortStatistics portdeltastat = deviceService.getDeltaStatisticsForPort(d.id(), port.number());
                    if (portstat != null)
                        print("portstat bytes recieved " + portstat.bytesReceived());
                    else
                        print("Unable to read portStats");

                    if (portdeltastat != null)
                        print("portdeltastat bytes recieved " + portdeltastat.bytesReceived());
                    else
                        print("Unable to read portDeltaStats");

                    SummaryFlowEntryWithLoad flowInfo = flowStatsService.loadSummary(d, port.number());

                    if (flowInfo != null)
                        print("summary load " + flowInfo.totalLoad());
                    else
                        print("Unable to read portDeltaStats");

                }

                print("");

            }
        } catch (NullPointerException e){
            print("Error");

        }




    }


}
