from subprocess import Popen as cmd, PIPE
from itertools import combinations_with_replacement
from tqdm import tqdm

c = 'chess-steg -s'
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = '1. e4 d6 2. Nc3 e5 3. g4 f5 4. Nf3 fxe4 5. Nxe4 Bxg4 6. h3 Bxf3 7. Qxf3 Nc6 8. Bc4 h6 9. Qf7+ { Black resigns. } 1-0'

num = 1
while True:
    for x in tqdm(combinations_with_replacement(chars, num)):
        out = cmd(f"""{c} '{''.join(x)}'""", shell=True, stdout=PIPE, encoding='utf8').stdout.read()
        if '1. e4 d6 2. Nc3 e5 3. g4 f5' in out:
            print(x)
            exit()
    num += 1
