# [2349. Design a Number Container System](https://leetcode.com/problems/design-a-number-container-system) 🛠️

**Type:** Medium ⚖️ <br>
**Topics:** Hash Table 🗂️🔑, Design 🎨🛠️, Heap (Priority Queue) ⬆️🏔️, Ordered Set: 🔢🔒
<hr>

### Problem Statement
Design a system that can:
1. **Insert or Replace** a number at a given index in the system. 🏗️
2. **Return the smallest index** for a given number in the system. 🔢

Implement the `NumberContainers` class:
- `NumberContainers()`: Initializes the number container system. 🚀
- `void change(int index, int number)`: Fills the container at the `index` with the `number`. If there's already a number at that `index`, it gets replaced. 🔄
- `int find(int number)`: Returns the smallest index filled with the given `number` or `-1` if no index has the number. 📍
<hr>

### Examples:
- **Example 1:** <br>
**Input:**<br>
`["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]`<br>
`[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]`<br>
**Output:** `[null, -1, null, null, null, null, 1, null, 2]` <br>
**Explanation:** <br>
    1. **NumberContainers nc = new NumberContainers();** 🆕 <br>
    2. **nc.find(10);** ➡️ No container has number 10, so -1 is returned. ❌ <br>
    3. **nc.change(2, 10);** ➡️ Container at index 2 is filled with number 10. 🛢️ <br>
    4. **nc.change(1, 10);** ➡️ Container at index 1 is filled with number 10. 🛢️ <br>
    5. **nc.change(3, 10);** ➡️ Container at index 3 is filled with number 10. 🛢️ <br>
    6. **nc.change(5, 10);** ➡️ Container at index 5 is filled with number 10. 🛢️ <br>
    7. **nc.find(10);** ➡️ Smallest index with number 10 is 1, so return 1. 📍 <br>
    8. **nc.change(1, 20);** ➡️ Replace number 10 at index 1 with number 20. 🔄 <br>
    9. **nc.find(10);** ➡️ Smallest index with number 10 is 2, so return 2. 📍
<hr>

### Constraints 📝⚠️
- <code>1 <= index, number <= 10<sup>9</sup></code> 🔢➖1️⃣➡️9️⃣🔟9️⃣
- At most <code>10<sup>5</sup></code> calls will be made **in total** to `change` and `find`. ⏱️
<hr>

### Hints 💡🔍
- Let’s make a little magic happen! 🪄 Use a hash table to keep track of where each number is hanging out in the container (because numbers need homes too! 🏡). Then, use another hash table to remember what’s currently living at each index (because we don’t want any index feeling lonely or confused! 😅).
- "Now, let’s level up! 🚀 Use an ordered set to keep all the indices for each number in neat order (because even numbers like to stay organized! 📅). When you’re finding the smallest index, the ordered set has your back. But wait—when a number changes homes 🏠 (thanks to the change method), make sure to update the ordered set so nobody gets lost or left behind! 😎
<hr>