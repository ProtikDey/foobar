evol = {((0, 0), (0, 0)): 0, ((0, 0), (0, 1)): 1, ((0, 0), (1, 0)): 1,
        ((0, 0), (1, 1)): 0, ((0, 1), (0, 0)): 1, ((0, 1), (0, 1)): 0,
        ((0, 1), (1, 0)): 0, ((0, 1), (1, 1)): 0, ((1, 0), (0, 0)): 1,
        ((1, 0), (0, 1)): 0, ((1, 0), (1, 0)): 0, ((1, 0), (1, 1)): 0,
        ((1, 1), (0, 0)): 0, ((1, 1), (0, 1)): 0, ((1, 1), (1, 0)): 0,
        ((1, 1), (1, 1)): 0}
devol = {0: (((0, 0), (0, 0)), ((0, 0), (1, 1)), ((0, 1), (0, 1)),
             ((0, 1), (1, 0)), ((0, 1), (1, 1)), ((1, 0), (0, 1)),
             ((1, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (0, 0)),
             ((1, 1), (0, 1)), ((1, 1), (1, 0)), ((1, 1), (1, 1))),
         1: (((1, 0), (0, 0)), ((0, 1), (0, 0)), ((0, 0), (1, 0)),
             ((0, 0), (0, 1)))}


def precol(col):
    possib = ((0, 0), (0, 1), (1, 0), (1, 1))
    curr = devol[col[0]]
    for i in range(1, len(col)):
        new = []
        for tes in curr:
            for comb in possib:
                if evol[(tes[i], comb)] == col[i]:
                    new.append(tes+(comb,))
        curr = tuple(new)
    bin_ret = [tuple(zip(*i)) for i in curr]
    return [tuple([bitlist(nu) for nu in possibl]) for possibl in bin_ret]

def bitlist(bitsl):
    out = 0
    for bit in bitsl:
        out = (out << 1) | bit
    return out


def solution(g):
    transposed = tuple(zip(*g))
    preimgs = precol(transposed[0])
    precount = dict()
    for pair in preimgs:
        precount[pair[0]] = 1
    for col in transposed:
        preimgs = precol(col)
        count = dict()
        for pair in preimgs:
            if pair[0] not in precount: precount[pair[0]] = 0
            if pair[1] not in count: count[pair[1]] = 0
            count[pair[1]] += precount[pair[0]]
        precount = count
    return sum(precount.values())