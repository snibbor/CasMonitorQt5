#!/usr/bin/env python3

import machine
from time import sleep

LINEVOL = 0.75

def countdown(t):
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		sleep(1)
		t -=1

print('STARTING...')
#machine.connect()
#machine.home()
machine.engage_sampleF()

#print('ADDING FORMALIN')
#machine.goto_formalin()
#machine.pump_in(0.5, 0.5)
#sleep(2)
#machine.goto_sampleD()
#machine.pump_out(LINEVOL, 0.5)
#machine.pump_out(0.3, 0.2)
#sleep(10)

#print('REMOVING FORMALIN')
#machine.pump_in(1.5, 0.5)
#sleep(2)
#machine.goto_waste()
#machine.pump_out(0.7)

#print('WASHING SYRINGE')
#machine.goto_meoh()
#machine.pump_in(1, 0.5)
#sleep(2)
#machine.goto_waste()
#machine.pump_out(1, 0.5)
#sleep(2)

#######################
#print('MEOH WASHING SAMPLE')
#machine.goto_meoh()
#machine.pump_in(1, 0.5)
#sleep(2)
#machine.goto_sampleD()
#machine.pump_out(LINEVOL, 0.5)
#sleep(2)
#machine.pump_out(0.6, 0.2)
#sleep(5)

#print('REMOVING MEOH WASH')
#machine.pump_in(0.6, 0.2)
#sleep(2)
#machine.pump_in(1.2, 0.5)
#sleep(2)
#machine.goto_waste()
#machine.pump_out(1.2, 0.5)
#sleep(2)

#print('ADDING DYE')
#machine.goto_vial()
#machine.pump_in(1.3, 0.5)
#sleep(2)
#machine.goto_sampleD()
#machine.pump_out(LINEVOL, 0.5)
#sleep(2)
#machine.pump_out(0.2, 0.2)


#print('INCUBATING DYE')
#countdown(600)
#for x in range(5):
#	print('CYCLE : {:02d}'.format(x+1))
#	machine.pump_out(0.07, 0.1)
#	countdown(500)

#print('REMOVING DYE')
#machine.pump_in(1.5, 0.5)
#sleep(2)
#machine.goto_waste()
#machine.pump_out(1, 0.5)

#print('ADDING BABB')
#machine.goto_babb()
#machine.pump_in(0.75, 0.5)
#sleep(5)
machine.goto_sampleF()
#machine.pump_out(0.8, 0.5)
#sleep(2)
#machine.pump_out(0.4, 0.2)
#countdown(300)

print('BABB FINAL WASH')
machine.pump_in(0.5, 0.5)
sleep(2)
machine.pump_in(1, 0.5)
sleep(3)
machine.goto_waste()
machine.pump_out(1, 0.5)
sleep(2)
machine.goto_babb()
machine.pump_in(0.8, 0.5)
sleep(2)
machine.goto_sampleF()
machine.pump_out(0.8, 0.5)
sleep(2)
machine.pump_out(0.6, 0.2)
#countdown(200)
#machine.pump_out(0.3, 0.2)
sleep(2)
machine.disengage_sampleF()
print('Specimen may be removed')

print('CLEANING')
machine.pump_in(1, 0.5)
sleep(2)
machine.pump_in(1, 0.5)
sleep(2)
machine.goto_waste()
machine.pump_out(0.7, 0.5)
sleep(2)
machine.goto_meoh()
machine.pump_in(1, 0.5)
sleep(2)
machine.goto_sampleF()
machine.pump_out(0.6, 0.5)
sleep(5)
machine.pump_in(0.7, 0.5)
sleep(2)
machine.goto_waste()
machine.pump_out(0.7)
sleep(2)
