

import ClointFusion as cf

cf.OFF_semi_automatic_mode()

cf.window_show_desktop()

### Going to flipkart
cf.launch_any_exe_bat_application(r"https://www.flipkart.com/")
cf.key_hit_enter()

USERNAME = cf.gui_get_any_input_from_user("enter Number")
PASSWORD = cf.gui_get_any_input_from_user("enter password",password=True)

#cf.capture_snip_now() 

### Login Page ###

try:
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\5_snip.PNG",conf=0.8))
    cf.key_write_enter(strMsg=USERNAME, key="t")
    cf.key_write_enter(strMsg=PASSWORD, key="t")
    #cf.capture_snip_now() 
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\1_snip.PNG",conf=0.8))
except Exception:
    print("Already Logged")


#cf.capture_snip_now()
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\2_snip.PNG",conf=0.8))
#------selecting product1----------#
cf.key_write_enter(strMsg="boAt Airdopes 131 Bluetooth Headset")
#cf.capture_snip_now()
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\3_snip.PNG",conf=0.8))

#cf.capture_snip_now()
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\4_snip.PNG",conf=0.8))
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\2_snip.PNG",conf=0.8))

#------selecting product2----------#
cf.key_write_enter(strMsg="boAt Airdopes 402 Bluetooth Headset")
#cf.capture_snip_now()
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\6_snip.PNG",conf=0.8))
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\4_snip.PNG",conf=0.8))

#-------------place Order---------#
#cf.capture_snip_now()
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\7_snip.PNG",conf=0.8))

#-----Enter Details-------#
NAME = cf.gui_get_any_input_from_user("enter Name")
MOBILENUMBER = cf.gui_get_any_input_from_user("enter phone number")
PINCODE = cf.gui_get_any_input_from_user("enter Pinnumber")
LOCALITY = cf.gui_get_any_input_from_user("enter place")
ADDRESS = cf.gui_get_any_input_from_user("enter address")
CITY = cf.gui_get_any_input_from_user("enter city")
STATE = cf.gui_get_dropdownlist_values_from_user(msgForUser="State",dropdown_list=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa" ,"Gujarat" ,"Haryana" , "Himachal Pradesh" ,"Jammu and Kashmir" ,"Jharkhand" , "Karnataka" ,"Kerala" ,"Madhya Pradesh","Maharashtra" ,"Manipur" ,"Meghalaya" ,"Mizoram","Nagaland" ,"Odisha","Punjab" ,"Rajasthan" ,"Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"],multi_select=False)
LANDMARK = cf.gui_get_any_input_from_user("enter landmark",mandatory_field=False) 
ALTERNATE = cf.gui_get_any_input_from_user("enter alter number",mandatory_field=False)
ADDRESSTYPE = cf.gui_get_dropdownlist_values_from_user(msgForUser="Select",dropdown_list=["Home","Work"],multi_select=False)


cf.key_write_enter(strMsg=NAME, key="t")
cf.key_write_enter(strMsg=MOBILENUMBER, key="t")
cf.key_write_enter(strMsg=PINCODE, key="t")
cf.key_write_enter(strMsg=LOCALITY, key="t")
cf.key_write_enter(strMsg=ADDRESS, key="t")
cf.key_write_enter(strMsg=CITY, key="t")
cf.key_write_enter(strMsg=STATE, key="t")
cf.key_write_enter(strMsg=LANDMARK,key = "t")
cf.key_write_enter(strMsg=ALTERNATE,key = "t")
cf.key_write_enter(strMsg=ADDRESSTYPE,key = "t")

#cf.capture_snip_now()
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\8_snip.PNG",conf=0.8))

#cf.capture_snip_now()
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\9_snip.PNG",conf=0.8))

#--------Select Debit/Credit card---------#

#cf.capture_snip_now()
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\10_snip.PNG",conf=0.8))

user_card = cf.gui_get_consent_from_user(msgForUser="Use your card?")
if user_card == "Yes":
    CARDNUMBER = cf.gui_get_any_input_from_user(msgForUser="Card Number")
    MONTH = cf.gui_get_any_input_from_user(msgForUser="Expiry Month")
    YEAR = cf.gui_get_any_input_from_user(msgForUser="Expiry Year")
    CVV = cf.gui_get_any_input_from_user(msgForUser="CVV")

cf.key_write_enter(CARDNUMBER, key="t")
cf.key_write_enter(MONTH, key="t")
cf.key_write_enter(YEAR, key="t")
cf.key_write_enter(CVV, key="t")

#cf.capture_snip_now()

try:
    card_paid = cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Users\G Rithika\Desktop\py\snips\11_snip.PNG", conf=0.8, wait=5))
except Exception:
    print("Incorrect Details")

if cf.gui_get_consent_from_user(msgForUser="Want to close the windows?") == "Yes":
    cf.key_press("alt + f4")










