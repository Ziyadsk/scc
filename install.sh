mkdir $HOME/.scc ; 
cp -R * ~/.scc/
chmod +x ~/.scc/scc.py
echo "export PATH=\"$PATH:$HOME/.scc/scc.py\"" >> ~/.bashrc
echo "export PATH=\"$PATH:$HOME/.scc/scc.py\"" >> ~/.zshrc
echo "alias scc='$HOME/.scc/scc.py'" >> ~/.bashrc 
echo "alias scc='$HOME/.scc/scc.py'" >> ~/.zshrc 


