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
echo -e "\n[${v1}+${b}] Instalando pacotes...\n"
pkg install python
pkg install python2
pkg install python3
pip install --upgrade pip
pip install pystyle
echo -e "\n[${v1}+${b}] Pacotes instalados com sucesso !\nUse ${r}python3 Disnet.py${b} caso queira executar o programa novamente."
sleep 4
echo -e "\nO Disnet vai ser executado automaticamente em...\n"
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
