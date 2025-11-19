from .selector_node import SelectorIntNode

# 这里将我们写的类映射给 ComfyUI
NODE_CLASS_MAPPINGS = {
    "SimpleSelectorInt": SelectorIntNode
}

# 这里是节点在菜单中显示的名字
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleSelectorInt": "最后有效节点序号选择器"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
