try:
    print('checking status..')
    status = 'LEGIT! :)'
    status_msg = f'status = {status}'
except SyntaxError:
    exec("print 'at least print_statement works though! ;)'")
    status_msg = 'Lame :\'('

print(status_msg)

