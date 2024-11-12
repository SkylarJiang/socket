- 你需要实现一个在线留言板系统的客户端部分，在这个模型中，客户端可以执行以下操作：
  1. **POST**
  2. **GET**
  3. **DELETE**
  4. **QUIT**：客户端可以发送命令来结束与服务器的会话。
- 内容
  1. Socket initialization: : initialize and create the TCP socket. 初始化及创建 TCP 连接
  2. Initiate the connection request: 输入 ip 和端口，创建一个socket
  3. Send command to the server: 上面四个命令
  4. Receive the message from the server

