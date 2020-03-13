from mininet.net import Mininet                                                                        
from mininet.node import Controller                                                                    
from mininet.topo import SingleSwitchTopo                                                              
from mininet.log import setLogLevel                                                                    
                                                                                                       
import os                                                                                              
                                                                                                       
class POXBridge( Controller ):                                                                         
    "Custom Controller class to invoke POX forwarding.l2_learning"                                     
    def start( self ):                                                                                 
        "Start POX learning switch"                                                                    
        self.pox = '%s/pox/pox.py' % os.environ[ 'HOME' ]                                              
        self.cmd( self.pox, 'forwarding.l2_learning &' )                                               
    def stop( self ):                                                                                  
        "Stop POX"                                                                                     
        self.cmd( 'kill %' + self.pox )                                                                
                                                                                                       
controllers = { 'poxbridge': POXBridge }                                                               
                                                                                                       
if __name__ == '__main__':                                                                             
    setLogLevel( 'info' )                                                                              
    net = Mininet( topo=SingleSwitchTopo( 4 ), controller=POXBridge )                                  
    net.start()                                                                                        
    net.pingAll()                                                                                      
    net.stop() 