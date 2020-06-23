import random


class RandomizedCollection(object):

    def __init__(self):
        self.vals, self.idxs = [], collections.defaultdict(set)

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)  # idxs store the indexs for the same val
        return not self.idxs[val]

    def remove(self, val):  # remove the most recent val?
        if self.idxs[val]:
            out, ins = self.idxs[val].pop(), self.vals[
                -1]  # out index: replace the remove index with the last value in vals and update the correspoinding index saved in the idx
            self.vals[out] = ins

            # update the index
            if self.idxs[ins]:
                self.idxs[ins].discard(len(self.vals) - 1)
                self.idxs[ins].add(out)

            # pop out
            self.vals.pop()
            return True
        return False

    def getRandom(self):
        return random.choice(self.vals)