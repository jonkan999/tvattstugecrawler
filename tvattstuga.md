# connect to VM:
ssh -i  ~/.gcp-pass/gcp_ssh jonkan@34.116.221.157

# upon creation of this VM
#getting git
sudo apt update
sudo apt install git

# getting chrome
sudo apt install curl
curl -fSsL https://dl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor | sudo tee /usr/share/keyrings/google-chrome.gpg >> /dev/null
echo deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update
sudo apt install google-chrome-stable

# get pip and initiate project
sudo apt install python3-pip
mkdir crawler
cd crawler
git init

# gitconfig
git config --global user.email "joel.engstrom17@gmail.com"
git config --global user.name "jonkn999"

# adding config:
touch ~/.config.ini
code ~/.config.ini
  [credentials]
  username = user
  password = pass
chmod 600 ~/.config.ini

# initiating dev environment
sudo apt install python3
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate

# from within venv
pip3 install selenium