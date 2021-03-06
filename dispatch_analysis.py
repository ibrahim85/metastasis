#!/usr/bin/env python
import sys
sys.path.append('/Users/zafaraliahmed/summer15/metastasis/')
import dispatcher

cpu=int(sys.argv[2]) #number of cpus to use


# stores the commands we are going to run
commandlist=[] 


# names of the simulations we are going to run
simulation_directories = sys.argv[1:]



for simulation_directory in simulation_directories: 
	commandlist.append('./pipeline ./simulation_out/'+simulation_directory+'/')
		
dispatcher.dispatcher(commandlist,slots=min(len(commandlist),cpu))