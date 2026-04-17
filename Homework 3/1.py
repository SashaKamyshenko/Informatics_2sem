class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.count += 1

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def delete(self, word):
        return self._delete(self.root, word, 0)

    def _delete(self, node, word, depth):
        if depth == len(word):
            if not node.is_end:
                return False
            node.count -= 1
            if node.count == 0:
                node.is_end = False
            return len(node.children) == 0 and node.count == 0

        ch = word[depth]
        if ch not in node.children:
            return False

        child = node.children[ch]
        should_delete = self._delete(child, word, depth + 1)

        if should_delete:
            del node.children[ch]
            return len(node.children) == 0 and node.count == 0

        return False
