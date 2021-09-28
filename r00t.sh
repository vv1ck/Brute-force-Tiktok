mno=$(whoami)
if [ $mno == root ]
  then
    python3 Brute-force-tiktok.py
else
    sudo python3 Brute-force-tiktok.py
fi
