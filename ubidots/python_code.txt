from ubidots import ApiClient

api = ApiClient(token='IZcfQVXA2uPVbk4OCf8efCQdje56Wr')

my_variable = api.get_variable('57d425607625425121ffa700')
#new_value = my_variable.save_value({'value': 10})


last_value = my_variable.get_values(1)
print last_value[0]['value']

new_value = my_variable.save_value({'value': 100})
while True:
    last_value = my_variable.get_values(1)
    print last_value[0]['value']
    #new_value = my_variable.save_value({'value': 100})
