ip = input('Введите IP: ')
split_ip = ip.split('.')

if len(split_ip) < 4:
  print('Адрес - это четыре числа, разделённые точками')
else:
   numeric = 0
   out_of_range = 0
   for i_ip in split_ip:
      if i_ip.isdigit():
         numeric += 1
         if int(i_ip) > 255:
            out_of_range += 1
            print(i_ip,'превышает 255')
      else:
        print(i_ip,'- не целое число')

if out_of_range == 0 and numeric == 4:
            print('IP-адрес корректен')
