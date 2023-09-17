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
  print(Colorate.Vertical(Colors.red_to_yellow, '=> [V] v4.0\n'))
  console.print(Panel.fit("""[red][01] [white]Consultar Token\n\n[red][02] [white]Bug Report\n\n[red][03] [white]Sair""", padding=(1,13), title="[bold yellow]Disnet"))
  m=input(f'{c.bred}[>>]: {c.white}')
  if m=='1' or m=='01':
    try:
     util.CT()
    except:
      print(f'\n{c.bred}[ ! ] Oh não ! não foi possível fazer a conexão, tente novamente mais tarde.{c.white}')
      sys.exit()
  elif m=='2' or m=='02':
    os.system('clear')
    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))
    print(f'\n[§] Caso tenha encontrado algum bug na ferramenta, entre em contato com o criador para reportar o bug. Discord ↓\n\n[ {c.bblue}D{c.white} ] @phant0mthegreat')
    input('\n[ENTER] para voltar ao menu.')
  elif m=='3' or m=='03':
    os.system('clear')
    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))
    print('\n[#] Até a próxima.')
    sys.exit()
except KeyboardInterrupt:
  print('\n[#] O programa foi interrompido.')
