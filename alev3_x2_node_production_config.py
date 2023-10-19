
   Master  = my_dict_template.copy()
   Master ["Reg_DNSLOTS"]   = 0x10
   Master ["Reg_UPSLOTS"]   = 0x0A
   Record_Master = [list(), list(), list(), list(), list(), list()]

   Slave_0 = my_dict_template.copy()
   Slave_0["Reg_DNSLOTS"]   = 0x00
   Slave_0["Reg_LDNSLOTS"]  = 0x80
   Slave_0["Reg_BCDNSLOTS"] = 0x00
   Slave_0["Reg_UPSLOTS"]   = 0x00
   Slave_0["Reg_LUPSLOTS"]  = 0x08
   Slave_0["Reg_DNMASK0"]   = 0xFF   # Slot  0 -  7
   Slave_0["Reg_DNMASK1"]   = 0xFF   # Slot  8 - 15
   Slave_0["Reg_DNMASK2"]   = 0x03   # Slot 16 - 23
   # Slave_0["Reg_DNMASK2"]   = 0x00   # Slot 16 - 23
   Record_Slave_0 = [list(), list(), list(), list(), list(), list()]

   A2B_Network = [
      ("Master", Master ,Record_Master),
      ("Slave0", Slave_0,Record_Slave_0)]

