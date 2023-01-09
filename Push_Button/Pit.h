#include "MKL25Z4.h"
extern uint32_t timer_value;
void PIT_Init(void); // Functie de initializarea a modulului periferic
void PIT_IRQHandler(void); // Functia de tratarea a intreruperilor pentru perifericul PIT
void UTILS_PrintTimer(uint32_t value); // Functie menita sa printeze o valoare numarata in formatul MM:SS