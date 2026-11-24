# Class List Manager - Group 6
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]

# ===== Each student adds her function BELOW this line =====

# Written by: Tala Alghulaiga
def count_names(names):
    return len(names)
    
#Written by: Rama Alkhatib
def search_name(names, name):
    if name in names:
        return True
    else:
        return False

#Written by: Jouri Alotaibi
def sortNames(names):
    return sorted(names, key=str.lower)
    
# Written by: Adeem Alothman
def remove_duplicates(names):
    unique = []
    for name in names:
        if name not in unique:
            unique.append(name)
    return unique
  
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
  
    print("Number of names:", count_names(names))
    print("search for Lama:", search_name(names, "Lama"))
    print("Sorted names:", sortNames(names))
    print("Without duplicates:", remove_duplicates(names))

main()
