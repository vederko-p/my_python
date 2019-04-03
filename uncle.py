s = 'Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил, \
И лучше выдумать не мог'

s1 = s.split()
s2 = []

for i in range(len(s1)):
    if s1[i].startswith('м') or s1[i].startswith('М'):
        continue
    s2.append(s1[i])

s3 = ' '.join(s2)

print(s3)
