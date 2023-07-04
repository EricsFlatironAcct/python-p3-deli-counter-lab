def line(queue):
   if len(queue) == 0:
      print ("The line is currently empty.")
   else:
      print("The line is currently:", end="")
      [print(f" {index+1}. {name}", end="") for index, name in enumerate(queue)]
      print()
def take_a_number(queue, name):
    queue.append(name)
    print(f"Welcome, {name}. You are number {len(queue)} in line.")
    return queue

def now_serving(queue):
    if len(queue) ==0:
       print("There is nobody waiting to be served!")
       return queue
    print(f"Currently serving {queue.pop(0)}.")
    return queue

# OTHER_DELI = ["Logan", "Avi", "Spencer"]
# line(OTHER_DELI)