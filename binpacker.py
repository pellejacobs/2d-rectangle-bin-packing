import copy

class Binpacker(object):
    def __init__(self, width, height):
        self.root = { 'width': width, 'height': height, 'x': 0, 'y': 0, 'used': False}

    def fittable(self, blocks, rotatable = False, root = None):
        if (root is None): root = self.root
        if (not blocks): return True # Empty blocks array can always be fitted
        def fit_block(root, block_width, block_height):
            tail = blocks[1:] # Takes a deepcopy
            node = self.__find_node(root, block_width, block_height)
            if (node is None): return False
            else:
                self.__split_node(node, block_width, block_height)
                return self.fittable(tail, rotatable, root)
        block = blocks[0]
        return fit_block(copy.deepcopy(root), block['width'], block['height']) or (rotatable and fit_block(copy.deepcopy(root), block['height'], block['width']))

    def __find_node(self, root, width, height):
        if not 'used' in root: print(root)
        if (root['used']):
            return self.__find_node(root['right'], width, height) or self.__find_node(root['down'], width, height)
        elif (width <= root['width'] and height <= root['height']):
            return root
        else:
            return None

    def __split_node(self, node, width, height):
        node['used'] = True
        node['down'] = { 'x': node['x'], 'y': node['y'] + height, 'width': node['width'], 'height': node['height'] - height, 'used': False }
        node['right'] = { 'x': node['x'] + width, 'y': node['y'], 'width': node['width'] - width, 'height': height, 'used': False }
        return node
