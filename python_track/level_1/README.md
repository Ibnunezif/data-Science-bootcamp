## Prime Number Checker
A high-performance script to determine if a given integer is a prime number.
## 🚀 Features## Efficient Prime Detection
Uses the Square Root Optimization method to minimize calculations.

* Logic: Instead of checking every number up to $n$, it only checks divisors up to $\sqrt{n}$. If no divisor is found by that point, the number is guaranteed to be prime.
* Time Complexity: $O(\sqrt{n})$, making it significantly faster for large numbers compared to a standard linear search.
* Edge Case Handling: Correctly identifies $0$ and $1$ as non-prime.

## 🛠️ How to Run

   1. Ensure you have Python 3.x installed.
   2. Run the script:
   
   python check_prime.py
   
   3. Input any integer at the prompt.
   4. The script returns True if prime and False if composite.

## 📝 Example

* Input: 17 → Output: True
* Input: 25 → Output: False

