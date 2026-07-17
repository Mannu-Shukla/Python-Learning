# Type Casting

## What is Type Casting?

Type Casting is the process of converting one data type into another.

### Types of Type Casting

- Implicit Type Casting (Automatic)
- Explicit Type Casting (Manual)


---

## Key Points

- Type casting changes the data type of a value.
- Python performs implicit type casting automatically.
- Explicit type casting is done using functions like `int()`, `float()`, `str()`, and `bool()`.
- `int(9.8)` returns `9` (it removes the decimal part).
- `int("Hello")` gives an error because `"Hello"` is not a numeric string.

---

## Common Examples

```python
age = "21"
age = int(age)

marks = 95
marks = float(marks)

num = 123
num = str(num)

value = bool(1)
```

---

**Status:** ✅ Completed