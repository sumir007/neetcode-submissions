class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded = encoded + "#" + str(length) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            if s[i] == '#':
                j = i + 1

                # read the length until we hit the next '#'
                num = ""
                while j < len(s) and s[j] != '#':
                    num += s[j]
                    j += 1

                length = int(num)

                # move past the second '#'
                j += 1

                # extract the word
                word = s[j:j + length]
                decoded.append(word)

                # move pointer to next encoded block
                i = j + length
            else:
                i += 1

        return decoded
        

