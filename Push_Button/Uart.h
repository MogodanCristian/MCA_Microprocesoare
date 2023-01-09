#include "MKL25Z4.h"
extern char c;
extern char buffer[3];
extern int numarator;
extern int flag;
extern int i;
void Create_num(char counter[3]);
void UART0_Transmit(uint8_t data); // Functie folostia pentru a trimite un octet catre interfata UART
uint8_t UART0_Receive(void); // Functie ce returneaza un octet de pe interfata UART, atunci cand acesta exista un buffer
void UART0_Init(uint32_t baud_rate); // Initializare a modulului UART pentru trasmiterea datelor, ce primeste ca parametru baud rate-ul dorit
void UART0_IRQHandler(void); // Handler-ul de intreruperi