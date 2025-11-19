import torch

# --- 核心修复部分开始 ---
class AnyType(str):
    """
    这是一个特殊的类，用来欺骗 ComfyUI 的类型检查系统。
    无论传入什么类型，它都返回 True (匹配成功)。
    """
    def __ne__(self, __value):
        return False
    def __eq__(self, __value):
        return True

# 实例化一个万能类型对象
any_type = AnyType("*")
# --- 核心修复部分结束 ---

class SelectorIntNode:
    """
    根据连接情况输出序号的节点。
    修正了类型验证错误。
    """
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
            "optional": {
                # 使用 any_type 代替之前的 "*"
                "input_1": (any_type, {}), 
                "input_2": (any_type, {}),
                "input_3": (any_type, {}),
                "input_4": (any_type, {}),
                "input_5": (any_type, {}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("selected_index",)
    FUNCTION = "get_index"
    CATEGORY = "MyCustomNodes/Utils"

    def get_index(self, **kwargs):
        # 定义总端口数
        total_inputs = 5
        
        # 倒序检查：从 5 到 1
        for i in range(total_inputs, 0, -1):
            key = f"input_{i}"
            
            # 检查是否有连接
            if key in kwargs:
                value = kwargs[key]
                
                # 逻辑：如果连接了东西，且不是 None (即没有被 Mute/忽略)
                # 注意：在某些 ComfyUI 版本中，被 Mute 的节点可能根本不会传参进 kwargs，
                # 或者传进来是 None。这个判断能同时覆盖这两种情况。
                if value is not None:
                    # 额外检查：防止某些特殊节点传空列表等情况
                    # 只要有值，就认为是有效连接
                    return (i,)
        
        # 如果全都被忽略或没连接，返回 0
        return (0,)

