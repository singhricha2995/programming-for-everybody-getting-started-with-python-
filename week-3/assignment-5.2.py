largest = None
smallest = None
while True:
    x=input('Enter a number:')
    if x=="done":
        break
    try:
        fx=int(x)
    except:
        print('Invalid input')
    if largest is None:
        largest = fx
    if fx>largest:
        largest = fx
    if smallest is None:
        smallest=fx
    if fx<smallest:
        smallest=fx
def done(largest,smallest):
    print('Maximum is',largest)
    print('Minimum is',smallest)
done(largest,smallest)
        
