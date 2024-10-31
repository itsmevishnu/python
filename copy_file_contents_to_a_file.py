import os


def copy_all_file_content_and_write_to_file(folder, output_file):
    files = [file for file in os.listdir(folder)]
    
    with open(output_file, "a") as output_file:
        for item in files:
            try:
                with open(f"{folder}/{item}", "r", encoding="utf-8-sig") as content:
                    output_file.write("\n")
                    output_file.write(f"Content of {item}\n")
                    output_file.write("==="*20)
                    output_file.write("\n")
                    output_file.write(content.read())
            except Exception as error:
                print(error)
def main():
  folder = "D:/tasks"
  output_file = "my_all_tasks.txt"
  copy_all_file_content_and_write_to_file(folder, output_file)

if __name__ == "__main__":
  main()
  
  

 
