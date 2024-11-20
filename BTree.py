class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []  # URLs
        self.values = []  # Contenido en caché
        self.timestamps = []  # Timestamps para cada entrada
        self.child = []  # Referencias a nodos hijos

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Grado mínimo del árbol B

    def insert(self, key, value, timestamp):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(False)
            self.root = temp
            temp.child.insert(0, root)
            self._split_child(temp, 0)
            self._insert_non_full(temp, key, value, timestamp)
        else:
            self._insert_non_full(root, key, value, timestamp)

    def _split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        x.values.insert(i, y.values[t - 1])
        x.timestamps.insert(i, y.timestamps[t - 1])
        
        z.keys = y.keys[t:]
        z.values = y.values[t:]
        z.timestamps = y.timestamps[t:]
        y.keys = y.keys[:t - 1]
        y.values = y.values[:t - 1]
        y.timestamps = y.timestamps[:t - 1]
        
        if not y.leaf:
            z.child = y.child[t:]
            y.child = y.child[:t]

    def _insert_non_full(self, x, key, value, timestamp):
        i = len(x.keys) - 1
        if x.leaf:
            while i >= 0 and key < x.keys[i]:
                i -= 1
            i += 1
            x.keys.insert(i, key)
            x.values.insert(i, value)
            x.timestamps.insert(i, timestamp)
        else:
            while i >= 0 and key < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if key > x.keys[i]:
                    i += 1
            self._insert_non_full(x.child[i], key, value, timestamp)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, x, key):
        i = 0
        while i < len(x.keys) and key > x.keys[i]:
            i += 1
        if i < len(x.keys) and key == x.keys[i]:
            return x.values[i], x.timestamps[i]
        elif x.leaf:
            return None, None
        else:
            return self._search_recursive(x.child[i], key)

    def delete_by_date(self, date):
        self._delete_by_date_recursive(self.root, date)

    def _delete_by_date_recursive(self, x, date):
        i = 0
        while i < len(x.timestamps):
            if x.timestamps[i] > date:
                x.keys.pop(i)
                x.values.pop(i)
                x.timestamps.pop(i)
            else:
                i += 1
        if not x.leaf:
            for child in x.child:
                self._delete_by_date_recursive(child, date) 