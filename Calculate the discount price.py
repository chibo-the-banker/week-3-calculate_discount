def calculate_discount(price,discount_percentage) :
  
  if discount_percentage > 0:
    new_price = price - price*(discount_percentage/100)
    print(f'The discounted price of the good is {new_price}')

  elif discount_percentage == 0:
    print(f'With a dicount percentage of {discount_percentage}%, the price remains the same at {price}')

  else: 
    print(f'With a dicount percentage of {discount_percentage}%, the price remains the same at {price} because your value is incorrect, try again')

price = int(input("What is the cost of your item? $"))
discount_percentage=int(input("Don't forget the discount percentage % "))
calculate_discount(price,discount_percentage)