/*	Author: lxu092
 *  Partner(s) Name: Luofeng Xu
 *	Lab Section:2
 *	Assignment: Lab 2  Exercise 4
 *	Exercise Description: [optional - include for your own benefit]
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
	DDRB=0x00;PORTB=0xFF;
	DDRC=0x00;PORTC=0xFF;
	DDRD=0xFF;PORTD=0x00;
	
	unsigned char wa=0x00;
	unsigned char wb=0x00;
   	unsigned char wc=0x00;
	unsigned char tmpw=0x00;
	unsigned char flag=0x00;
	while (1) {
		wa=PINA;
		wb=PINB;
		wc=PINC;
		flag=wa+wb+wc;
		tmpw=flag&0xFC;
		if (flag>140){
			tmpw=tmpw |0x01;
		}
		else {
			tmpw=tmpw &0xFE;
		}
		if (abs(wa-wc)>80){
			tmpw=tmpw |0x02;
		}
		else {
			tmpw=tmpw &0xFD;
		}
		PORTD=tmpw;
	}
	return 0;

}
