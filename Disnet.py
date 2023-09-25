import os, cores as c, banners, requests
from pystyle import Colorate, Colors
from rich.panel import Panel
from rich.console import Console
import sys, util
console = Console()
try:
 util.inter()
 print(banners.banner0)
 banners.Carreg()
 os.system('clear')
 while True:
  os.system('clear')
  print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))
  print(Colorate.Vertical(Colors.red_to_yellow, '\n=> [C] Criado pôr: Phant0m The Great'))
  print(Colorate.Vertical(Colors.red_to_yellow, '=> [V] v6.1\n'))
  console.print(Panel.fit("""[red][01] [white]Consultar Token\n\n[red][02] [white]Enviar mensagem em um servidor\n\n[red][03] [white]Bug report\n\n[red][04] [white]Sair""", padding=(1,13), title="[bold yellow]Disnet"))
  user_response=input(f'{c.bred}[>>]: {c.white}')
  if user_response=='1' or user_response=='01':
    try:
     util.CT()
    except:
      print(f'\n{c.bred}[ ! ] Oh não ! não foi possível fazer a conexão, tente novamente mais tarde.{c.white}')
      sys.exit()
  elif user_response=='2' or user_response=='02':
    try:
      os.system('clear')
      print(Colorate.Vertical(Colors.red_to_yellow, banners.banner2))
      token=input(f'\n[{c.red}>{c.white}] Token: ')
      server_id=input(f'[{c.red}>{c.white}] Id do servidor: ')
      channel_id=input(f'[{c.red}>{c.white}] Id do canal: ')
      message=input(f'[{c.red}>{c.white}] Mensagem: ')
    
      util.MS(token, server_id, channel_id, message)
    except:
      print(f'\n{c.bred}[ ! ] Oh não ! não foi possível fazer a conexão, tente novamente mais tarde.{c.white}')
      sys.exit()
  elif user_response=='3' or user_response=='03':
    os.system('clear')
    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))
    print(f'\n[§] Caso tenha encontrado algum bug na ferramenta, entre em contato com o criador para reportar o bug. Discord ↓\n\n[ {c.bblue}D{c.white} ] @phant0mthegreat')
    input('\n[ENTER] para voltar ao menu.')
  elif user_response=='4' or user_response=='04':  
    os.system('clear')
    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))
    print('\n[#] Até a próxima.')
    sys.exit()
except KeyboardInterrupt:
  print('\n[#] O programa foi interrompido.')
