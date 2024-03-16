g="${b}\033[1;30m"
b="\033[0m"
b1="$b\033[1;37m"
r="${b}\033[1;31m"
r1="${b}\033[31m"
A="${b}\033[1;34m"
A1="${b}\033[34m"
ac="${b}\e[1;36m"
ac1="${b}\e[36m"
v="${b}\033[1;32m"
v1="${b}\033[32m"
m="$b\033[1;35m"
m1="$b\033[35m"
a="$b\033[1;33m"
a1="$b\033[33m"
cy="$b\033[38;2;23;147;209m"
clear
banner() {
echo "
         (                                
         )\ )                          )  
         (()/(  (                (   ( /(  
         /(_)) )\  (    (      ))\  )\()) 
         (_))_ ((_) )\   )\ )  /((_)(_))/  
         |   \ (_)((_) _(_/( (_)) | |_/   
         | |) || |(_-<| ' \))/ -_)|  _|  
         |___/ |_|/__/|_||_| \___| \__|"
}
banner
echo -e "\n[${A}+${b}] Intalando pacotes...\n"
if pip install requests && pip install rich && pip install pystyle ; then
  echo -e "\n[${v1}+${b}] Boas notícias, os pacotes foram instalados com sucesso"
  sleep 2
  echo -e "\nO Disnet vai começar automaticamente em alguns segundos, caso queira iniciá-lo novamente, basta entrar no repositório do Disnet e digitar ${r}python3 Disnet.py${b}"
  sleep 3
  echo -e "\nIniciando em...\n"
  sleep 1
  echo "5"
  sleep 1
  echo "4"
  sleep 1
  echo "3"
  sleep 1
  echo "2"
  sleep 1
  echo "1"
  sleep 1
  clear
  python3 Disnet.py
else
  echo "[${r}+${b}] Más notícias, não foi possível instalar os pacotes em sua máquina, tente novamente mais tarde."
fi
