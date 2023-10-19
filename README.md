# A2B_Timeslot_Configuration
A Python utility to look at A2B timeslot configuration registers and report various timeslot frames throughout the A2B network..

[Markdown Cheat Sheet](https://www.markdownguide.org/basic-syntax/)

## Synopsis
Not sophisticated or polished, but it WORKS, and generates very useful information.

## Requirements
* Python v3

## Usage
* Run Cypher_A2B_Routing_Registers.py on the command line;
	* $ python3 ./Cypher_A2B_Routing_Registers.py
* Register configurations currently have to be manaully added/edited.
* The _config.py files are two register configurations that can be copied and pasted in to the Cypher_A2B_Routing_Registers.py utility script.  These files represent the network topology descriptions.

## Files
*  Cypher_A2B_Routing_Registers.py		= The utility source code.
*  alev3_x2_node_production_config.py	= A2B topology for ALEV3 production setup.  To be manually copied and pasted into the main utility Python script file.
*  alev3_x3_node_tuning_config.py		= A2B topology for ALEV3 tuning setup.  To be manually copied and pasted into the main utility Python script file.
*  register_setting_template.py			= A2B Timeslot registers required by the utiity. 

## Further Enhancements
* Add I2SGCFG to determine and report TDMx for each serial port.
* Add I2SCFG to report exact timeslot locations in each serial port; RX0, RX1, TX0, TX1.
* Enable user defining of Rx timeslot literal names.
* Parse .etf trace files to generate network topology.

## Example Output
```
Master
Tx FB [10]:|S1_00|S1_01|S1_02|S1_03|S1_04|S1_05|S1_06|S1_07|S0_00|S0_01|#

Slave 0
Tx FB [ 2]:|MM_16|MM_17|#

Slave 1
Tx FB [16]:|MM_02|MM_03|MM_04|MM_05|MM_06|MM_07|MM_08|MM_09|MM_10|MM_11|MM_12|MM_13|MM_14|MM_15|MM_16|MM_17|#
```