define ($IP 10.10.1.1)                                                                                              
define ($MAC 00:00:00:00:01:00)                                                                                     
                                                                                                                    
source::FromDevice;                                                                                                 
sink::ToDevice;                                                                                                     
                                                                                                                    
c::Classifier(                                                                                                      
                                                                                                                    
                                                                                                                    
//TRANSPORT LAYER PROTOCOLS                                                                                         
                                                                                                                    
        23/11,                  //UDP Protocol Type over IPv4                                                       
        23/06,                  //TCP Protocol Type over IPv4                                                       
        -);                                                                                                         
                                                                                                                    
source->c;                                                                                                          
                                                                                                                    
c[0]->Print('UDP Packet over IPv4')  -> MalwareDetect -> sink;                                                      
c[1]->Print('TCP Packet over IPv4') -> MalwareDetect -> sink;                                                       
c[2]->Print('Others')->Discard; 