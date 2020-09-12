from typing import Optional

class TrieNode:
    def __init__(self, flag: Optional[bool] = False):
        self.flag = flag
        self.triemap = {}

    def __len__(self):
        return len(self.triemap)

class Trie(TrieNode):
    def __init__(self, s: Optional[str] = None):
        super().__init__()
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
        temp = self
        while len(s) > 0:
            if s[0] not in temp.triemap:
                temp.triemap[s[0]] = TrieNode()
                self.size += 1
            temp = temp.triemap[s[0]]
            s = s[1:]
        if not temp.flag:
            temp.flag = True
            self.__num_words += 1

    def find(self, s: str) -> bool:
        temp = self
        while len(s) > 0:
            if s[0] in temp.triemap:
                temp = temp.triemap[s[0]]
                s = s[1:]
            else:
                break
        if len(s) == 0:
            return temp.flag
        else:
            return False

    def delete(self, s: str) -> bool:
        if not self.find(s):
            return False
        temp = self
        traversal = [temp]
        mystr = s
        while len(s) > 0:
            temp = temp.triemap[s[0]]
            traversal.append(temp)
            s = s[1:]
        traversal[-1].flag = False
        while len(traversal[-1]) == 0 and not traversal[-1].flag:
            del traversal[-2].triemap[mystr[-1]]
            self.size -= 1
            mystr = mystr[:-1]
            traversal.pop()
        self.__num_words -= 1
        return True
