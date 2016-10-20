# blame-bird.py
This Python script tries to figure out which app uses a lot of
space and files in the `Library/Caches/com.apple.bird` folder on your mac.

```
$ python blame-bird.py
4R6749AYRE.com.pixelmatorteam.pixelmator            0.00MB      1
com.apple.shoebox                                   0.00MB      3
com.apple.TextInput                                 0.00MB      7
iCloud.com.apple.iBooks                             0.00MB      2
57T9237FN3.net.whatsapp.WhatsApp                 6904.66MB    647

Accounted for: 6904MB.  Still unaccounted: 1879MB
```

If you supply the app name as argument, the script generates a list of
related files (uncomment `| xargs du -hs` to add file sizes).

```
$ python blame-bird.py com.apple.TextInput # | xargs du -hs
/Users/usr/Library/Caches/com.apple.bird/session/g/C8E6D0A6-46A8-4803-8DDE-451341DD2DBA
/Users/usr/Library/Caches/com.apple.bird/session/g/4DF22D5F-464A-4F11-9CC5-4D9A073E0D59
/Users/usr/Library/Caches/com.apple.bird/session/g/8E0BB4C3-C0C6-495F-AC60-B750971EF17D
/Users/usr/Library/Caches/com.apple.bird/session/g/9F21F0B3-26C3-4066-A11E-7A853DF7E4F5
/Users/usr/Library/Caches/com.apple.bird/session/g/1FB77878-5975-47EC-A062-C7326FBBE496
/Users/usr/Library/Caches/com.apple.bird/session/g/B4B6DCFE-9958-498E-9B53-8C6195A2CF30
/Users/usr/Library/Caches/com.apple.bird/session/g/28456B01-2DDD-4F08-924A-6C1BB8F04464
```

See [this question on Ask Different](http://apple.stackexchange.com/questions/220007).
