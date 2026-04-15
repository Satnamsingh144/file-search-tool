import os

def file_founder(folder,keyboard="",extenisions=""):
    result=[]
    for root , dirs , files in os.walk(folder):
      for file in files:
         if keyboard.lower() in file.lower():
            if extenisions:
               if file.lower().endswith(extenisions.lower()):
                  result.append(os.path.join(root,file))
            else:
               result.append(os.path.join(root,file))
    return result

def main():
    print("=== Smart File Search Tool ===")

    folder = input("Enter folder path: ")

    if not os.path.isdir(folder):
        print("Invalid folder path!")
        return

    keyword = input("Enter file name keyword (optional): ")
    extension = input("Enter file extension (e.g. .pdf) (optional): ")

    results = file_founder(folder, keyword, extension)

    print("\n=== Results ===")
    if results:
        for file in results:
            print(file)
        print(f"\nTotal files found: {len(results)}")
    else:
        print("No files found.")


if __name__ == "__main__":
    main()