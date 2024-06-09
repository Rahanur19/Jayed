# 4) Add a full stop at the end of each line and rewrite to another file &quot;zen2.
# txt&quot; on the same directory.

initial_file = open("zen.txt", "r")
initial_text = initial_file.readlines()
initial_file.close()


modified_text = [line.strip() + '.' for line in initial_text]

new_file = open("zen2.txt", "w") 
new_file.write('\n'.join(modified_text))
new_file.close()

print("Modification completed. Output written into 'zen2.txt'.")
