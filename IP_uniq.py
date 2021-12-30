import os
ips = []
uniq = []
q0 = input("From which file should be IOC loaded?: ").replace(' ', '')
try:
    num_lines = sum(1 for line in open(f'{q0}'))
except:
    print(f"File called {q0} does not exist...")
    exit
with open(f'{q0}', 'r') as f:
    for i in range(0, num_lines):
        lajna = str(f.readline().replace('\n', ''))
        ips.append(lajna)
        if lajna not in uniq:
            uniq.append(lajna)
        else:
            continue
    uniq_mezera = '\n'.join(uniq)
q1 = input("Do you want to create new text file with list of IPs? Y/N: ").replace(' ', '')
if q1 == "Y" or q1 == "y":
    q2 = input("How it should be called? (without .txt): ").replace(' ', '')
    os.system(f"touch {q2}.txt")
    with open(f'{q2}.txt', 'a+') as f:
        f.write(f'{uniq_mezera}')
elif q1  == "N" or q1 == "n":
    print(uniq_mezera)
else:
    exit
