# HOWTO-TERM

TLDR : that is just ChatGPT without session keys or APIs from your terminal to assist you with your day to day tasks in terminal
Based on the idea of [Gynvael](https://gynvael.coldwind.pl/?id=771)

## Examples
```
$ howto convert a set of jpegs into a pdf, assume 90 dpi A4 page
True
diff: 0001f2, time: 45.728ms, solved: True
"""bash
convert *.jpg -page A4 -density 90 output.pdf
"""

$ howto block any access to tcp port 1234 using iptables
True
diff: 00017f, time: 47.351ms, solved: True
"""bash
iptables -A INPUT -p tcp --dport 1234 -j DROP
"""

$ howto zoom in my webcam
True
diff: 0002bc, time: 24.064ms, solved: True
"""bash
v4l2-ctl --set-ctrl=zoom_absolute=200
"""

$ howto encrypt a file using openssl with aes in authenticated mode
True
diff: 000203, time: 161.309ms, solved: True
"""bash
openssl enc -aes-256-gcm -salt -in plaintext.txt -out encrypted.enc
"""

```

## Drawbacks

Sometimes the proof of work fails and the following output is returned:
```
$ howto encrypt a file using openssl with aes in authenticated mode
True
diff: 000032, time: 2218.395ms, solved: False
```

in those cases you have to rerun the same command again

## Installation
```
git clone https://github.com/w1redch4d/howto-term.git
cd howto-term
pip install .
```

