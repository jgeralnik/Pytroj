import marshal, byteplay

f = open('exploit.pyc')
f.read(8)
data = byteplay.Code.from_code(marshal.loads(f.read()))
count = 0
for op, args in data.code:
    if op == byteplay.SetLineno:
        count = args

print count, len(data.code)
