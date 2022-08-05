# This is a console bot-helper that works with the phone book using commands.
It can execute commands like:
           1. hello - Greetings message.
           2. add 'name' 'phone' 'birthday' - Adds record the contact with {name} and {phone number} 
           and {birthday} (optional parameter) to the book.
           3. remove 'name' - Removes record {name}.
           4. showall - Show the list of all contacts in the phone book.
           5. addphone 'name' 'phone' - Adds {phone} number to contact {name}.
           6. changephone 'name' 'old phone' 'new phone' - Changes the {old phone} to the {new phone} 
           of the contact {name}.
           7. removephone 'name' 'phone' - Removes the {phone} of the contact {name}.
           8. addbirthday 'name' 'phone' - Adds {birthday} to contact {name}.
           9. changebirthday 'name' 'birthday' - Changes the {old birthday} to the {new birthday} 
           of the contact {name}.
           10. datetobirth {name} - Calculates the number of days until the birthday contact {name}.
           11. removebirthday 'name' 'birthday' - Removes the {birthday} of the contact {name}. 
           12. search 'name' - Searches records by the {name}.
           13. asearch 'name or phone or birthday or multiple characters' - Searches for a records by the
           specified criteria except special characters like .^$*+?{}[]\|().
           14. changephone 'name' 'old phone number' 'new phone number' - Changes the old phone number 
           to the new phone number {name}.
           15. exit or close or . (dot) or goodbye or bye - Terminates program execution.
