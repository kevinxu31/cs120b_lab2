/*	Author: lxu092
 *  Partner(s) Name: Luofeng Xu
 *	Lab Section:2
 *	Assignment: Lab 2  Exercise 2
 *	Exercise Description: L2E2
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
  	DDRA=0x00;PORTA=0xFF;
	DDRB=0xFF;PORTB=0x00;
	unsigned char tmpA0=0x00;
	unsigned char tmpA1=0x00;
   	unsigned char tmpA2=0x00;
	unsigned char tmpA3=0x00;
	unsigned char cntavail=0x00;
	while (1) {
		tmpA0=PINA &0x01;
		tmpA1=PINA &0x02;
		tmpA2=PINA &0x04;
		tmpA3=PINA &0x08;
		cntavail=4-(tmpA3>>3)-(tmpA2>>2)-(tmpA1>>1)-tmpA0;
		PORTC=cntavail;
	}
	return 0;

}
