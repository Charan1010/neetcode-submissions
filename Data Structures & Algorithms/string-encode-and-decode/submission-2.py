class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += (str(len(s)) + "#" + s)

        print(encoded_str)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        pointer = 0
        while pointer < len(s):
            str_len = re.search(r'[0-9]+', s[pointer:]).group()
            decoded_strs.append(s[pointer+len(str_len)+1: pointer+len(str_len)+int(str_len)+1])
            pointer += len(str_len)+int(str_len)+1

        print(decoded_strs)
        return decoded_strs

