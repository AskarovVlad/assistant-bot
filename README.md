# This is a console bot-helper that works with the phone book using commands.
It can execute commands like:
1. **hello** - Greetings message.
2. **showcommands** - Shows a list of all commands.
3. **add** 'name' 'phone' 'birthday' - Adds record the contact with {name} and {phone number} 
and {birthday} (optional parameter) to the book.
4. **remove** 'name' - Removes record {name}.
5. **showall** - Show the list of all contacts in the phone book.
6. **addphone** 'name' 'phone' - Adds {phone} number to contact {name}.
7. **changephone** 'name' 'old phone' 'new phone' - Changes the {old phone} to the {new phone} 
of the contact {name}.
8. **removephone** 'name' 'phone' - Removes the {phone} of the contact {name}.
9. **addbirthday** 'name' 'phone' - Adds {birthday} to contact {name}.
10. **changebirthday** 'name' 'birthday' - Changes the {old birthday} to the {new birthday} 
of the contact {name}.
11. **datetobirth** {name} - Calculates the number of days until the birthday contact {name}.
12. **removebirthday** 'name' 'birthday' - Removes the {birthday} of the contact {name}. 
13. **search** 'name' - Searches records by the {name}.
14. **asearch** 'name or phone or birthday or multiple characters' - Searches for a records by 
the specified criteria except special characters like .^$*+?{}[]\|().
15. **changephone** 'name' 'old phone number' 'new phone number' - Changes the old phone number 
to the new phone number {name}.
16. **exit** or **close** or **.** (dot) or **goodbye** or **bye** - Terminates program execution.
