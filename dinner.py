bill_amt = int(input("Enter Bill Amount:" ))
tip_perc = int(input("Enter Tip percentage:" ))
sharing = int(input("No. of friends:" ))

bill_after_tip = bill_amt+(bill_amt*(tip_perc/100))
each_friend_bill = bill_after_tip / sharing
print(f'Total bill after adding the tip for {sharing} friends as {bill_after_tip} and per head contribution is {round(each_friend_bill,2)}')