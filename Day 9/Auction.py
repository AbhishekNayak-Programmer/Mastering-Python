from art import logo
print(logo)

is_bidding = True
highest_bid_amount = 0
bidder_name = ''
persons = {}

while is_bidding :
    name = input("Enter your name : ")
    bid = input("Enter bid amount : ")
    persons[name] = bid
    if int(bid) > highest_bid_amount :
        bidder_name = name
        highest_bid_amount = int(bid)

    still_persons_left = input("Does some persons left? (Write y or n) : ").lower()

    if still_persons_left == "n" :
        is_bidding = False
        print(f'Highest Bidder name is {bidder_name} and bid amount is {str(highest_bid_amount)}')
    else :
        print("\n" * 20)