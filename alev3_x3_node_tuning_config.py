
   Master  = my_dict_template.copy()
   Master ["Reg_DNSLOTS"]   = 0x12
   # Master ["Reg_DNSLOTS"]   = 0x10
   Master ["Reg_UPSLOTS"]   = 0x0A
   Record_Master = [list(), list(), list(), list(), list(), list()]

   Slave_0 = my_dict_template.copy()
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
   # Slave_1["Reg_DNMASK0"]   = 0xFC   # Slot  0 -  7
   # Slave_1["Reg_DNMASK1"]   = 0xFF   # Slot  8 - 15
   # Slave_1["Reg_DNMASK2"]   = 0x03   # Slot 16 - 23
   Slave_1["Reg_DNMASK0"]   = 0xFF   # Slot  0 -  7
   Slave_1["Reg_DNMASK1"]   = 0xFF   # Slot  8 - 15
   Slave_1["Reg_DNMASK2"]   = 0x00   # Slot 16 - 23
   Record_Slave_1 = [list(), list(), list(), list(), list(), list()]

   A2B_Network = [
      ("Master", Master ,Record_Master),
      ("Slave0", Slave_0,Record_Slave_0),
      ("Slave1", Slave_1,Record_Slave_1)]
