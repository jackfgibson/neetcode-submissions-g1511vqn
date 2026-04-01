class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en = en + str(len(s)) + '_' + s
        return en

    def decode(self, s: str) -> List[str]:
        dec = []
        l_str = ''
        l = 0
        word = ""
        read_length = True
        for char in s:
            if read_length:
                if char!='_':
                    l_str+=char
                else:
                    l = int(l_str)
                    l_str = ''
                    read_length = False
                    if l==0:
                        dec.append("")
                        read_length =  True
            else:
                word+=char
                l-=1
                if l==0:
                    dec.append(word)
                    word = ""
                    read_length = True
        return dec


