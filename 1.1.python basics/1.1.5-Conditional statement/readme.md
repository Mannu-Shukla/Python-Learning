# Conditional Statements

## What are Conditional Statements?

Conditional statements allow a program to make decisions based on a condition.

---

## Types of Conditional Statements

### `if`

Executes a block of code only if the condition is `True`.

```python
if age >= 18:
    print("Eligible to Vote")
```

---

### `if...else`

Executes one block if the condition is `True` and another block if it is `False`.

```python
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

### `if...elif...else`

Used when there are multiple conditions to check.

```python
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

---

### Nested `if`

An `if` statement inside another `if` statement.

```python
if age >= 18:
    if has_id:
        print("Entry Allowed")
```

---

## Key Points

- `if` checks a condition.
- `else` runs when the `if` condition is `False`.
- `elif` is used to check multiple conditions.
- Python uses **indentation** to define code blocks.
- Conditions can be combined using `and`, `or`, and `not`.
- Python executes the first `True` condition in an `if-elif-else` chain and skips the rest.

---

## Common Examples

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

**Status:** ✅ Completed