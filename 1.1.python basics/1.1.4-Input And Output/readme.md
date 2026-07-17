# Input & Output

## What is Output?

Output is the information displayed by a program to the user.

### `print()` Function

The `print()` function is used to display output on the screen.

**Example:**

```python
print("Hello, World!")
```

---

## Printing Multiple Values

You can print multiple values in a single `print()` statement.

**Example:**

```python
name = "Mannu"
age = 21

print(name, age)
```

---

## `sep` Parameter

The `sep` parameter specifies the separator between multiple values.

**Example:**

```python
print("Python", "Java", "C++", sep="-")
```

**Output:**

```
Python-Java-C++
```

---

## `end` Parameter

The `end` parameter changes what is printed at the end of a `print()` statement.

**Example:**

```python
print("Hello", end=" ")
print("World")
```

**Output:**

```
Hello World
```

---

## What is Input?

Input is the information provided by the user to the program.

### `input()` Function

The `input()` function is used to take input from the user.

**Example:**

```python
name = input("Enter your name: ")
print(name)
```

---

## Type Casting User Input

The `input()` function always returns a string.

To perform mathematical operations, convert the input to an integer or float.

**Example:**

```python
age = int(input("Enter your age: "))
print(age + 5)
```

---

## f-Strings

f-Strings are used to insert variables or expressions inside strings.

**Example:**

```python
name = "Mannu"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

---

## Escape Characters

| Escape Character | Description |
|------------------|-------------|
| `\n` | New Line |
| `\t` | Horizontal Tab |
| `\"` | Double Quote |
| `\\` | Backslash |

**Example:**

```python
print("Python\nJava")
```

---

## Comments

Comments are used to explain code and are ignored by Python.

### Single-line Comment

```python
# This is a comment
```

### Multi-line Comment

```python
"""
This is a multi-line comment.
"""
```

---

## Key Points

- `print()` displays output.
- `input()` takes input from the user.
- `input()` always returns a string.
- Use `int()` or `float()` to convert numeric input.
- `sep` changes the separator between printed values.
- `end` changes what is printed at the end of a line.
- f-Strings make string formatting simple and readable.
- Escape characters help format text.
- Comments improve code readability.

---

## Common Examples

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1} years old.")

print("Python", "Java", "C++", sep=" | ")

print("Hello", end=" ")
print("World")

print("Line1\nLine2")
```

---

**Status:** ✅ Completed