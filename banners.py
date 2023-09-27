import sys, time, cores as c
from pystyle import Colorate, Colors

texto = "[⚠️] ESTA FERRAMENTA É FEITA SOMENTE PARA FINS EDUCACIONAIS E DE PESQUISA, EU (PHANT0M THE GREAT) NÃO ASSUMO QUALQUER TIPO DE RESPONSABILIDADE POR QUALQUER USO INADEQUADO DESTA FERRAMENTA, USE-A COM BOM SENSO [⚠️]"
def text():
  for char in texto:
      print(char, end='', flush=True)  
      time.sleep(0.03)
    
def Carreg():
	l = ['|', '-', '|', '-']
	for i in l+l+l:
		sys.stdout.write('\r' + f'''Entrando no {Colorate.Vertical(Colors.red_to_yellow, 'Disnet')}...'''+i)
		sys.stdout.flush()
		time.sleep(0.2)

banner0="""
─────█─▄▀█──█▀▄─█─────
────▐▌──────────▐▌────
────█▌▀▄──▄▄──▄▀▐█────
───▐██──▀▀──▀▀──██▌───
──▄████▄──▐▌──▄████▄──"""

banner1="""
            (                                
            )\ )                          )  
            (()/(  (                (   ( /(  
            /(_)) )\  (    (      ))\  )\()) 
            (_))_ ((_) )\   )\ )  /((_)(_))/  
            |   \ (_)((_) _(_/( (_)) | |_/   
            | |) || |(_-<| ' \))/ -_)|  _|  
            |___/ |_|/__/|_||_| \___| \__|"""

banner2='''               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--' '''
banner3="""
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⠷⠾⠛⠛⠛⠛⠷⠶⢶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣴⡾⠛⠉⠁⠀           ⠈⠛⢿⣦
⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀   ⠈⠛⢿⣦⡀⠀
⢠⣼⠟⠁⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠙⣧⡀
⣿⡇⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⢈⣷
⣿⣿⣦⡀⣠⣾⣿⣿⣿⡿⠟⠛⠁⠁⠁⠁⠁⠁⠛⠻⢿⣿⣿⣿⣿⣆⣀⣠⣾⣿
⠉⠻⣿⣿⣿⣿⣽⡿⠋⠀⠀            ⠛⣿⣿⣿⣿⣿⡟⠁
⠀⠀⠈⠙⠛⣿⣿⠀⠀⠀⠀      ⠀⠀⠀⠀   ⣹⣿⡟⠋⠁⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣷⣄⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⣀⣾⣿⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⣿⡇⠀⠀⠀⠀⢸⣿⡏⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣄⠀⠀⣀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
