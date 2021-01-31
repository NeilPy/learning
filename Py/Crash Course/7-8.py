sandwich_orders = ['Katsu sandos', 'pastrami', 'Triple-decker steak', 'pastrami',
                   'Ploughman’s ', 'Posh BLT', 'pastrami']
finished_sandwiches = []
print('\nPastrami is gone')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print('\nI made your ' + current_sandwich.title() + ' sandwich.')
    finished_sandwiches.append(current_sandwich)

print('\nThe all sandwich:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
