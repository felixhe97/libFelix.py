from typing import Optional

class Trie:
    def __init__(self, s: Optional[str] = None):
        self.__triemap = [False, {}]
        self.__num_words = 0
        # size is number of (possibly duplicated) characters stored in trie
        self.size = 0
        if s is not None:
            self.insert(s)

    def __len__(self):
        return self.__num_words

    def insert(self, s: str) -> None:
        if len(s) <= 0:
            return
        temp = self.__triemap
        while len(s) > 0:
            if s[0] not in temp[1]:
                temp[1][s[0]] = [False, {}]
                self.size += 1
            temp = temp[1][s[0]]
            s = s[1:]
        if not temp[0]:
            temp[0] = True
            self.__num_words += 1

    def find(self, s: str) -> bool:
        temp = self.__triemap
        while len(s) > 0:
            if s[0] in temp[1]:
                temp = temp[1][s[0]]
                s = s[1:]
            else:
                break
        if len(s) == 0:
            return temp[0]
        else:
            return False

    def delete(self, s: str) -> bool:
        if not self.find(s):
            return False
        temp = self.__triemap
        traversal = [temp]
        mystr = s
        while len(s) > 0:
            temp = temp[1][s[0]]
            traversal.append(temp)
            s = s[1:]
        if len(traversal[-1][1]) == 0:
            del traversal[-2][1][mystr[-1]]
            self.size -= 1
            mystr = mystr[:-1]
            traversal.pop()
        while len(traversal[-1][1]) == 0 and not traversal[-1][0]:
            del traversal[-2][1][mystr[-1]]
            self.size -= 1
            mystr = mystr[:-1]
            traversal.pop()
        self.__num_words -= 1
        return True