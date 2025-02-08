# Design a Number Container System: Sorting Numbers, One Box at a Time! 📦🔢
### Intuition 🤔
The idea behind the `NumberContainers` class is to manage a system where each container (index) can store a number. You can update (replace) the number at any given index, and you need to be able to find the smallest index where a given number is stored. 

It's like a messy room with boxes (indices), and you need to keep track of which number is in each box. When you change the contents of a box, you need to make sure the list of contents (indices) is still in order. To do this, we use **SortedList** to maintain order and efficiency.

### Approach 🚀
1. **change(index, number)**:  
   - First, we check if the index already has a number (like checking if your box is already filled 🧐). If it does, we **remove** that index from the old number’s list (goodbye, old stuff 👋).  
   - Then, we update the box (index) with the new number 📦🔄 and put it in the sorted list of the new number (like organizing your stuff in alphabetical order 📚).  
   - SortedList keeps everything neat and tidy 🧹, so finding the smallest index later is easy peasy 🍋!

2. **find(number)**:  
   - To find the smallest index for a number, we just peek into the sorted list (like peeking at the front of the line 🎟️). If it exists and is not empty (no empty boxes, yay! 🎉), we return the first index (who’s at the front of the line 🏅?).  
   - If the number doesn’t exist, we sadly return **-1** (no number? Not found, sorry 😞).

    Now we’ve got a system that works like magic! ✨

### Code Implementation 👨‍💻👩‍💻 
```python3 []
from sortedcontainers import SortedList
from collections import defaultdict

class NumberContainers:
    def __init__(self):
        # Dictionary to track the current number at each index 🗂️
        # We're keeping tabs on which number lives where, because you can't trust a container to keep things organized!
        self.__current_number_at_index = {}

        # Dictionary to track indices for each number using a sorted list 🔢📋
        # SortedList helps us keep things in order. We like things neat and tidy!
        self.__indices_for_number = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        # Get the current number at the given index, if any 🔍
        # "Hey, what's already in this container?" we ask. If it's empty, we won't find anything.
        previous_number = self.__current_number_at_index.get(index, None)
        
        # If the previous number exists and it's different from the new number 🤔➡️
        # Time for a change! First, remove the old number's index from its list. Goodbye old friend! 👋
        if previous_number is not None:
            # Remove the index from the previous number's sorted list 🔥
            self.__indices_for_number[previous_number].remove(index)
            # If no more indices for the previous number, clean up 🧹
            # We’re polite. If there are no more containers with that number, we say goodbye to it from our memory.
            if not self.__indices_for_number[previous_number]:
                del self.__indices_for_number[previous_number]

        # Now, let’s update the container at the given index with the new number 🔄
        # A fresh start! New number, new beginning. 🌱
        self.__current_number_at_index[index] = number
        # Add the index to the sorted list of the new number 📝
        # Sorting? Of course! We like our containers in order, always. ✨
        self.__indices_for_number[number].add(index)

    def find(self, number: int) -> int:
        # Check if the number exists in the dictionary 🔎
        # "Is this number even here?" we wonder as we check our sorted list.
        if number in self.__indices_for_number and self.__indices_for_number[number]:
            # Return the smallest index for the given number 🏆
            # We found it! It’s the smallest index, the one we were looking for. 🎯
            return self.__indices_for_number[number][0]
        else:
            # If number doesn't exist, return -1 🚫
            # Oops, not found. Looks like that number isn’t here at all. Better luck next time! 🍀
            return -1
```

### Time Complexity ⏱️
1. **change(index, number)**:  
    - **Removing an index** from a `SortedList`: **$O(log(n))$**  
    - **Adding an index** to a `SortedList`: **$O(log(n))$**  
    
    So, the overall time complexity for the `change` method is **$O(log(n))$**.

2. **find(number)**:  
    - **Accessing the first index** in a `SortedList`: **$O(1)$**  
    
    So, the time complexity for the `find` method is **$O(1)$**. It's like going straight to the front of the line at the bakery! 🍞

### Space Complexity 💾
- The space complexity is **$O(n)$** because we store the indices in a `SortedList` for each number, and we also store the number at each index in the dictionary.

### Final Thoughts 🧠
The beauty of this approach lies in how we efficiently maintain the order of the indices using `SortedList`, which avoids having to constantly sort or search through unsorted lists. It's like keeping your room tidy without having to clean up every day. 😎

And here's a little joke for you:  
Why did the programmer bring a ladder to work?  
Because they wanted to **reach** the top of the stack! 🎉