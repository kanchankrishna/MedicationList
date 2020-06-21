import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "patientkanchan@gmail.com"
receiver_email = input("Enter the email of the pharmacy that you want to order the medications from:")
password = "testgadha"

#connect to your email
server = smtplib.SMTP("smtp.gmail.com", 587)
#587 is the port that you are connecting to
#establish the Connection
server.starttls()
msg = MIMEMultipart('alternative')
msg['Subject'] = "Your Order"

user_answer =input("Hi there! Would you like to add an item to your list of medication?")
htmlContent = "<table>" + "<tr>" + "<th style='border: 1px solid #dddddd; text-align: left; padding: 8px; width: 20%'>Medication Name</th>" + "<th style='border: 1px solid #dddddd; text-align: left; padding: 8px; width: 75%'>Quantity</th>"+ "</tr>"
          
if(user_answer == "yes") or (user_answer == "Yes"):
  while user_answer == "yes":
    item_name = input("Enter the name of the medication: \n")
    quantity = int(input("Enter the quantity of this medication: \n"))
    print("")
    string_quantity = str(quantity)
    append_file = open("MedicationList.txt", "a")
    append_file.write(item_name+ " " +string_quantity)
    append_file.write("\n")
    user_answer = input("Would you like to add another item to your medication list? ")
    if (user_answer=="no" or user_answer=="No"):
      append_file.close()
      file = open("MedicationList.txt", "r")
      lines = file.readlines()
      for line in lines:
        newlines = line.split()
        htmlContent = htmlContent + "<tr>" + "<td style='border: 1px solid #dddddd; text-align: left; padding: 8px;' th:text=>" + newlines[0] + "</td>"  + "<td style='border: 1px solid #dddddd; text-align: left; padding: 8px;' th:text=>" + newlines[1] + "</td>"  + "</tr>";
      messageBody = "<html><body><title>Grocery List</title><p style=\"font-family: Arial, sans-serif\">Hi, <br>Please create an order for these medications :</p>"+ htmlContent + "</table><br><p style=\"font-family: Arial, sans-serif\">Thank you.<br>Kanchan Krishna</p></body></html>";
      part1 = MIMEText("Hi!How are you?", 'plain')
      part2 = MIMEText(messageBody, 'html')
      msg.attach(part1)
      msg.attach(part2)
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, msg.as_string())
      print("Your order has been sent to " +receiver_email)
elif user_answer=="no":
    print("Thanks! Have a great day.")
else:
  print("Alright! Have a great day.") 




