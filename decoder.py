#!/usr/bin/python
# *-* encoding: utf8 *-*

def menu():
	respuesta = -1
	while (respuesta not in OPCIONES):
		respuesta = int(raw_input("  Selecciona una opción [0-%d]: " % (len(OPCIONES)-1)))
	return respuesta

def hex2ascii():
	while True:
		try:
			input = raw_input("String hexadecimal (salida con -1): ")
			if input == "-1":
				print("")
				break
			elif (len(input)%2 != 0):
				raise HexDecoderException("String hexadecimal malformado (número impar de caracteres)\n")		
			i = 0
			output = ''
			while i < len(input):
				hexchar = input[i]+input[i+1]
				if (int(hexchar, 16) < 32) or (int(hexchar,16) == 127):
					output += HEX_NO_PRINT[str(int(hexchar,16))]
				elif (int(hexchar, 16) > 127):
					raise HexDecoderException("El caracter hexadecimal %s (%d decimal) no tiene traducción a ASCII (0-127)\n" % (hexchar, int(hexchar,16)))
				else:
					output += hexchar.decode("hex")
				i += 2
			print("String ASCII: %s\n" % output)
		except Exception as e:
			print("[*** ERROR] %s\n" % e)

def ascii2hex():
	while True:
		try:
			input = raw_input("String ASCII (salida con -1): ")
			if input == "-1":
				print("")
				break
			print("String hexadecimal: %s" % input.encode("hex"))
		except Exception as e:
			print("[*** ERROR] %s\n" % e)

class HexDecoderException(Exception):
	def __init__(self, message):
		super(Exception, self).__init__(message)

try:
	logo = """
	++++++++++++++++++++++++++++++++++++++++++++++++++
	 ######   #####  ####### ######  ####### ######  
	 #     # #     # #     # #     # #       #     # 
	 #     # #       #     # #     # #       #     # 
	 #     # #       #     # #     # #####   ######  
	 #     # #       #     # #     # #       #   #   
	 #     # #     # #     # #     # #       #    #  
	 ######   #####  ####### ######  ####### #     # 
	++++++++++++++++++++++++++++++++++++++++++++++++++
	"""
	
	print(logo)
	OPCIONES = {0:"Hex string => ASCII",1:"ASCII string => hex",2:"GTFO"}
	HEX_NO_PRINT = { # https://www.asciitable.com/index/asciifull.gif
		"0":chr(27)+"[0;91m"+"{NULL}"+chr(27)+"[0;00m",
		"1":chr(27)+"[0;91m"+"{SOH}"+chr(27)+"[0;00m",
		"2":chr(27)+"[0;91m"+"{STX}"+chr(27)+"[0;00m",
		"3":chr(27)+"[0;91m"+"{ETX}"+chr(27)+"[0;00m",
		"4":chr(27)+"[0;91m"+"{EOT}"+chr(27)+"[0;00m",
		"5":chr(27)+"[0;91m"+"{ENQ}"+chr(27)+"[0;00m",
		"6":chr(27)+"[0;91m"+"{ACK}"+chr(27)+"[0;00m",
		"7":chr(27)+"[0;91m"+"{BELL}"+chr(27)+"[0;00m",
		"8":chr(27)+"[0;91m"+"{BS}"+chr(27)+"[0;00m",
		"9":chr(27)+"[0;91m"+"{TAB}"+chr(27)+"[0;00m",
		"10":chr(27)+"[0;91m"+"{LF}"+chr(27)+"[0;00m",
		"11":chr(27)+"[0;91m"+"{VT}"+chr(27)+"[0;00m",
		"12":chr(27)+"[0;91m"+"{FF}"+chr(27)+"[0;00m",
		"13":chr(27)+"[0;91m"+"{CR}"+chr(27)+"[0;00m",
		"14":chr(27)+"[0;91m"+"{SO}"+chr(27)+"[0;00m",
		"15":chr(27)+"[0;91m"+"{SI}"+chr(27)+"[0;00m",
		"16":chr(27)+"[0;91m"+"{DLE}"+chr(27)+"[0;00m",
		"17":chr(27)+"[0;91m"+"{DC1}"+chr(27)+"[0;00m",
		"18":chr(27)+"[0;91m"+"{DC2}"+chr(27)+"[0;00m",
		"19":chr(27)+"[0;91m"+"{DC3}"+chr(27)+"[0;00m",
		"20":chr(27)+"[0;91m"+"{DC4}"+chr(27)+"[0;00m",
		"21":chr(27)+"[0;91m"+"{NAK}"+chr(27)+"[0;00m",
		"22":chr(27)+"[0;91m"+"{SYN}"+chr(27)+"[0;00m",
		"23":chr(27)+"[0;91m"+"{ETB}"+chr(27)+"[0;00m",
		"24":chr(27)+"[0;91m"+"{CAN}"+chr(27)+"[0;00m",
		"25":chr(27)+"[0;91m"+"{EM}"+chr(27)+"[0;00m",
		"26":chr(27)+"[0;91m"+"{SUB}"+chr(27)+"[0;00m",
		"27":chr(27)+"[0;91m"+"{ESC}"+chr(27)+"[0;00m",
		"28":chr(27)+"[0;91m"+"{FS}"+chr(27)+"[0;00m",
		"29":chr(27)+"[0;91m"+"{GS}"+chr(27)+"[0;00m",
		"30":chr(27)+"[0;91m"+"{RS}"+chr(27)+"[0;00m",
		"31":chr(27)+"[0;91m"+"{US}"+chr(27)+"[0;00m",	
		"127":chr(27)+"[0;91m"+"{DEL}"+chr(27)+"[0;00m",
		
		}


	for key in OPCIONES:
		print("\t%d: %s" % (key, OPCIONES[key]))
	
	print("")
	
	while True:
		respuesta = menu()
		print("")
		input = ''
		if respuesta == 0:
			hex2ascii()
		elif respuesta == 1:
			ascii2hex()
		elif respuesta == 2:
			print("\nSaliendo...")
			break
except KeyboardInterrupt:
	print("\n\nKTHXBYE")
