import socket

serv_sock = socket.socket(socket.AF_INET,       #задаем семейство протоколов "Интернет" (INET)
						  socket.SOCK_STREAM,   #задаем тип передачи данных "потоковый" (TCP)
	                      proto = 0)            #выбираем протокол "по умолчанию" для TCP, т.е. IP
#print(type(s))									#<class 'socket.socket'>

#print(serv_sock.fileno()) #доступ к целочисленному файловому дескриптору

serv_sock.bind(('172.20.10.8', 53210)) #привязываем созданный сокет к сетевому адаптеру (IP и сетевой порт)
serv_sock.listen(10) #10 - это размер очереди входящий подключений, или backlog

while True:
	#Бесконечно обрабатываем входящие подключения
	client_sock, client_addr = serv_sock.accept() #получаем соединение из очереди
											      #accept не возвращает управление коду до тех пор,
											      #пока в очереди установленных соединений не появится
                                                  #установленное подключение 

	#пример чтения и записи данных в клиентский сокет
	while True:
		#Пока клиент не отключится, читаем передаваемые данные и отправляем обратно
		data = client_sock.recv(1024) 
		if not data:
			#клиент отключился
			break
		client_sock.sendall(data)

	client_sock.close()
