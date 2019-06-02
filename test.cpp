/**
 *  @example serial_port_read.cpp
 */

#include <libserial/SerialPort.h>

#include <cstdlib>
#include <cstring>
#include <iostream>
#include <unistd.h>

constexpr const char* const SERIAL_PORT_1 = "/dev/ttyACM0" ;

/**
 * @brief This example demonstrates configuring a serial port and
 *        reading serial data.
 */
int main()
{
    using namespace LibSerial ;


    // Instantiate a SerialPort object.
    SerialPort myPort ;
    myPort.Open(SERIAL_PORT_1);
    std::string datablock;
    char lineTerminator = '\n';
    // int msTimeout = 0;

    while(true)
    {
      std::cout << datablock <<std::endl;
      myPort.ReadLine(datablock,lineTerminator,0);
      std::cout << "HIgh" << std::endl;


    }

    return 0;
}