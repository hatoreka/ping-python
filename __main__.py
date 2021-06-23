import pings

p = pings.Ping()

hosts = ["google.com", "yahoo.co.jp"]
res = p.ping("google.com")

for h in hosts:
  res = p.ping(h, times=5)
  print(res.print_messages())
  if res.is_reached():
    print('OK')
  else:
    print('NG')