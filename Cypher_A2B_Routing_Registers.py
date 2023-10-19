#!/usr/bin/python3

# ============================================================================ #

my_dict_template = {
   "Reg_DNSLOTS":  0x00,
   "Reg_LDNSLOTS": 0x00,
   "Reg_BCDNSLOTS":0x00,
   "Reg_UPSLOTS" : 0x00,
   "Reg_LUPSLOTS": 0x00,
   "Reg_DNMASK0":  0x00,   # Slot  0 -  7
   "Reg_DNMASK1":  0x00,   # Slot  8 - 15
   "Reg_DNMASK2":  0x00,   # Slot 16 - 23
   "Reg_DNMASK3":  0x00,   # Slot 24 - 31
   "Reg_DNOFFSET": 0x00,
   "Reg_UPMASK0":  0x00,   # Slot  0 -  7
   "Reg_UPMASK1":  0x00,   # Slot  8 - 15
   "Reg_UPMASK2":  0x00,   # Slot 16 - 23
   "Reg_UPMASK3":  0x00,   # Slot 24 - 31
   "Reg_UPOFFSET": 0x00,
}

TxFrameBuf = 0
SCF_A_Side = 1
SCF_B_Side = 2
SRF_A_Side = 3
SRF_B_Side = 4
RxFrameBuf = 5

empty = "empty"

# ============================================================================ #

def report_time_slots( group_name, my_list ) :
   nmb_ts = len(my_list)
   print( "{} [{:2}]:".format(group_name,nmb_ts), end = ""  )
   for slot in my_list :
      if slot == empty :
         break
      print( "|{}".format(slot), end = "" )
   print( "|#" )
   return

# ---------------------------------------------------------------------------- #

def handle_mask_registers( reg, asl, idx, txb ) :
# reg
# asl = A-Side List
# 
   # print( reg, ":", end=" " )
   byte = regs[reg]
   mask = 0x01
   cc = 0
   mx = -1
   for xx in range(0,8) :
      bitv = mask & byte
      if bitv :
         bb = 1
         cc = cc + 1
         mx = xx
         if (xx + idx * 8) > (len( asl ) - 1) :
            print("\nMAJOR PROBLAMO #2\n")
            time_slot = "XXXXX"
         else :
            time_slot = asl[ xx + idx * 8 ]
         txb.append(time_slot)
      else :
         bb = 0
      mask = mask * 2
      # print( "bit{}:{},".format(xx,bb), end="" )
   # print( "#" )
   return (cc,mx)

# ---------------------------------------------------------------------------- #

def accumulate_mask_registers( direction, list_aside ) :

   C = 0
   M = -1
   register_group = "Reg_" + direction + "MASK"
   list_txbuf = list()
   # print( "register_group:", register_group )

   for reg_indx in range(4) :
      register_liter = register_group + "{:1}".format(reg_indx)
      print( "register_liter:", register_liter )
      c,m = handle_mask_registers( register_liter, list_aside, reg_indx, list_txbuf ) # ; print("c&m:", c, m)
      C = C + c
      if m > -1 : M = reg_indx*8 + m

   # print( "C&M:", C, M )

   return (C,M,list_txbuf)

# ============================================================================ #

if __name__ == '__main__' :

   Master  = my_dict_template.copy()
   Master ["Reg_DNSLOTS"]   = 0x12
   # Master ["Reg_DNSLOTS"]   = 0x10
   Master ["Reg_UPSLOTS"]   = 0x0A
   Record_Master = [list(), list(), list(), list(), list(), list()]

   Slave_0 = my_dict_template.copy()
   # Slave_0["Reg_DNSLOTS"]   = 0x12
   Slave_0["Reg_DNSLOTS"]   = 0x12
   Slave_0["Reg_LDNSLOTS"]  = 0x80
   Slave_0["Reg_BCDNSLOTS"] = 0x00
   Slave_0["Reg_UPSLOTS"]   = 0x08
   Slave_0["Reg_LUPSLOTS"]  = 0x02
   Slave_0["Reg_DNMASK0"]   = 0x00   # Slot  0 -  7
   Slave_0["Reg_DNMASK1"]   = 0x00   # Slot  8 - 15
   Slave_0["Reg_DNMASK2"]   = 0x03   # Slot 16 - 23
   Record_Slave_0 = [list(), list(), list(), list(), list(), list()]
   # Slave_0["Reg_DNOFFSET"]  = 0x03
   # Slave_0["Reg_LDNSLOTS"]  = 0x85

   Slave_1 = my_dict_template.copy()
   Slave_1["Reg_DNSLOTS"]   = 0x00
   Slave_1["Reg_LDNSLOTS"]  = 0x80
   Slave_1["Reg_BCDNSLOTS"] = 0x00
   Slave_1["Reg_UPSLOTS"]   = 0x00
   Slave_1["Reg_LUPSLOTS"]  = 0x08
   Slave_1["Reg_DNMASK0"]   = 0xFC   # Slot  0 -  7
   Slave_1["Reg_DNMASK1"]   = 0xFF   # Slot  8 - 15
   Slave_1["Reg_DNMASK2"]   = 0x03   # Slot 16 - 23
   # Slave_1["Reg_DNMASK0"]   = 0xFF   # Slot  0 -  7
   # Slave_1["Reg_DNMASK1"]   = 0xFF   # Slot  8 - 15
   # Slave_1["Reg_DNMASK2"]   = 0x00   # Slot 16 - 23
   Record_Slave_1 = [list(), list(), list(), list(), list(), list()]

   A2B_Network = [
      ("Master", Master ,Record_Master),
      ("Slave0", Slave_0,Record_Slave_0),
      ("Slave1", Slave_1,Record_Slave_1)]
   # ====================================================================== #

   print( "Script BGN" )

   # Initialize Rx Frame Buffer Time Slots
   print("Initialize Rx Frame Buffer Time Slots")
   count = -1
   for node in A2B_Network :
      name = node[0]
      regs = node[1]
      slts = node[2] # list of time slot lists
      if count == -1 :
         # print( "\nMaster" )
         prefix = "MM"
      else :
         # print( "\nSlave", count )
         prefix = "S"+"{:1}".format(count)
      count = count + 1
      my_list = slts[RxFrameBuf]
      for indx in range(32) :
         my_list.append(prefix + "_" + "{:02}".format(indx))

   # ---------------------------------------------------------------------- #

   # Generate Synchronization Control Frame Time Slots
   print("Generate Synchronization Control Frame Time Slots")
   count = -1
   for node in A2B_Network :

      name = node[0]
      regs = node[1]
      slts = node[2]

      if count == -1 :
         # print( "\nMaster:", name )
         # SCF
         cc = regs["Reg_DNSLOTS"] # ; print( "cc =", cc )
         slts[SCF_B_Side] = slts[RxFrameBuf][0:cc]
         prev = slts[SCF_B_Side]

      else :
         print( "\nSlave", count )
         # SCF
         slts[SCF_A_Side] = prev.copy()
         dif = regs["Reg_DNSLOTS"] - len( slts[SCF_A_Side] )
         if dif > 0 :
            print("\nMAJOR PROBLAMO #1\n")
            time_slot = "YYYYY"
            for xxx in range(dif) :
               slts[SCF_A_Side].append(time_slot)
         #
         #
         C, dnmaskrx, dntxbuf = accumulate_mask_registers( "DN", slts[SCF_A_Side] )
         slts[TxFrameBuf] = dntxbuf
         # print("C&dnmaskrx:", C, dnmaskrx)
         # print("dntxbuf:", dntxbuf)
         #
         # 
         cc = regs["Reg_DNSLOTS"] # ; print( "cc =", cc )
         slts[SCF_B_Side] = slts[SCF_A_Side][0:cc].copy()
         #
         cc = 0x3F & regs["Reg_LDNSLOTS"] # ; print( "cc =", cc )
         oo = regs["Reg_DNOFFSET"] # ; print( "oo =", oo )
         appd = slts[RxFrameBuf][oo:oo+cc]
         slts[SCF_B_Side] = slts[SCF_B_Side] + appd
         #
         prev = slts[SCF_B_Side]

      count = count + 1

   # exit(0)

   # ---------------------------------------------------------------------- #

   # Generate Synchronization Response Frame Time Slots
   print("Generate Response Control Frame Time Slots")
   count = len(A2B_Network)
   index = count - 2
   # print("count:", count)
   # print("index:", index)
   for xxxx in A2B_Network :
      # print("index:", index+1)
      node = A2B_Network[index+1]
      name = node[0]
      regs = node[1]
      slts = node[2]

      if index == count - 2 :
         print( "End Node:", index )
         # SRF
         cc = 0x3F & regs["Reg_LUPSLOTS"] # ; print( "cc =", cc )
         oo = regs["Reg_UPOFFSET"] # ; print( "oo =", oo )
         appd = slts[RxFrameBuf][oo:oo+cc]
         slts[SRF_A_Side] = slts[SRF_A_Side] + appd
         #
         prev = slts[SRF_A_Side]

      elif index == -1 :
         # print( "Master:", index )
         # SRF
         slts[SRF_B_Side] = prev.copy()
         #
         # cc = regs["Reg_UPSLOTS"]  ; print( "cc =", cc )
         # slts[RxFrameBuf] = slts[SRF_A_Side][0:cc]
         # slts[SCF_B_Side] = slts[RxFrameBuf][0:cc]
         # prev = slts[SRF_A_Side]

         slts[TxFrameBuf] = slts[SRF_B_Side]

      else :
         # print( "Slave:", index )
         # SRF
         slts[SRF_B_Side] = prev.copy()
         #
         #
         C, upmaskrx, uptxbuf = accumulate_mask_registers( "UP", slts[SRF_B_Side] )
         slts[TxFrameBuf] = slts[TxFrameBuf] + uptxbuf
         # print("C&upmaskrx:", C, upmaskrx)
         # print("uptxbuf:", uptxbuf)
         #
         #
         cc = regs["Reg_UPSLOTS"] # ; print( "cc =", cc )
         slts[SRF_A_Side] = slts[SRF_B_Side][0:cc].copy()
         #
         cc = 0x3F & regs["Reg_LUPSLOTS"] # ; print( "cc =", cc )
         oo = regs["Reg_UPOFFSET"] # ; print( "oo =", oo )
         appd = slts[RxFrameBuf][oo:oo+cc]
         slts[SRF_A_Side] = slts[SRF_A_Side] + appd
         #
         prev = slts[SRF_A_Side]

      index = index - 1

   # ---------------------------------------------------------------------- #
   # ---------------------------------------------------------------------- #

   # dnmaskrx
   # upmaskrx
   # slts[TxFrameBuf] = dntxbuf + uptxbuf

   # ---------------------------------------------------------------------- #
   # ---------------------------------------------------------------------- #

   count = -1
   for node in A2B_Network :
      name = node[0]
      regs = node[1]
      slts = node[2]
      if count == -1 :
         print( "\nMaster" )
         report_time_slots( "Tx FB", slts[TxFrameBuf] )
         # report_time_slots( "SCF A", slts[SCF_A_Side] )
         # report_time_slots( "SCF B", slts[SCF_B_Side] )
         # report_time_slots( "SRF A", slts[SRF_A_Side] )
         # report_time_slots( "SRF B", slts[SRF_B_Side] )
         # report_time_slots( "Rx FB", slts[RxFrameBuf] )
      else :
         print( "\nSlave", count )
         report_time_slots( "Tx FB", slts[TxFrameBuf] )
         # report_time_slots( "SCF A", slts[SCF_A_Side] )
         # report_time_slots( "SCF B", slts[SCF_B_Side] )
         # report_time_slots( "SRF A", slts[SRF_A_Side] )
         # report_time_slots( "SRF B", slts[SRF_B_Side] )
         # report_time_slots( "Rx FB", slts[RxFrameBuf] )
      count = count + 1

   print( "Script END" )

   exit(0)
