#include "gpio.h"
#include "Pit.h"
#include "MKL25Z4.h"
#include "Uart.h"

int main()
{

	UART0_Init(115200);
	Switch_Init();
	
	while (1) 
	{
		if(flag==1)
			PIT_Init();
		if(timer_value == numarator + 2)
			return 0;
	}
	
	return 0;
	
}