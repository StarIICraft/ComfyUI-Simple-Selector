Simple Selector Int (最后有效节点序号选择器)
🇨🇳 中文说明
节点名称：最后有效节点序号选择器 (SimpleSelectorInt)
分类：MyCustomNodes/Utils

核心功能
这是一个逻辑控制节点。它拥有5个通用的输入端口，会按照倒序（从5到1）的顺序检查连接状态，并输出第一个被发现是“有效激活”的端口序号（整数）。

主要特性
倒序优先级：
检查顺序为：Input 5 -> Input 4 -> Input 3 -> Input 2 -> Input 1。
一旦发现有效输入，立即停止检查并输出该序号。
例如：同时连接了 input_2 和 input_4，节点将输出 4。
智能忽略 (Mute支持)：
如果连接的上游节点被 静音/禁用 (Mute / Ctrl+M)，本节点会自动跳过它，继续向前寻找。
例如：连接了 input_2 和 input_4，但把 input_4 对应的节点 Mute 了，节点将输出 2。
万能输入：
端口支持连接任何类型的节点（图像、模型、Latent、浮点数等），不会出现类型报错。
输出值
INT (整数)：
返回找到的端口号 (1, 2, 3, 4, 或 5)。
如果没有任何输入被连接，或者所有连接的节点都被 Mute 了，输出 0。
应用场景
作为逻辑开关，配合 "Index Switch" 类节点使用。
在工作流中快速切换不同的配置，只需 Mute 掉不需要的节点，无需断开连线。
🇺🇸 English Description
Node Name: Last Valid Index Selector (SimpleSelectorInt)
Category: MyCustomNodes/Utils

Core Functionality
This is a logic control node with 5 universal input ports. It checks the connection status in reverse order (from 5 down to 1) and outputs the index integer of the first "valid and active" input found.

Key Features
Reverse Priority:
Check order: Input 5 -> Input 4 -> Input 3 -> Input 2 -> Input 1.
It stops checking and returns the index immediately upon finding a valid input.
Example: If both input_2 and input_4 are connected, the node outputs 4.
Mute/Bypass Handling:
If an upstream node is Muted (Ctrl+M), this node will treat it as non-existent and skip to the next available input.
Example: If input_2 and input_4 are connected, but the node linked to input_4 is Muted, the node outputs 2.
Universal Inputs:
The inputs accept ANY type (Image, Model, Latent, Float, etc.) without triggering type validation errors.
Output
INT (Integer):
Returns the index number of the active port (1, 2, 3, 4, or 5).
Returns 0 if no inputs are connected or if all connected nodes are muted.
Use Cases
Acting as a logic controller when paired with "Index Switch" nodes.
Quickly switching between workflow configurations by simply Muting nodes, without the need to disconnect wires.