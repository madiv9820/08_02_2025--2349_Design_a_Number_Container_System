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