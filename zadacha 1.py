print ('Введите произвольное число:')
chislo = float(input())
print ('Введите пограничное число:')
granica = float(input())
if chislo < granica:
    print ('1-е число {} меньше пограничного {}'.format (chislo, granica))
elif chislo > granica:
    print ('1-е число {} больше пограничного {}'.format (chislo, granica))
    if (granica * 3) == chislo:
        print ('1-е число {} больше пограничного {} ровно в три раза'.format (chislo, granica))
    elif (granica * 3) < chislo:
        print('1-е число {} больше пограничного {} более чем в три раза'.format (chislo, granica))
else:
    print ('1-е число как-то относится к пограничному, однако данное отношение не описано в условиях задачи')
