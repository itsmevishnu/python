tests = int(input())
seats = []
for i in range(tests):
   seats.append(int(input()))
   
#iterating through the test cases
def get_seat_type(number):
    if number % 6 == 0 or number%6 == 1 :
        return "WS"
    elif number % 6 == 2 or number %6 == 5 :
        return "MS"
    else:
        return "AS"
        
for i in seats:
    current = i;
    if(i%12==0):
      next_seat = i -12 + 1
    else:
        next_seat  = (current//12)*12 + (12 - i%12)+1
    seat_type = get_seat_type(i)
    print(str(next_seat)+" "+seat_type)