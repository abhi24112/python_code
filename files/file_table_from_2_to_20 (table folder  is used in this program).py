for a in range(2,21):
    with open(f"table/Multiplication_table_of_{a}.txt","w") as f:
        for i in range(1,11):
            f.write(f"{a}x{i}={a*i}\n")
      
