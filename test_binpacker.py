from binpacker import Binpacker

def test_trivial_positive_case ():
    blocks = []
    packer = Binpacker(100, 100)
    assert packer.fittable(blocks, False)
#
def test_positive_case1():
    blocks = [
        {'width': 100, 'height': 100},
        {'width': 100, 'height': 100},
        {'width': 100, 'height': 100},
        {'width': 100, 'height': 100},
    ]
    packer = Binpacker(200, 200)
    return packer.fittable(blocks, False)

def test_negative_case():
    blocks = [
        {'width': 200, 'height': 100},
        {'width': 100, 'height': 100},
        {'width': 100, 'height': 100},
        {'width': 100, 'height': 100},
    ]
    packer = Binpacker(200, 300)
    return not packer.fittable(blocks, False)

def test_positive_rotate_case():
    blocks = [
        {'width': 200, 'height': 100},
        {'width': 100, 'height': 100},
        {'width': 100, 'height': 100},
        {'width': 100, 'height': 100},
    ]
    packer = Binpacker(200, 300)
    return packer.fittable(blocks, True)
