## Python Utility Scripts
A collection of three efficient Python scripts for common algorithmic tasks: calculating Fibonacci numbers using memoization, finding the largest number in a list, and counting vowels in a string.
## 🚀 Features## 1. Optimized Fibonacci Calculator
Calculates Fibonacci numbers using Memoization (Top-Down Dynamic Programming).

* Efficiency: Reduces time complexity from exponential $O(2^n)$ to linear $O(n)$ by storing previously calculated results in a dictionary.
* Input: Integer $n$.
* Output: The $n^{th}$ Fibonacci number.

## 2. Largest Number Finder
Identifies the maximum value in a user-provided list.

* Logic: Uses float("-inf") as a baseline to ensure it works even with lists of negative numbers.
* Input: Space-separated integers (e.g., 10 45 2 33).
* Output: The highest value found in the set.

## 3. Vowel Counter
Counts the total number of vowels in a given string.

* Logic: Utilizes a set for $O(1)$ constant-time lookups and handles both uppercase and lowercase characters.
* Input: Any string or sentence.
* Output: Total count of a, e, i, o, u.

## 🛠️ How to Run

   1. Ensure you have Python 3.x installed.
   2. Copy the code into a .py file (e.g., utils.py).
   3. Run the script via terminal:
   
   python utils.py
   
   4. Follow the on-screen prompts to input your data.

## 📝 Note
All functions are wrapped in while True loops, allowing for continuous testing. Use Ctrl+C to exit the program.

