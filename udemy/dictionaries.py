# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = ["Outstanding", "Exceeds Expectations", "Acceptable", "Fail"]

# for key in student_scores:
    
#     if student_scores[key] <= 70:
#         print("Fail")
#     elif student_scores[key] > 70 and student_scores[key] <= 80:
#         print("Acceptable")
#     elif student_scores[key] > 80 and student_scores[key] <= 90:
#         print("Exceeds Expectations")
#     else:
#         print("Outstanding")
    
# print("Welome to Bid now")

more_bids = True
bids = []

def get_bids(more_bids, bids):
    while more_bids:
        name = input("Please enter your name: ")
        bid_amount = int(input("Please enter your bid amount: $"))

        new_bid = {
        "bidder": name,
        "bid_amount": bid_amount
    }

        bids.append(new_bid)

    
        if input("To recevied more bis type 'yes' or to cancel type 'no': ") == 'yes':
            more_bids = True
        else:
            more_bids = False
        print("\n" * 100)


def find_max_bid(bids):
    max_bidder = {}

    max_bid = bids[0]

    for i in range(1, len(bids)):
        if bids[i]["bid_amount"] > max_bid["bid_amount"]:
            max_bid = bids[i]
    return max_bid

get_bids(more_bids, bids)
max_bid = find_max_bid(bids)

print(f"Max bidder is: {max_bid["bidder"]} and bid amount is: {max_bid["bid_amount"]}")

  

