dic=["1.what is the capital of india?\na.mumbai\tb.new delhi\tc.kolkata\td.chennai",
      "2.what is the currency of japan?\na.sgd\tb.aud\tc.diahram\td.yen",
      "3.which is the prime no?\na.2\tb.4\tc.6\td.8",
      "4.who is the prime minister of india?\na.modi\tb.amita shah\tc.rajnath singh\td.rahul gandhi"]
correct = ["b","d","a","a"]
amount = [1000,2000,3000,4000]
earning = 0
for i in range(len(dic)):
    print(dic[i])
    answer = input("Enter your answer : ")

    if (answer != correct[i]):
        print("Your answer is wrong you lost.")
        if (earning == 0):
            break
        else:
            print("Your earned : {0}".format(earning))    

        break
    else:
        earning += amount[i]
        print("Your earned : {0}".format(earning))    
  


